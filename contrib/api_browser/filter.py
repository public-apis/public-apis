#!/usr/bin/env python3
"""
API Filter

This module filters the list of APIs based on keyword and category.
"""

from typing import List, Dict

def filter_apis(apis: List[Dict], query: str = None, category: str = None) -> List[Dict]:
    """Filter APIs based on keyword and category.
    
    Args:
        apis: List of APIs to filter
        query: Keyword to search in API name or description
        category: Category to filter by
        
    Returns:
        Filtered list of APIs
    """
    filtered = apis.copy()
    
    # Filter by category
    if category:
        filtered = [api for api in filtered if api['category'].lower() == category.lower()]
    
    # Filter by query
    if query:
        query_lower = query.lower()
        filtered = [
            api for api in filtered 
            if query_lower in api['name'].lower() or query_lower in api['description'].lower()
        ]
    
    return filtered

if __name__ == "__main__":
    # Test the filter
    test_apis = [
        {
            'name': 'GitHub API',
            'description': 'GitHub API for accessing repositories, users, etc.',
            'auth': 'OAuth',
            'https': 'Yes',
            'cors': 'Yes',
            'link': 'https://api.github.com',
            'category': 'Development'
        },
        {
            'name': 'OpenWeatherMap API',
            'description': 'Weather data API',
            'auth': 'apiKey',
            'https': 'Yes',
            'cors': 'Yes',
            'link': 'https://api.openweathermap.org',
            'category': 'Weather'
        },
        {
            'name': 'Twitter API',
            'description': 'Twitter API for accessing tweets and users',
            'auth': 'OAuth',
            'https': 'Yes',
            'cors': 'No',
            'link': 'https://api.twitter.com',
            'category': 'Social'
        }
    ]
    
    # Test category filter
    dev_apis = filter_apis(test_apis, category='Development')
    print(f"Development APIs: {[api['name'] for api in dev_apis]}")
    
    # Test query filter
    weather_apis = filter_apis(test_apis, query='weather')
    print(f"Weather APIs: {[api['name'] for api in weather_apis]}")
    
    # Test combined filter
    oauth_apis = filter_apis(test_apis, query='OAuth', category='Social')
    print(f"Social OAuth APIs: {[api['name'] for api in oauth_apis]}")
