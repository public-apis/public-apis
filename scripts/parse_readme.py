import re
import json

def parse_readme():
    """
    Parses the README.md file to extract API data and saves it as a JSON file.
    """
    apis = []
    current_category = ""

    with open("README.md", "r", encoding="utf-8") as f:
        for line in f:
            # Check for category headers
            category_match = re.match(r"^###\s(.+)", line)
            if category_match:
                current_category = category_match.group(1).strip()
                continue

            # Check for API table rows
            # Format: | [API_NAME](API_LINK) | DESCRIPTION | AUTH | HTTPS | CORS |
            api_match = re.match(r"\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|", line)
            if api_match and current_category:
                api_name = api_match.group(1).strip()
                api_link = api_match.group(2).strip()
                api_description = api_match.group(3).strip()
                api_auth = api_match.group(4).strip()
                api_https = api_match.group(5).strip()
                api_cors = api_match.group(6).strip()

                apis.append({
                    "category": current_category,
                    "name": api_name,
                    "link": api_link,
                    "description": api_description,
                    "auth": api_auth,
                    "https": api_https,
                    "cors": api_cors,
                })

    # Write the data to a JSON file
    with open("scripts/apis.json", "w", encoding="utf-8") as f:
        json.dump({"count": len(apis), "entries": apis}, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    parse_readme()
    print("Successfully parsed README.md and created scripts/apis.json")
