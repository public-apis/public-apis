#!/usr/bin/env python3
"""
API Browser CLI Tool

This tool allows users to browse and filter the public APIs list from the repository.
"""

import argparse
import json
from typing import List, Dict

import parser
import filter
import cache

def main():
    """Main entry point for the API Browser CLI tool."""
    # Parse command line arguments
    args = parse_args()
    
    # Initialize cache
    cache_manager = cache.CacheManager()
    
    # Load APIs data
    if args.cache_refresh or not cache_manager.is_valid():
        # Parse from README.md if cache is invalid or refresh is requested
        apis = parser.parse_apis_from_readme("../../README.md")
        # Save to cache
        cache_manager.save(apis)
    else:
        # Load from cache
        apis = cache_manager.load()
    
    # Filter APIs
    filtered_apis = filter.filter_apis(apis, args.query, args.category)
    
    # Output results
    output_results(filtered_apis, args.output)

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Browse and filter public APIs")
    
    # Filter options
    parser.add_argument(
        "-q", "--query", 
        type=str, 
        help="Filter APIs by keyword in name or description"
    )
    parser.add_argument(
        "-c", "--category", 
        type=str, 
        help="Filter APIs by category"
    )
    
    # Output options
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        choices=["json", "table"], 
        default="table", 
        help="Output format (default: table)"
    )
    
    # Cache options
    parser.add_argument(
        "--cache-refresh", 
        action="store_true", 
        help="Force refresh the local cache"
    )
    
    return parser.parse_args()

def output_results(apis: List[Dict], format: str) -> None:
    """Output the filtered APIs in the specified format."""
    if format == "json":
        print(json.dumps(apis, indent=2))
    else:
        # Output as table
        print("{:<50} {:<100} {:<20} {:<10} {:<10}".format(
            "Name", "Description", "Auth", "HTTPS", "CORS"
        ))
        print("=" * 200)
        for api in apis:
            print("{:<50} {:<100} {:<20} {:<10} {:<10}".format(
                api["name"],
                api["description"][:97] + "..." if len(api["description"]) > 100 else api["description"],
                api["auth"],
                api["https"],
                api["cors"]
            ))

if __name__ == "__main__":
    main()
