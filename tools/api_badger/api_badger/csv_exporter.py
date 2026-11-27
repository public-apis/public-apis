import csv
from typing import List
from .parser import APIEntry
from .badges import BadgeGenerator


class CsvExporter:
    """Export API entries to CSV format with badges."""
    
    def __init__(self):
        self.badge_generator = BadgeGenerator()
    
    def export_to_csv(self, entries: List[APIEntry], output_path: str):
        """Export API entries to CSV file."""
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'description', 'auth', 'https', 'cors', 'link', 'category', 
                         'https_badge', 'auth_badge', 'cors_badge']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for entry in entries:
                badges = self.badge_generator.generate_badges(entry)
                writer.writerow({
                    'name': entry.name,
                    'description': entry.description,
                    'auth': entry.auth,
                    'https': entry.https,
                    'cors': entry.cors,
                    'link': entry.link,
                    'category': entry.category,
                    'https_badge': badges['https'],
                    'auth_badge': badges['auth'],
                    'cors_badge': badges['cors']
                })