#!/usr/bin/env python3
"""
Deployment script for the Movie Wiki Scraper API to Deta Space
"""

import os
import subprocess
import sys
import shutil

def find_deta_executable():
    """Find the deta executable in PATH or Python scripts directory"""
    # Check if deta is in PATH
    deta_path = shutil.which('deta')
    if deta_path:
        return deta_path
    
    # Check in Python scripts directory
    python_scripts_dir = os.path.join(sys.prefix, 'Scripts')
    deta_path = os.path.join(python_scripts_dir, 'deta.exe')
    if os.path.exists(deta_path):
        return deta_path
    
    # Check in local packages
    local_scripts_dir = os.path.join(
        os.path.expanduser('~'), 
        'AppData', 
        'Local', 
        'Packages', 
        'PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0', 
        'LocalCache', 
        'local-packages', 
        'Python311', 
        'Scripts'
    )
    deta_path = os.path.join(local_scripts_dir, 'deta.exe')
    if os.path.exists(deta_path):
        return deta_path
    
    return None

def check_deta_installed():
    """Check if Deta CLI is installed"""
    try:
        deta_path = find_deta_executable()
        if deta_path:
            result = subprocess.run([deta_path, '--help'], capture_output=True, text=True)
            return result.returncode == 0
        return False
    except FileNotFoundError:
        return False

def install_deta():
    """Install Deta CLI"""
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'deta'], check=True)
        print("Deta CLI installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install Deta CLI")
        return False

def login_deta():
    """Login to Deta Space"""
    try:
        deta_path = find_deta_executable()
        if not deta_path:
            print("Deta CLI not found. Please install it manually.")
            print("Run: pip install deta")
            return False
        
        subprocess.run([deta_path, 'login'], check=True)
        print("Logged in to Deta Space successfully")
        return True
    except subprocess.CalledProcessError:
        print("Failed to login to Deta Space")
        return False
    except FileNotFoundError:
        print("Deta CLI not found. Please install it manually.")
        print("Run: pip install deta")
        return False

def deploy_to_deta():
    """Deploy the application to Deta Space"""
    try:
        # Change to the scraper_api directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        deta_path = find_deta_executable()
        if not deta_path:
            print("Deta CLI not found. Please install it manually.")
            return False
        
        # Initialize the project if it doesn't exist
        print("Initializing Deta project...")
        subprocess.run([deta_path, 'new'], check=True)
        
        # Deploy the project
        print("Deploying to Deta Space...")
        subprocess.run([deta_path, 'deploy'], check=True)
        
        print("Deployment completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e}")
        return False
    except FileNotFoundError:
        print("Deta CLI not found. Please install it manually.")
        print("Run: pip install deta")
        return False

def main():
    """Main deployment function"""
    print("Movie Wiki Scraper API Deployment Script")
    print("=" * 40)
    
    # Check if Deta CLI is installed
    if not check_deta_installed():
        print("Deta CLI not found. Installing...")
        if not install_deta():
            print("\nPlease install Deta CLI manually:")
            print("Run: pip install deta")
            return False
    
    # Login to Deta Space
    print("Please login to Deta Space:")
    if not login_deta():
        print("\nPlease login manually:")
        deta_path = find_deta_executable()
        if deta_path:
            print(f"Run: {deta_path} login")
        else:
            print("Run: deta login (after installing)")
        return False
    
    # Deploy the application
    print("Deploying the Movie Wiki Scraper API...")
    if deploy_to_deta():
        print("\nDeployment successful!")
        print("Your API is now available on Deta Space.")
        return True
    else:
        print("\nDeployment failed!")
        print("\nPlease try manual deployment:")
        print("1. Navigate to the scraper_api directory")
        print("2. Run: deta new")
        print("3. Run: deta deploy")
        return False

if __name__ == "__main__":
    main()