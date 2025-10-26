#!/usr/bin/env python3
"""
Programmatic deployment script for the Movie Wiki Scraper API
"""

import os
import sys
import json
import zipfile
import requests
from pathlib import Path

def create_deployment_package():
    """Create a zip file containing all necessary files for deployment"""
    # Files to include in the deployment
    files_to_include = [
        'main.py',
        'requirements.txt',
        'runtime.txt'
    ]
    
    # Create a zip file
    zip_filename = 'deployment.zip'
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file)
            else:
                print(f"Warning: {file} not found")
    
    print(f"Created deployment package: {zip_filename}")
    return zip_filename

def deploy_to_platform():
    """Create deployment package for various platforms"""
    print("Creating deployment package...")
    package_file = create_deployment_package()
    
    print("Deployment package created successfully!")
    print("\nTo deploy to your chosen platform:")
    print("1. For Render: Go to render.com and create a new Web Service")
    print("2. For Railway: Go to railway.app and create a new project")
    print("3. For self-hosting: Upload the deployment.zip file to your server")
    print("4. See ALTERNATIVE_DEPLOYMENT.md for detailed instructions")
    
    # Clean up the deployment package
    # os.remove(package_file)
    
    return True

def main():
    """Main deployment function"""
    print("Movie Wiki Scraper API Programmatic Deployment")
    print("=" * 50)
    
    try:
        if deploy_to_platform():
            print("\nDeployment package created successfully!")
            print("Follow the instructions above to complete deployment.")
            print("See ALTERNATIVE_DEPLOYMENT.md for detailed platform-specific instructions.")
            return True
        else:
            print("\nFailed to create deployment package!")
            return False
    except Exception as e:
        print(f"\nError during deployment: {e}")
        return False

if __name__ == "__main__":
    main()