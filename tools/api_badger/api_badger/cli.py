import os
import click
from flask import Flask, render_template_string
from .parser import MarkdownParser
from .readme_generator import ReadmeGenerator
from .html_generator import HtmlGenerator
from .csv_exporter import CsvExporter


@click.group()
def cli():
    """API Badger - Generate badges for public APIs from README.md"""
    pass


@cli.command()
@click.option('--input-file', '-i', default='README.md', help='Input markdown file')
@click.option('--out-dir', '-o', default='output', help='Output directory')
@click.option('--skip-invalid', is_flag=True, help='Skip invalid entries')
def build(input_file, out_dir, skip_invalid):
    """Build README with badges and HTML page."""
    click.echo(f"🔨 Building API badges from {input_file}...")
    
    # Create output directory
    os.makedirs(out_dir, exist_ok=True)
    
    # Parse markdown
    parser = MarkdownParser()
    try:
        entries = parser.parse_file(input_file)
        click.echo(f"📊 Found {len(entries)} API entries")
    except FileNotFoundError:
        click.echo(f"❌ Error: Input file '{input_file}' not found")
        return
    except Exception as e:
        click.echo(f"❌ Error parsing file: {e}")
        return
    
    # Filter invalid entries if requested
    if skip_invalid:
        original_count = len(entries)
        entries = [e for e in entries if e.link and e.name]
        filtered_count = original_count - len(entries)
        if filtered_count > 0:
            click.echo(f"🚫 Skipped {filtered_count} invalid entries")
    
    # Generate README with badges
    readme_gen = ReadmeGenerator()
    readme_path = os.path.join(out_dir, 'README_BADGES.md')
    readme_gen.generate_readme_badges(entries, readme_path)
    click.echo(f"✅ Generated README with badges: {readme_path}")
    
    # Generate HTML page
    html_gen = HtmlGenerator()
    html_path = os.path.join(out_dir, 'index.html')
    html_gen.generate_html(entries, html_path)
    click.echo(f"✅ Generated HTML page: {html_path}")
    
    click.echo(f"🎉 Build complete! Check the {out_dir} directory.")


@cli.command()
@click.option('--input-file', '-i', default='README.md', help='Input markdown file')
@click.option('--out-dir', '-o', default='output', help='Output directory')
@click.option('--skip-invalid', is_flag=True, help='Skip invalid entries')
def export_csv(input_file, out_dir, skip_invalid):
    """Export API data to CSV format."""
    click.echo(f"📤 Exporting API data to CSV from {input_file}...")
    
    # Create output directory
    os.makedirs(out_dir, exist_ok=True)
    
    # Parse markdown
    parser = MarkdownParser()
    try:
        entries = parser.parse_file(input_file)
        click.echo(f"📊 Found {len(entries)} API entries")
    except FileNotFoundError:
        click.echo(f"❌ Error: Input file '{input_file}' not found")
        return
    except Exception as e:
        click.echo(f"❌ Error parsing file: {e}")
        return
    
    # Filter invalid entries if requested
    if skip_invalid:
        original_count = len(entries)
        entries = [e for e in entries if e.link and e.name]
        filtered_count = original_count - len(entries)
        if filtered_count > 0:
            click.echo(f"🚫 Skipped {filtered_count} invalid entries")
    
    # Export to CSV
    csv_exporter = CsvExporter()
    csv_path = os.path.join(out_dir, 'api_data.csv')
    csv_exporter.export_to_csv(entries, csv_path)
    click.echo(f"✅ Exported CSV data: {csv_path}")
    
    click.echo(f"🎉 CSV export complete!")


@cli.command()
@click.option('--input-file', '-i', default='README.md', help='Input markdown file')
@click.option('--out-dir', '-o', default='output', help='Output directory')
@click.option('--port', '-p', default=8080, help='Port to serve on')
@click.option('--skip-invalid', is_flag=True, help='Skip invalid entries')
def serve(input_file, out_dir, port, skip_invalid):
    """Build and serve the HTML page."""
    click.echo(f"🚀 Building and serving API badges...")
    
    # First build the files
    build.callback(input_file, out_dir, skip_invalid)
    
    # Create Flask app
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        html_path = os.path.join(out_dir, 'index.html')
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return "HTML file not found. Please run 'build' command first.", 404
    
    @app.route('/api_data.csv')
    def csv_data():
        csv_path = os.path.join(out_dir, 'api_data.csv')
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as f:
                return f.read(), 200, {'Content-Type': 'text/csv'}
        else:
            return "CSV file not found.", 404
    
    click.echo(f"🌐 Starting server on http://localhost:{port}")
    click.echo(f"📁 Serving files from {out_dir}")
    click.echo("Press Ctrl+C to stop the server")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=False)
    except KeyboardInterrupt:
        click.echo("\n👋 Server stopped")


def main():
    """Main entry point."""
    cli()


if __name__ == '__main__':
    main()