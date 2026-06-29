from typing import Dict, List
from .parser import APIEntry


class BadgeGenerator:
    """Generate badge URLs for API entries."""
    
    # Badge color mappings
    COLOR_MAPPINGS = {
        'https': {
            'Yes': 'brightgreen',
            'No': 'red',
            'Unknown': 'orange'
        },
        'auth': {
            'No': 'brightgreen',
            'apiKey': 'yellow',
            'OAuth': 'blue',
            'X-Mashape-Key': 'orange',
            'Unknown': 'lightgrey'
        },
        'cors': {
            'Yes': 'brightgreen',
            'No': 'red',
            'Unknown': 'orange'
        }
    }
    
    def __init__(self):
        self.base_url = "https://img.shields.io/badge/"
    
    def generate_badges(self, entry: APIEntry) -> Dict[str, str]:
        """Generate badge URLs for an API entry."""
        return {
            'https': self._generate_https_badge(entry.https),
            'auth': self._generate_auth_badge(entry.auth),
            'cors': self._generate_cors_badge(entry.cors)
        }
    
    def _generate_https_badge(self, https_value: str) -> str:
        """Generate HTTPS badge URL."""
        color = self.COLOR_MAPPINGS['https'].get(https_value, 'lightgrey')
        label = "HTTPS"
        message = https_value.replace(' ', '_')
        return f"{self.base_url}{label}-{message}-{color}"
    
    def _generate_auth_badge(self, auth_value: str) -> str:
        """Generate Auth badge URL."""
        color = self.COLOR_MAPPINGS['auth'].get(auth_value, 'lightgrey')
        label = "Auth"
        message = auth_value.replace(' ', '_')
        return f"{self.base_url}{label}-{message}-{color}"
    
    def _generate_cors_badge(self, cors_value: str) -> str:
        """Generate CORS badge URL."""
        color = self.COLOR_MAPPINGS['cors'].get(cors_value, 'lightgrey')
        label = "CORS"
        message = cors_value.replace(' ', '_')
        return f"{self.base_url}{label}-{message}-{color}"
    
    def generate_all_badges(self, entries: List[APIEntry]) -> List[Dict]:
        """Generate badges for all API entries."""
        results = []
        for entry in entries:
            badges = self.generate_badges(entry)
            results.append({
                'entry': entry,
                'badges': badges
            })
        return results