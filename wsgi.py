#!/usr/bin/env python3
"""
WSGI entrypoint for production deployment.
This file sets up the Flask app for WSGI servers like Gunicorn.
"""

import sys
import os

# Add the backend directory to Python path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)

# Change working directory to backend for relative imports and file paths
os.chdir(backend_path)

# Import the Flask app from backend
from app import app

# WSGI application object
application = app

if __name__ == "__main__":
    app.run()