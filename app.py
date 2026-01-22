#!/usr/bin/env python3
"""
Main application entrypoint for deployment platforms.
This file imports and runs the Flask app from the backend directory.
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

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)