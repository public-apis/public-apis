import json
import random
import subprocess
from flask import Flask, jsonify, request, render_template

# Create the Flask application
app = Flask(__name__, template_folder='../dashboard/templates', static_folder='../dashboard/static')

# Load the API data from the JSON file
try:
    with open("scripts/apis.json", "r", encoding="utf-8") as f:
        api_data = json.load(f)
        all_entries = api_data.get("entries", [])
except FileNotFoundError:
    print("Error: scripts/apis.json not found. Please run scripts/parse_readme.py first.")
    all_entries = []

@app.route('/', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Serves the dashboard page.
    """
    return render_template('index.html')

@app.route('/sync', methods=['POST'])
def sync_repository():
    """
    Syncs the repository with the parent and updates the API data.
    """
    try:
        # Check if upstream remote exists
        remotes = subprocess.check_output(['git', 'remote']).decode('utf-8')
        if 'upstream' not in remotes.split('\n'):
            subprocess.run(['git', 'remote', 'add', 'upstream', 'https://github.com/public-apis/public-apis.git'], check=True)

        # Fetch and merge from upstream
        subprocess.run(['git', 'fetch', 'upstream'], check=True)
        subprocess.run(['git', 'merge', 'upstream/master'], check=True)

        # Rerun the parsing script
        subprocess.run(['python3', 'scripts/parse_readme.py'], check=True)

        return jsonify({"success": True, "message": "Sync completed successfully."})
    except subprocess.CalledProcessError as e:
        return jsonify({"success": False, "message": f"An error occurred during sync: {e.stderr.decode('utf-8') if e.stderr else str(e)}"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({"status": "ok"}), 200

@app.route('/entries', methods=['GET'])
def get_entries():
    """
    Returns API entries. Can be filtered by category.
    """
    if not all_entries:
        return jsonify({"error": "No entries available. Run the parsing script."}), 500

    category_query = request.args.get('category')
    if category_query:
        # Filter entries by category (case-insensitive)
        filtered_entries = [
            entry for entry in all_entries
            if entry.get('category', '').lower() == category_query.lower()
        ]
        return jsonify({"count": len(filtered_entries), "entries": filtered_entries})
    else:
        # Return all entries
        return jsonify({"count": len(all_entries), "entries": all_entries})

@app.route('/categories', methods=['GET'])
def get_categories():
    """
    Returns a list of all unique categories.
    """
    if not all_entries:
        return jsonify({"error": "No entries available. Run the parsing script."}), 500

    categories = sorted(list(set(entry.get("category") for entry in all_entries if "category" in entry)))
    return jsonify(categories)

@app.route('/random', methods=['GET'])
def get_random_entry():
    """
    Returns a random API entry.
    """
    if not all_entries:
        return jsonify({"error": "No entries available. Run the parsing script."}), 500

    random_entry = random.choice(all_entries)
    return jsonify(random_entry)

if __name__ == '__main__':
    # This is for development purposes only.
    # For a production environment, use a proper WSGI server like Gunicorn.
    app.run(host='0.0.0.0', port=5000, debug=True)
