# Alternative Deployment Options for Movie Wiki Scraper API

Since Deta Space has shut down, here are alternative platforms where you can deploy the Movie Wiki Scraper API.

## 🚀 Deployment Options

### 1. Render (Recommended)

Render is a great alternative to Deta Space with a free tier.

#### Steps:
1. Go to [render.com](https://render.com) and sign up
2. Create a new Web Service
3. Connect your GitHub repository (or upload the scraper_api folder)
4. Set the following configuration:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     - `PYTHON_VERSION=3.9`
     - `PORT=8080`

#### Free Tier:
- 500 hours/month of free usage
- Sleeps after 15 minutes of inactivity

### 2. Railway

Railway is another excellent platform with a generous free tier.

#### Steps:
1. Go to [railway.app](https://railway.app) and sign up
2. Create a new project
3. Deploy from GitHub or upload your code
4. Railway will automatically detect it's a Python app
5. Add environment variables if needed

#### Free Tier:
- $5 credit/month
- Sleeps after 12 hours of inactivity

### 3. Heroku

Heroku is a well-established platform (though free tier has limitations).

#### Steps:
1. Install Heroku CLI
2. Create a `Procfile` with:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
3. Create a `runtime.txt` with:
   ```
   python-3.9.18
   ```
4. Deploy using:
   ```bash
   heroku create
   git push heroku main
   ```

#### Free Tier:
- Sleeps after 30 minutes of inactivity
- Limited to 550-1000 hours/month

### 4. PythonAnywhere

PythonAnywhere offers free hosting for Python applications.

#### Steps:
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Create a new web app
3. Upload your files
4. Configure the WSGI file

#### Free Tier:
- Limited to one web app
- No HTTPS for custom domains

### 5. Vercel (with Python functions)

Vercel now supports Python serverless functions.

#### Steps:
1. Create an `api/` directory
2. Move your FastAPI app to work as serverless functions
3. Deploy to Vercel

#### Free Tier:
- Generous free tier
- Functions sleep after inactivity

### 6. Self-Hosting (Local/Cloud VPS)

You can run the API on your own server or a VPS.

#### Steps:
1. Get a VPS (DigitalOcean, Linode, AWS EC2, etc.)
2. Install Python 3.9+
3. Clone/upload your code
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 80
   ```

## 🛠️ Required Files for Any Deployment

Make sure these files are included:

```
scraper_api/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version (if needed)
├── Procfile             # For Heroku
├── README.md            # Documentation
└── .env                 # Environment variables (if any)
```

## 🌐 Environment Variables

Most platforms support environment variables. For this API, you might want to set:

```
PORT=8080
PYTHON_VERSION=3.9
```

## 🧪 Testing Your Deployed API

After deployment, test the endpoints:

- `GET /` - Health check
- `GET /scrape/imdb_top_picks` - Scrape IMDb's Top Picks
- `GET /scrape/imdb_fan_favorites` - Scrape IMDb's Fan Favorites
- `GET /scrape/imdb_popular` - Scrape IMDb's Popular section
- `GET /scrape/latest` - Scrape latest movies

## 🔄 Integration with Frontend

Update your JavaScript frontend to use the new API URL:

```javascript
// Replace with your actual deployment URL
const SCRAPER_API_BASE = 'https://your-app.onrender.com'; // or whatever platform you use

// Example function to fetch popular movies
async function fetchPopularMovies() {
    try {
        const response = await fetch(`${SCRAPER_API_BASE}/scrape/imdb_top_picks`);
        const data = await response.json();
        return data.items;
    } catch (error) {
        console.error('Error fetching popular movies:', error);
        return [];
    }
}
```

## ⚠️ Important Notes

1. **Rate Limiting**: The API includes delays between requests to avoid overwhelming target servers
2. **User Agent**: A proper user agent is set to avoid being blocked
3. **Error Handling**: All endpoints include proper error handling
4. **CORS**: CORS is enabled to allow requests from your frontend
5. **Actual Scraping**: The current implementation returns sample data. To make it actually scrape IMDb, you would need to implement the HTML parsing logic based on IMDb's current structure.

## 📈 Monitoring

Most platforms provide built-in monitoring:
- Render: Dashboard with logs and metrics
- Railway: Real-time logs and performance metrics
- Heroku: Logs and performance monitoring
- Self-hosted: You can add monitoring tools like Prometheus

## 🆘 Need Help?

If you're having issues with deployment:

1. Check the platform's documentation
2. Verify all required files are present
3. Ensure environment variables are set correctly
4. Check logs for error messages