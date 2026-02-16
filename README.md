# Bracket Matrix - Live NCAA Tournament Bracket Tracker

A fully functional, modern web application that displays NCAA tournament bracket predictions from multiple experts.

## 🚀 Features

- **Live Data Updates**: Scrapes and displays the latest bracket predictions
- **Interactive Interface**: Sort, filter, and search through teams
- **Consensus Analysis**: See where experts agree/disagree on seeding
- **Detailed Team Views**: Click any team to see all expert predictions
- **Responsive Design**: Works beautifully on desktop and mobile
- **REST API**: Full backend API for data access

## 📁 Project Structure

```
bracket-matrix-app/
├── backend/
│   ├── api.py              # Flask REST API server
│   ├── scraper.py          # Data scraper for BracketMatrix.com
│   ├── bracket_data.json   # Current bracket data
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # React frontend application
└── README.md
```

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Modern web browser

### Backend Setup

1. **Install Python dependencies**:
```bash
cd backend
pip install -r requirements.txt
```

2. **Start the API server**:
```bash
python api.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

Simply open `frontend/index.html` in a web browser, or serve it with a local server:

```bash
cd frontend
python -m http.server 8000
```

Then visit `http://localhost:8000`

## 🔄 Updating Data

### Option 1: Manual Scraping (When Network Available)

Run the scraper to fetch the latest data from BracketMatrix.com:

```bash
cd backend
python scraper.py
```

This will:
- Fetch the latest bracket predictions
- Parse all team and expert data
- Save to `bracket_data.json`
- The API will automatically serve the updated data

### Option 2: Manual Data Updates

If you can't run the scraper, you can manually update `backend/bracket_data.json`:

1. Visit http://www.bracketmatrix.com/
2. Copy the data you want
3. Update the JSON file following this structure:

```json
{
  "last_updated": "2026-02-15T00:00:00",
  "bracketologists": [
    {"name": "ESPN", "url": "..."}
  ],
  "teams": [
    {
      "seed": "1",
      "team": "Michigan",
      "conference": "Big Ten",
      "average_seed": "1.00",
      "num_brackets": "112",
      "predictions": ["1", "1", "1"]
    }
  ]
}
```

### Option 3: Automated Updates (Production)

Set up a cron job to run the scraper automatically:

```bash
# Edit crontab
crontab -e

# Add this line to update every hour
0 * * * * cd /path/to/bracket-matrix-app/backend && python scraper.py
```

## 🌐 API Endpoints

The backend provides these REST API endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/brackets` | GET | Get all bracket data |
| `/api/teams` | GET | Get just team data |
| `/api/bracketologists` | GET | Get expert information |
| `/api/team/<name>` | GET | Get specific team data |
| `/api/update` | POST | Trigger data refresh |
| `/health` | GET | Health check |

### Example API Calls

```bash
# Get all data
curl http://localhost:5000/api/brackets

# Get teams only
curl http://localhost:5000/api/teams

# Get specific team
curl http://localhost:5000/api/team/Michigan

# Trigger update
curl -X POST http://localhost:5000/api/update
```

## 🎨 Frontend Features

### Search & Filter
- **Search**: Type team names to find specific teams
- **Conference Filter**: View teams from specific conferences
- **Sort Options**: Sort by seed, team name, or conference

### Team Details
- Click any team row to see detailed predictions
- View all expert picks for that team
- See consensus level (high/medium/low agreement)

### Visual Indicators
- **Seed Colors**: Different colors for 1-seeds, 2-seeds, etc.
- **Consensus Badges**: Green (high agreement), Orange (medium), Red (low)
- **Interactive Hover**: Rows highlight on hover

## 🚀 Deployment

### Deploy to Production

1. **Backend**: Deploy the Flask API to any Python hosting service:
   - Heroku
   - AWS Elastic Beanstalk
   - Google Cloud Run
   - DigitalOcean App Platform

2. **Frontend**: Deploy the HTML to any static hosting:
   - Netlify
   - Vercel
   - GitHub Pages
   - AWS S3 + CloudFront

3. **Update API URL**: In `frontend/index.html`, change:
```javascript
const API_URL = 'https://your-api-domain.com/api';
```

## 📊 Data Format

The application expects data in this format:

```json
{
  "last_updated": "ISO 8601 date string",
  "source_url": "http://www.bracketmatrix.com/",
  "bracketologists": [
    {
      "name": "Expert name",
      "url": "Expert's bracket URL (optional)"
    }
  ],
  "update_dates": ["2/13", "2/13", ...],
  "teams": [
    {
      "seed": "1",
      "team": "Team Name",
      "conference": "Conference Name",
      "average_seed": "1.00",
      "num_brackets": "112",
      "predictions": ["1", "1", "2", null, ...]
    }
  ]
}
```

## 🔧 Customization

### Adding More Bracketologists

The scraper automatically picks up all experts from BracketMatrix.com. To manually add:

1. Edit `bracket_data.json`
2. Add to `bracketologists` array
3. Add corresponding predictions to each team's `predictions` array

### Styling

The frontend uses Tailwind CSS. To customize:

1. Edit the `<style>` section in `index.html`
2. Modify Tailwind classes in the React components
3. Change color schemes, fonts, spacing, etc.

## 📝 Notes

- The scraper respects BracketMatrix.com's data structure
- Data updates typically every few hours during the season
- The app works entirely with the static data file (no database needed)
- All frontend code is client-side (React in browser)

## 🐛 Troubleshooting

**API not connecting**:
- Ensure Flask server is running on port 5000
- Check CORS settings in `api.py`
- Update `API_URL` in frontend if using different port

**Scraper failing**:
- Check network connectivity
- Verify BracketMatrix.com is accessible
- Site structure may have changed (update scraper selectors)

**No data showing**:
- Verify `bracket_data.json` exists and is valid JSON
- Check browser console for errors
- Ensure API is returning data (test endpoints directly)

## 📄 License

This is a personal project for educational purposes. Please respect BracketMatrix.com's terms of service when scraping data.

## 🙏 Credits

- Data source: [BracketMatrix.com](http://www.bracketmatrix.com/)
- Built with React, Flask, Python, and Tailwind CSS
