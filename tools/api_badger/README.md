# API Badger 🚀

Generate beautiful badges for public APIs from README.md files. This tool parses API tables from markdown files and generates visual badges for HTTPS, Authentication, and CORS status.

## Features

- 📊 **Parse API Tables**: Extract API information from markdown tables
- 🏷️ **Generate Badges**: Create visual badges using shields.io for HTTPS, Auth, and CORS
- 📄 **README Generation**: Generate enhanced README with badge tables
- 🌐 **HTML Output**: Create beautiful static HTML pages with API listings
- 📋 **CSV Export**: Export API data to CSV format with badge URLs
- 🖥️ **CLI Interface**: Easy-to-use command line interface
- 🧪 **Comprehensive Tests**: Full test coverage with pytest

## Installation

### From Source

```bash
cd tools/api_badger
pip install -r requirements.txt
pip install -e .
```

### Development Installation

```bash
cd tools/api_badger
pip install -r requirements.txt
pip install -e .[dev]
```

## Usage

### Basic Commands

#### Build README with badges and HTML page
```bash
# Default: Use README.md and create output in 'output' directory
api-badger build

# Custom input file and output directory
api-badger build -i custom_readme.md -o my_output

# Skip invalid entries
api-badger build --skip-invalid
```

#### Export to CSV
```bash
# Export API data to CSV
api-badger export-csv

# Custom output directory
api-badger export-csv -o csv_output
```

#### Serve HTML page
```bash
# Build and serve on default port 8080
api-badger serve

# Custom port
api-badger serve -p 3000

# Custom input file and skip invalid entries
api-badger serve -i README.md --skip-invalid
```

### Command Options

#### `build` command
- `--input-file, -i`: Input markdown file (default: README.md)
- `--out-dir, -o`: Output directory (default: output)
- `--skip-invalid`: Skip invalid API entries

#### `export-csv` command
- `--input-file, -i`: Input markdown file (default: README.md)
- `--out-dir, -o`: Output directory (default: output)
- `--skip-invalid`: Skip invalid API entries

#### `serve` command
- `--input-file, -i`: Input markdown file (default: README.md)
- `--out-dir, -o`: Output directory (default: output)
- `--port, -p`: Port to serve on (default: 8080)
- `--skip-invalid`: Skip invalid API entries

## Output Files

### README_BADGES.md
Enhanced version of the original README with badge columns showing:
- 🔒 **HTTPS Badge**: Shows if API supports HTTPS
- 🔑 **Auth Badge**: Shows authentication requirements
- 🌐 **CORS Badge**: Shows CORS support status

### index.html
Beautiful static HTML page featuring:
- 📱 Responsive design
- 🎨 Modern card-based layout
- 🔗 Clickable API links
- 🏷️ Visual badges for each API
- 📋 Category navigation
- ⚡ Smooth scrolling and interactions

### api_data.csv
Complete CSV export with columns:
- name, description, auth, https, cors, link, category
- https_badge, auth_badge, cors_badge (badge URLs)

## Badge Colors

The tool uses the following color scheme for badges:

### HTTPS Badge
- ✅ **Yes**: Bright Green
- ❌ **No**: Red
- ❓ **Unknown**: Orange

### Auth Badge
- 🔓 **No**: Bright Green
- 🔑 **apiKey**: Yellow
- 🔐 **OAuth**: Blue
- 🔧 **X-Mashape-Key**: Orange
- ❓ **Unknown**: Light Grey

### CORS Badge
- ✅ **Yes**: Bright Green
- ❌ **No**: Red
- ❓ **Unknown**: Orange

## Examples

### Sample Badge URLs Generated
```
HTTPS: https://img.shields.io/badge/HTTPS-Yes-brightgreen
Auth: https://img.shields.io/badge/Auth-apiKey-yellow
CORS: https://img.shields.io/badge/CORS-Yes-brightgreen
```

### Sample HTML Output
The HTML output creates a beautiful, responsive page with:
- Grid layout of API cards
- Hover effects and animations
- Category-based navigation
- Mobile-friendly responsive design

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=api_badger

# Run specific test file
pytest tests/test_api_badger.py
```

## Development

### Project Structure
```
api_badger/
├── api_badger/
│   ├── __init__.py
│   ├── parser.py          # Markdown parsing logic
│   ├── badges.py          # Badge URL generation
│   ├── readme_generator.py # README with badges
│   ├── html_generator.py  # HTML page generation
│   ├── csv_exporter.py    # CSV export functionality
│   └── cli.py             # Command line interface
├── tests/
│   ├── __init__.py
│   └── test_api_badger.py # Comprehensive tests
├── requirements.txt
├── setup.py
└── README.md
```

### Adding New Features

1. **New Badge Types**: Extend `BadgeGenerator` class in `badges.py`
2. **New Output Formats**: Create new generator classes
3. **New CLI Commands**: Add to `cli.py` using Click framework

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is part of the public-apis repository and follows the same licensing terms.

## Support

For issues and feature requests, please use the GitHub issue tracker.

---

Made with ❤️ by the API Badger team