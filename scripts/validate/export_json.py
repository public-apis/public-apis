# -*- coding: utf-8 -*-
import re
import json
import sys
from typing import List, Dict

def parse_readme_to_json(filename: str) -> Dict:
    """Parse README.md and convert API entries to JSON format."""
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    
    apis_data = {"categories": []}
    current_category = None
    link_re = re.compile(r'\[(.+)\]\((http.*)\)')
    
    for line in lines:
        if line.startswith('### '):
            category_name = line.replace('###', '').strip()
            current_category = {
                "name": category_name,
                "apis": []
            }
            apis_data["categories"].append(current_category)
        
        elif line.startswith('|') and not line.startswith('|---') and current_category:
            segments = [seg.strip() for seg in line.split('|')[1:-1]]
            if len(segments) >= 5:
                title_match = link_re.match(segments[0])
                if title_match:
                    api_entry = {
                        "name": title_match.group(1),
                        "url": title_match.group(2),
                        "description": segments[1],
                        "auth": segments[2].replace('`', ''),
                        "https": segments[3] == "Yes",
                        "cors": segments[4]
                    }
                    current_category["apis"].append(api_entry)
    
    return apis_data

def main(filename: str, output: str = "public_apis.json"):
    data = parse_readme_to_json(filename)
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(data['categories'])} categories to {output}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python export_json.py README.md [output.json]')
        sys.exit(1)
    
    filename = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "public_apis.json"
    main(filename, output)
