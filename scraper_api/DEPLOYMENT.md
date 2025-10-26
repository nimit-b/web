# Movie Wiki Scraper API Deployment Guide

⚠️ **Important Notice**: Deta Space has shut down as of April 2025. This guide has been updated with alternative deployment options.

This guide explains how to deploy the Movie Wiki Scraper API to alternative platforms.

## 📁 Project Structure

```
scraper_api/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── runtime.txt         # Python runtime version
├── README.md           # Documentation
└── deploy.py           # Deployment script
```

## 🚀 Deployment Steps

### Option 1: Render (Recommended)

1. **Sign up for Render**:
   Go to [render.com](https://render.com) and create an account.

2. **Create a new Web Service**:
   - Click "New+" and select "Web Service"
   - Connect your GitHub repository or upload the scraper_api folder

3. **Configure the service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     - `PYTHON_VERSION=3.9`
     - `PORT=8080`

### Option 2: Railway

1. **Sign up for Railway**:
   Go to [railway.app](https://railway.app) and create an account.

2. **Create a new project**:
   - Click "New Project"
   - Deploy from GitHub or upload your code

3. **Railway will automatically detect it's a Python app**

### Option 3: Automated Deployment

Run the deployment script:
```bash
python deploy.py
```

### Option 4: Programmatic Deployment

Run the programmatic deployment script:
```bash
python programmatic_deploy.py
```

This will create a `deployment.zip` file that you can upload to your chosen platform manually.

### Option 5: Manual Deployment

If the automated deployment doesn't work, follow the manual deployment guide in `MANUAL_DEPLOYMENT.md`.

## 🌐 Accessing Your Deployed API

After deployment, your platform will provide you with a public URL like:
```
https://movie-wiki-scraper-1234567890.onrender.com
```

You can test the API endpoints:
- `GET /` - Health check
- `GET /scrape/imdb_top_picks` - Scrape IMDb's Top Picks
- `GET /scrape/imdb_fan_favorites` - Scrape IMDb's Fan Favorites
- `GET /scrape/imdb_popular` - Scrape IMDb's Popular section
- `GET /scrape/latest` - Get latest movies

Example:
```
https://movie-wiki-scraper-1234567890.onrender.com/scrape/imdb_top_picks
```

## 🛠️ Integrating with the Frontend

To use this API with your JavaScript frontend:

1. Update the `SCRAPER_API_BASE` variable in your JavaScript code to point to your deployed URL
2. Replace the existing scraping functions with calls to this API
3. Handle CORS properly (already configured in the API)

## ⚠️ Important Notes

1. **Rate Limiting**: The API includes delays between requests to avoid overwhelming target servers
2. **User Agent**: A proper user agent is set to avoid being blocked
3. **Error Handling**: All endpoints include proper error handling
4. **CORS**: CORS is enabled to allow requests from your frontend
5. **Actual Scraping**: The current implementation returns sample data. To make it actually scrape IMDb, you would need to implement the HTML parsing logic based on IMDb's current structure.

## 🧪 Testing Locally

To test the API locally before deployment:

1. Start the API server:
   ```bash
   python -m uvicorn main:app --reload --port 8001
   ```

2. Test the endpoints:
   ```bash
   curl http://localhost:8001/
   curl http://localhost:8001/scrape/imdb_top_picks
   ```

## 📈 Monitoring

Most platforms provide built-in monitoring for your application. You can view logs and metrics in the platform's dashboard.