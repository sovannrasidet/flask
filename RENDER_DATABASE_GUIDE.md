# Render Database Setup Guide

## Quick Setup for PostgreSQL (Recommended)

### Step 1: Create PostgreSQL Database
1. Go to Render dashboard
2. Click "New +" → "PostgreSQL"
3. Choose a name (e.g., "flask-login-db")
4. Select free tier
5. Click "Create Database"

### Step 2: Get Database URL
1. Go to your database service
2. Click "Connect" tab
3. Copy the "External Database URL"
4. It looks like: `postgresql://user:password@host:port/dbname`

### Step 3: Update Your Web Service
1. Go to your Flask web service
2. Click "Environment" tab
3. Add environment variable:
   - **Key**: `DATABASE_URL`
   - **Value**: (paste the PostgreSQL URL from step 2)

### Step 4: Redeploy
1. Push updated code to GitHub
2. Render will automatically redeploy
3. Your app will now use PostgreSQL

### Step 5: Initialize Database
The first deployment will create tables automatically. To add your test user:
1. Go to Render dashboard → your service → "Shell"
2. Run: `python initdb.py`

## Alternative: Disk Storage (Keep SQLite)

If you prefer to keep SQLite:

1. Go to your web service settings
2. Click "Advanced" → "Add Disk"
3. Mount path: `/app/instance`
4. Size: 1GB (free tier)
5. Redeploy

## Important Notes

- **PostgreSQL** is more reliable for production
- **SQLite** with disk storage is simpler but less robust
- Your current data will be lost when switching databases
- Test users need to be recreated after database changes

## Environment Variables for Production

Add these to your Render service:
- `SECRET_KEY` (generate: `python -c 'import secrets; print(secrets.token_hex(32))'`)
- `DATABASE_URL` (PostgreSQL URL)
- `FLASK_ENV=production`
