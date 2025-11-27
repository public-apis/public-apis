#!/usr/bin/env python3
"""
API Browser Tests

Unit tests for the API Browser tool.
"""

import os
import tempfile
import unittest
from unittest.mock import patch, mock_open
from typing import List, Dict

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import parser
import filter
import cache
import cli

class TestParser(unittest.TestCase):
    """Tests for the parser module."""
    
    def test_parse_apis_from_readme(self):
        """Test parsing APIs from a sample README content."""
        sample_readme = """### Development

| API | Description | Auth | HTTPS | CORS |
| --- | --- | --- | --- | --- |
| [GitHub API](https://api.github.com) | GitHub API for accessing repositories, users, etc. | OAuth | Yes | Yes |
| [OpenWeatherMap API](https://api.openweathermap.org) | Weather data API | apiKey | Yes | Yes |

### Social

| API | Description | Auth | HTTPS | CORS |
| --- | --- | --- | --- | --- |
| [Twitter API](https://api.twitter.com) | Twitter API for accessing tweets and users | OAuth | Yes | No |
"""
        
        with patch("builtins.open", mock_open(read_data=sample_readme)):
            apis = parser.parse_apis_from_readme("../../README.md")
        
        self.assertEqual(len(apis), 3)
        
        # Check first API
        self.assertEqual(apis[0]['name'], 'GitHub API')
        self.assertEqual(apis[0]['description'], 'GitHub API for accessing repositories, users, etc. ')
        self.assertEqual(apis[0]['auth'], 'OAuth')
        self.assertEqual(apis[0]['https'], 'Yes')
        self.assertEqual(apis[0]['cors'], 'Yes')
        self.assertEqual(apis[0]['link'], 'https://api.github.com')
        self.assertEqual(apis[0]['category'], 'Development')
        
        # Check second API
        self.assertEqual(apis[1]['name'], 'OpenWeatherMap API')
        self.assertEqual(apis[1]['category'], 'Development')
        
        # Check third API
        self.assertEqual(apis[2]['name'], 'Twitter API')
        self.assertEqual(apis[2]['category'], 'Social')

class TestFilter(unittest.TestCase):
    """Tests for the filter module."""
    
    def setUp(self):
        """Set up test data."""
        self.test_apis = [
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
                'cors': 'Yes',
                'link': 'https://api.twitter.com',
                'category': 'Social'
            }
        ]
    
    def test_filter_by_category(self):
        """Test filtering APIs by category."""
        filtered = filter.filter_apis(self.test_apis, category='Development')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'GitHub API')
        
        # Test case insensitivity
        filtered = filter.filter_apis(self.test_apis, category='development')
        self.assertEqual(len(filtered), 1)
        
        # Test non-existent category
        filtered = filter.filter_apis(self.test_apis, category='NonExistent')
        self.assertEqual(len(filtered), 0)
    
    def test_filter_by_query(self):
        """Test filtering APIs by query."""
        filtered = filter.filter_apis(self.test_apis, query='Weather')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'OpenWeatherMap API')
        
        # Test query in description
        filtered = filter.filter_apis(self.test_apis, query='repositories')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'GitHub API')
        
        # Test case insensitivity
        filtered = filter.filter_apis(self.test_apis, query='twitter')
        self.assertEqual(len(filtered), 1)
        
        # Test non-existent query
        filtered = filter.filter_apis(self.test_apis, query='NonExistent')
        self.assertEqual(len(filtered), 0)
    
    def test_filter_by_category_and_query(self):
        """Test filtering APIs by both category and query."""
        filtered = filter.filter_apis(self.test_apis, query='OAuth', category='Social')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['name'], 'Twitter API')
        
        # Test no matches
        filtered = filter.filter_apis(self.test_apis, query='OAuth', category='Weather')
        self.assertEqual(len(filtered), 0)

class TestCache(unittest.TestCase):
    """Tests for the cache module."""
    
    def setUp(self):
        """Set up test data."""
        self.test_apis = [
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
        
        # Create a temporary directory for cache files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cache_file = os.path.join(self.temp_dir.name, 'test_cache.json')
    
    def tearDown(self):
        """Clean up test data."""
        self.temp_dir.cleanup()
    
    def test_cache_save_load(self):
        """Test saving and loading from cache."""
        cache_manager = cache.CacheManager(self.cache_file, cache_duration=60)
        
        # Save to cache
        cache_manager.save(self.test_apis)
        
        # Load from cache
        loaded_apis = cache_manager.load()
        
        self.assertEqual(len(loaded_apis), 1)
        self.assertEqual(loaded_apis[0]['name'], 'Test API')
    
    def test_cache_validity(self):
        """Test cache validity check."""
        cache_manager = cache.CacheManager(self.cache_file, cache_duration=1)  # 1 second
        
        # Cache is initially invalid
        self.assertFalse(cache_manager.is_valid())
        
        # Save to cache
        cache_manager.save(self.test_apis)
        
        # Cache is now valid
        self.assertTrue(cache_manager.is_valid())
        
        # Wait for cache to expire
        import time
        time.sleep(2)
        
        # Cache is now invalid
        self.assertFalse(cache_manager.is_valid())
    
    def test_cache_clear(self):
        """Test clearing the cache."""
        cache_manager = cache.CacheManager(self.cache_file)
        
        # Save to cache
        cache_manager.save(self.test_apis)
        self.assertTrue(os.path.exists(self.cache_file))
        
        # Clear cache
        cache_manager.clear()
        self.assertFalse(os.path.exists(self.cache_file))

class TestCLI(unittest.TestCase):
    """Tests for the CLI module."""
    
    @patch('sys.argv', ['cli.py', '-q', 'weather'])
    def test_parse_args_query(self):
        """Test parsing command line arguments with query."""
        args = cli.parse_args()
        self.assertEqual(args.query, 'weather')
        self.assertIsNone(args.category)
        self.assertEqual(args.output, 'table')
        self.assertFalse(args.cache_refresh)
    
    @patch('sys.argv', ['cli.py', '-c', 'development'])
    def test_parse_args_category(self):
        """Test parsing command line arguments with category."""
        args = cli.parse_args()
        self.assertIsNone(args.query)
        self.assertEqual(args.category, 'development')
        self.assertEqual(args.output, 'table')
        self.assertFalse(args.cache_refresh)
    
    @patch('sys.argv', ['cli.py', '-o', 'json'])
    def test_parse_args_output_json(self):
        """Test parsing command line arguments with JSON output."""
        args = cli.parse_args()
        self.assertEqual(args.output, 'json')
    
    @patch('sys.argv', ['cli.py', '--cache-refresh'])
    def test_parse_args_cache_refresh(self):
        """Test parsing command line arguments with cache refresh."""
        args = cli.parse_args()
        self.assertTrue(args.cache_refresh)
    
    @patch('sys.argv', ['cli.py', '-q', 'weather', '-c', 'development', '-o', 'json', '--cache-refresh'])
    def test_parse_args_combined(self):
        """Test parsing command line arguments with all options."""
        args = cli.parse_args()
        self.assertEqual(args.query, 'weather')
        self.assertEqual(args.category, 'development')
        self.assertEqual(args.output, 'json')
        self.assertTrue(args.cache_refresh)

if __name__ == '__main__':
    unittest.main()
