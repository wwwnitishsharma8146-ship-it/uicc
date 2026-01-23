#!/usr/bin/env python3
"""
Vercel serverless function that imports your original backend Flask app
"""

import sys
import os
from pathlib import Path

# Get the root directory and backend directory
root_dir = Path(__file__).parent.parent
backend_dir = root_dir / 'backend'

# Add backend directory to Python path
sys.path.insert(0, str(backend_dir))

# Change working directory to backend so your relative paths work
os.chdir(str(backend_dir))

# Import your original Flask app from backend/app.py
from app import app

# Export for Vercel
application = app

if __name__ == "__main__":
    app.run(debug=True)