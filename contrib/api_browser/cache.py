#!/usr/bin/env python3
"""
API Cache

This module handles caching of the parsed APIs list to a local file.
"""

import json
import os
import time
from typing import List, Dict

CACHE_FILE = "apis_cache.json"
CACHE_DURATION = 24 * 60 * 60  # 24 hours in seconds

class CacheManager:
    """Manages the local cache of APIs data."""
    
    def __init__(self, cache_file: str = CACHE_FILE, cache_duration: int = CACHE_DURATION):
        """Initialize the CacheManager.
        
        Args:
            cache_file: Path to the cache file
            cache_duration: Cache duration in seconds
        """
        self.cache_file = cache_file
        self.cache_duration = cache_duration
    
    def is_valid(self) -> bool:
        """Check if the cache is valid (exists and not expired).
        
        Returns:
            True if cache is valid, False otherwise
        """
        if not os.path.exists(self.cache_file):
            return False
        
        # Check if cache is expired
        file_mod_time = os.path.getmtime(self.cache_file)
        current_time = time.time()
        
        return (current_time - file_mod_time) < self.cache_duration
    
    def load(self) -> List[Dict]:
        """Load APIs from the cache file.
        
        Returns:
            List of APIs loaded from cache
        """
        with open(self.cache_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return data['apis']
    
    def save(self, apis: List[Dict]) -> None:
        """Save APIs to the cache file.
        
        Args:
            apis: List of APIs to save to cache
        """
        data = {
            'timestamp': time.time(),
            'apis': apis
        }
        
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def clear(self) -> None:
        """Clear the cache by deleting the cache file."""
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)

if __name__ == "__main__":
    # Test the CacheManager
    cache_manager = CacheManager()
    
    # Test save and load
    test_apis = [
        {
            'name': 'Test API',
            'description': 'Test API description',
            'auth': 'No',
            'https': 'Yes',
            'cors': 'Yes',
            'link': 'https://example.com',
            'category': 'Test'
        }
    ]
    
    print("Saving test APIs to cache...")
    cache_manager.save(test_apis)
    
    print(f"Cache is valid: {cache_manager.is_valid()}")
    
    print("Loading APIs from cache...")
    loaded_apis = cache_manager.load()
    print(f"Loaded {len(loaded_apis)} APIs")
    
    # Test clear
    print("Clearing cache...")
    cache_manager.clear()
    print(f"Cache is valid: {cache_manager.is_valid()}")
