# Urnix Flask App

This is a small Flask app configured for deployment on Vercel.

## Deploying to Vercel

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Log in to Vercel

```bash
vercel login
```

### 3. Deploy the project

From the project root:

```bash
cd c:/Users/ACER/OneDrive/Desktop/Urnix
vercel
```

Follow the prompts. Vercel will use `vercel.json` and `requirements.txt` to deploy the app.

## What is included

- `app.py` — your Flask app
- `api/index.py` — Vercel Python entrypoint
- `requirements.txt` — Flask dependency
- `vercel.json` — Vercel configuration

## Notes

- This deploys the app as a serverless Python function.
- Static files and templates are served by Flask.
