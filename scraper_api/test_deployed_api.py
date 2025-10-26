#!/usr/bin/env python3
"""
Test script for the deployed Movie Wiki Scraper API
"""

import requests
import time

# Replace this with your actual Deta Space URL after deployment
DETA_SPACE_URL = "https://movie-wiki-scraper-1234567890.deta.app"

def test_api_endpoints(base_url):
    """Test all API endpoints"""
    
    # Test home endpoint
    print("Testing home endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    print()
    
    # Test scraping endpoints
    endpoints = [
        "/scrape/imdb_top_picks",
        "/scrape/imdb_fan_favorites",
        "/scrape/imdb_popular",
        "/scrape/latest"
    ]
    
    for endpoint in endpoints:
        print(f"Testing {endpoint}...")
        try:
            response = requests.get(f"{base_url}{endpoint}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"Items found: {data.get('count', len(data.get('items', [])))}")
                if 'items' in data and len(data['items']) > 0:
                    first_item = data['items'][0]
                    print(f"Sample item: {first_item['title']} ({first_item['year']})")
            else:
                print(f"Error response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        print()
        time.sleep(1)  # Small delay between requests

def main():
    """Main test function"""
    print("Movie Wiki Scraper API Test Script")
    print("=" * 35)
    print(f"Testing API at: {DETA_SPACE_URL}")
    print()
    
    test_api_endpoints(DETA_SPACE_URL)
    
    print("Test completed!")

if __name__ == "__main__":
    main()