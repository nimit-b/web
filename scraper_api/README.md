# Movie Wiki Scraper API

A Python web scraper API built with FastAPI that scrapes movie and TV show data from IMDb and other sources.

## ⚠️ Important Notice

Deta Space has shut down as of April 2025. Please see `ALTERNATIVE_DEPLOYMENT.md` for deployment options.

## 🚀 Deployment Options

### Option 1: Render (Recommended)
1. Go to [render.com](https://render.com) and sign up
2. Create a new Web Service
3. Connect your GitHub repository or upload the scraper_api folder
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Option 2: Railway
1. Go to [railway.app](https://railway.app) and sign up
2. Create a new project
3. Deploy from GitHub or upload your code
4. Railway will automatically detect it's a Python app

### Option 3: Self-Hosting
1. Get a VPS (DigitalOcean, Linode, AWS EC2, etc.)
2. Install Python 3.9+
3. Clone/upload your code
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn main:app --host 0.0.0.0 --port 80`

See `ALTERNATIVE_DEPLOYMENT.md` for detailed instructions for each platform.

## 📁 Project Structure

```
scraper_api/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python runtime version
├── deploy.py            # Automated deployment script
├── programmatic_deploy.py # Programmatic deployment script
├── ALTERNATIVE_DEPLOYMENT.md # Alternative deployment options
├── MANUAL_DEPLOYMENT.md # Manual deployment guide
├── DEPLOYMENT.md        # Complete deployment guide
└── README.md            # This file
```

## 🧪 Testing the API Locally

1. Start the API server:
   ```bash
   python -m uvicorn main:app --reload --port 8001
   ```

2. Test the endpoints:
   - `GET http://localhost:8001/` - Health check
   - `GET http://localhost:8001/scrape/imdb_top_picks` - Scrape IMDb's Top Picks
   - `GET http://localhost:8001/scrape/imdb_fan_favorites` - Scrape IMDb's Fan Favorites
   - `GET http://localhost:8001/scrape/imdb_popular` - Scrape IMDb's Popular section
   - `GET http://localhost:8001/scrape/latest` - Scrape latest movies

## 🌐 Testing the Deployed API

After deployment on your chosen platform, test the endpoints:

- `GET /` - Health check
- `GET /scrape/imdb_top_picks` - Scrape IMDb's Top Picks
- `GET /scrape/imdb_fan_favorites` - Scrape IMDb's Fan Favorites
- `GET /scrape/imdb_popular` - Scrape IMDb's Popular section
- `GET /scrape/latest` - Scrape latest movies

Example:
```
https://your-app.onrender.com/scrape/imdb_top_picks
```

## ⚠️ Important Notes

1. This is a template - the actual scraping logic needs to be implemented based on the current HTML structure of the target websites.
2. Web scraping should respect the target websites' terms of service and robots.txt.
3. Consider adding rate limiting and caching to avoid overwhelming target servers.
4. The current implementation returns sample data. To make it actually scrape IMDb, you would need to implement the HTML parsing logic based on IMDb's current structure.