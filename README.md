# UIC Patent Portal

A comprehensive patent application management system for Chandigarh University's Innovation Cell.

**Status**: Production Ready ✅ | **Last Updated**: January 19, 2026

## Project Structure

```
patent-portal/
├── backend/                 # Flask backend application
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── database.db         # SQLite database
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Main application form
│   │   ├── login.html      # Login page
│   │   └── signup.html     # Registration page
│   ├── static/             # Static assets
│   │   ├── css/            # Stylesheets
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Image assets
│   └── uploads/            # File upload directory
├── scripts/                # Setup and utility scripts
├── tests/                  # Test files and debugging tools
├── docs/                   # Documentation files
├── Procfile               # Render deployment config
├── render.yaml            # Render service config
├── requirements.txt       # Root dependencies for deployment
└── README.md              # This file
```

## Features

- ✅ User authentication (login/signup)
- ✅ Patent application submission
- ✅ Team member management
- ✅ File upload support
- ✅ Google Drive integration
- ✅ Google Sheets synchronization
- ✅ Application status tracking

## Quick Start

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to: `http://localhost:5000`

## Deployment

This project is configured for deployment on Render.com:

1. Push to GitHub
2. Connect your GitHub repo to Render
3. Render will automatically deploy using the configuration files

## Google Integrations

- **Google Drive**: Automatic file upload for patent documents
- **Google Sheets**: Real-time data synchronization for applications

## Development

The application is built with:
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Integrations**: Google Apps Script, Google Drive API
