import json
import os
import sys


def load_json_file(path: str):
    """
    Safely load JSON from a file path.

    Provides user-friendly error messages and clean exits
    instead of raw stack traces.
    """

    if not os.path.exists(path):
        print(f"❌ Error: File not found: {path}")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing failed in {path}: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error reading {path}: {e}")
        sys.exit(1)
