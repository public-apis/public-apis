#!/usr/bin/env python3
"""
API Parser

This module parses the public APIs list from the README.md file.
"""

import re
from typing import List, Dict

def parse_apis_from_readme(file_path: str) -> List[Dict]:
    """Parse APIs from the README.md file and return a list of dictionaries.
    
    Args:
        file_path: Path to the README.md file
        
    Returns:
        List of APIs, each represented as a dictionary with keys: 
        'name', 'description', 'auth', 'https', 'cors', 'link', 'category'
    """
    apis = []
    current_category = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Regular expressions to match different parts of the README
    category_re = re.compile(r'###\s+(.+)')
    table_header_re = re.compile(r'\| API \| Description \| Auth \| HTTPS \| CORS \|')
    table_row_re = re.compile(r'\|\s*\[(.+)\]\((https?://[^)]+)\)\s*\|\s*(.+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|')
    
    in_table = False
    
    for line in lines:
        line = line.strip()
        
        # Check if this is a category header
        category_match = category_re.match(line)
        if category_match:
            current_category = category_match.group(1)
            in_table = False
            continue
        
        # Check if this is the start of a table
        if table_header_re.match(line):
            in_table = True
            continue
        
        # Check if this is a table row
        if in_table and line.startswith('|'):
            row_match = table_row_re.match(line)
            if row_match:
                name = row_match.group(1)
                link = row_match.group(2)
                description = row_match.group(3)
                auth = row_match.group(4)
                https = row_match.group(5)
                cors = row_match.group(6)
                
                # Clean up the fields
                auth = auth.strip() if auth.strip() != '' else 'No'
                https = https.strip() if https.strip() != '' else 'No'
                cors = cors.strip() if cors.strip() != '' else 'Unknown'
                
                api = {
                    'name': name,
                    'description': description,
                    'auth': auth,
                    'https': https,
                    'cors': cors,
                    'link': link,
                    'category': current_category
                }
                
                apis.append(api)
    
    return apis

if __name__ == "__main__":
    # Test the parser
    apis = parse_apis_from_readme("../../README.md")
    print(f"Parsed {len(apis)} APIs")
    for api in apis[:5]:
        print(f"- {api['name']} ({api['category']})")
