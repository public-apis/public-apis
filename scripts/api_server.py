import json
import random
import subprocess
import os
from flask import Flask, jsonify, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

# Create the Flask application
app = Flask(__name__, template_folder='../dashboard/templates', static_folder='../dashboard/static')

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
apis_json_path = os.path.join(script_dir, "apis.json")
parse_script_path = os.path.join(script_dir, "parse_readme.py")

# Load the API data from the JSON file
try:
    with open(apis_json_path, "r", encoding="utf-8") as f:
        api_data = json.load(f)
        all_entries = api_data.get("entries", [])
except FileNotFoundError:
    print(f"Error: {apis_json_path} not found. Please run scripts/parse_readme.py first.")
    all_entries = []

def do_sync():
    """
    This function contains the logic to sync the repository.
    """
    print("Performing sync...")
    try:
        # Check if upstream remote exists
        remotes = subprocess.check_output(['git', 'remote']).decode('utf-8')
        if 'upstream' not in remotes.split('\n'):
            subprocess.run(['git', 'remote', 'add', 'upstream', 'https://github.com/public-apis/public-apis.git'], check=True)

        # Fetch and merge from upstream
        subprocess.run(['git', 'fetch', 'upstream'], check=True)
        subprocess.run(['git', 'merge', 'upstream/master'], check=True)

        # Rerun the parsing script
        subprocess.run(['python3', parse_script_path], check=True)
        print("Sync completed successfully.")
        return True, "Sync completed successfully."
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred during sync: {e.stderr.decode('utf-8') if e.stderr else str(e)}"
        print(error_message)
        return False, error_message
    except Exception as e:
        error_message = f"An unexpected error occurred during sync: {str(e)}"
        print(error_message)
        return False, error_message

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
    success, message = do_sync()
    return jsonify({"success": success, "message": message})

@app.route('/next-sync-time', methods=['GET'])
def get_next_sync_time():
    """
    Returns the time of the next scheduled sync.
    """
    if scheduler.get_jobs():
        next_run = scheduler.get_jobs()[0].next_run_time
        return jsonify({'next_run_time': next_run.isoformat()})
    return jsonify({'next_run_time': None})

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

    # Set up the scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=do_sync, trigger="interval", hours=24)
    scheduler.start()
    print("Scheduler started...")

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    # To keep the main thread alive, the Flask app needs to be run.
    # The scheduler will run in the background.
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
