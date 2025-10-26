# Run this script to start the scraper API locally for testing

if __name__ == "__main__":
    import uvicorn
    from main import app
    
    print("Starting Movie Wiki Scraper API locally...")
    print("Access the API at: http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)