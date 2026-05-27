import json
import os

def search_api(keyword):
    # Debugging info (helps you understand path issues)
    print("Current directory:", os.getcwd())
    print("Files here:", os.listdir())

    # Load JSON file
    with open("api-list.json", "r") as file:
        data = json.load(file)

    results = []
    keyword = keyword.lower()

    for item in data:
        item_name = item["API"].lower()
        item_desc = item["Description"].lower()

        if keyword in item_name or keyword in item_desc:
            results.append(item)

    return results

# MAIN PROGRAM
if __name__ == "__main__":
    keyword = input("Enter keyword to search: ")
    matches = search_api(keyword)

    print("\nSearch Results:")
    for m in matches:
        print(f"- {m['API']}: {m['Description']}")