import re
from typing import List, Dict, Optional


class APIEntry:
    def __init__(self, name: str, description: str, auth: str = "", https: str = "", 
                 cors: str = "", link: str = "", category: str = ""):
        self.name = name
        self.description = description
        self.auth = auth or "No"
        self.https = https or "No"
        self.cors = cors or "No"
        self.link = link
        self.category = category

    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'description': self.description,
            'auth': self.auth,
            'https': self.https,
            'cors': self.cors,
            'link': self.link,
            'category': self.category
        }


class MarkdownParser:
    def __init__(self):
        self.api_entries = []
        
    def parse_file(self, file_path: str) -> List[APIEntry]:
        """Parse markdown file and extract API tables."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return self.parse_content(content)
    
    def parse_content(self, content: str) -> List[APIEntry]:
        """Parse markdown content and extract API tables."""
        self.api_entries = []
        lines = content.split('\n')
        
        current_category = ""
        in_table = False
        table_started = False
        
        for line in lines:
            line = line.strip()
            
            # Check for category headers
            if line.startswith('### '):
                current_category = line.replace('### ', '').strip()
                continue
            
            # Check for table start
            if '|' in line and 'API' in line and 'Description' in line:
                in_table = True
                table_started = True
                continue
            
            # Skip table separator lines
            if in_table and '---' in line:
                continue
            
            # Parse table rows
            if in_table and '|' in line and table_started:
                entry = self._parse_table_row(line, current_category)
                if entry:
                    self.api_entries.append(entry)
            
            # Check for table end (empty line or new section)
            if in_table and not line.strip():
                in_table = False
                table_started = False
        
        return self.api_entries
    
    def _parse_table_row(self, line: str, category: str) -> Optional[APIEntry]:
        """Parse a single table row."""
        # Clean up the line
        line = line.strip()
        if not line.startswith('|') or not line.endswith('|'):
            return None
        
        # Remove leading and trailing pipes
        line = line[1:-1].strip()
        
        # Split by pipe and clean up
        cells = [cell.strip() for cell in line.split('|')]
        
        # Skip header rows (but not API names that contain "API")
        if cells[0].strip() == 'API' or '---' in cells[0]:
            return None
        
        # Parse cells based on expected format
        if len(cells) >= 5:
            name = self._extract_name_from_link(cells[0])
            description = cells[1] if len(cells) > 1 else ""
            auth = self._clean_cell_value(cells[2] if len(cells) > 2 else "")
            https = self._clean_cell_value(cells[3] if len(cells) > 3 else "")
            cors = self._clean_cell_value(cells[4] if len(cells) > 4 else "")
            link = self._extract_link_from_name(cells[0])
            
            return APIEntry(
                name=name,
                description=description,
                auth=auth,
                https=https,
                cors=cors,
                link=link,
                category=category
            )
        elif len(cells) == 1:
            # Handle case where there might be only one cell with the API name
            name = self._extract_name_from_link(cells[0])
            link = self._extract_link_from_name(cells[0])
            
            return APIEntry(
                name=name,
                description="",
                auth="No",
                https="No",
                cors="No",
                link=link,
                category=category
            )
        
        return None
    
    def _clean_cell_value(self, value: str) -> str:
        """Clean up cell values."""
        value = value.strip()
        if not value:  # Empty string should default to "No"
            return 'No'
        elif value.lower() in ['yes', '✓', '✅']:
            return 'Yes'
        elif value.lower() in ['no', '✗', '❌']:
            return 'No'
        elif value.lower() == 'unknown':
            return 'Unknown'
        else:
            return value
    
    def _extract_name_from_link(self, cell: str) -> str:
        """Extract API name from markdown link."""
        # Match pattern [Name](url)
        match = re.search(r'\[([^\]]+)\]', cell)
        if match:
            return match.group(1).strip()
        # If no link, return the cell content
        return cell.strip()
    
    def _extract_link_from_name(self, cell: str) -> str:
        """Extract URL from markdown link."""
        # Match pattern [Name](url)
        match = re.search(r'\(([^\)]+)\)', cell)
        if match:
            return match.group(1).strip()
        return ""