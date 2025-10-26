# Test script for the scraper API
# Run this to test the API locally

import requests
import time

BASE_URL = "http://localhost:8000"

def test_endpoints():
    """Test all API endpoints"""
    
    # Test home endpoint
    print("Testing home endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test health endpoint
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test scrape endpoints (these will return placeholder data)
    endpoints = [
        "/scrape/imdb_top_picks",
        "/scrape/imdb_fan_favorites", 
        "/scrape/imdb_popular",
        "/scrape/latest"
    ]
    
    for endpoint in endpoints:
        print(f"Testing {endpoint}...")
        response = requests.get(f"{BASE_URL}{endpoint}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
        time.sleep(1)  # Small delay between requests

if __name__ == "__main__":
    test_endpoints()