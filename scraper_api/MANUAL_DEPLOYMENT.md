# Manual Deployment Guide for Movie Wiki Scraper API

⚠️ **Important Notice**: Deta Space has shut down as of April 2025. This guide has been updated with alternative deployment options.

If the automated deployment script doesn't work, you can deploy the API manually using these steps.

## 📋 Prerequisites

1. Python 3.9 or higher
2. Internet connection
3. An account with your chosen deployment platform (Render, Railway, etc.)

## 🔧 Step-by-Step Manual Deployment

### Option 1: Render

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

### Option 3: Self-Hosting

1. **Get a VPS** (DigitalOcean, Linode, AWS EC2, etc.)
2. **Install Python 3.9+**
3. **Clone/upload your code**
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 80
   ```

## 🧪 Testing After Deployment

After deployment, your platform will provide you with a URL like:
```
https://your-project-name-123456.onrender.com
```

Test the API endpoints:

1. Health check: `GET https://your-project-name-123456.onrender.com/`
2. Scrape endpoint: `GET https://your-project-name-123456.onrender.com/scrape/imdb_top_picks`

## 🛠️ Troubleshooting

### If deployment fails:

1. Check your internet connection
2. Ensure all required files are present:
   - `main.py`
   - `requirements.txt`
   - `runtime.txt`

### Common Issues:

1. **Missing dependencies**: Make sure all dependencies are listed in `requirements.txt`
2. **Port configuration**: Ensure the PORT environment variable is set correctly
3. **Python version**: Make sure the platform supports Python 3.9+

## 📁 Required Files for Deployment

Make sure these files exist in the `scraper_api` directory:

```
scraper_api/
├── main.py              # FastAPI application
├── requirements.txt     # Dependencies
├── runtime.txt          # Python version
└── README.md            # Documentation
```

## 🔄 Integration with Frontend

After deployment, update your JavaScript frontend to use your deployed URL:

```javascript
// Replace this with your actual deployment URL
const SCRAPER_API_BASE = 'https://your-project-name-123456.onrender.com';

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

## 📈 Monitoring Your Deployment

1. Visit your platform's dashboard (Render, Railway, etc.)
2. Log in with your account
3. Find your deployed application
4. View logs, metrics, and manage your app

## 🆘 Need Help?

If you're still having issues:

1. Check the platform's documentation
2. Verify your Python installation
3. Ensure you have the latest version of pip: `python -m pip install --upgrade pip`
4. Check the logs for error messages