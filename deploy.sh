#!/bin/bash

# Deployment script for Flask App

echo "Starting deployment..."

# Install dependencies
pip install -r requirements.txt

# Initialize database if it doesn't exist
if [ ! -f "instance/data.db" ]; then
    echo "Initializing database..."
    python initdb.py
fi

# Run with Gunicorn
echo "Starting application with Gunicorn..."
gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app
