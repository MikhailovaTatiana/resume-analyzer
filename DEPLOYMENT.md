# Deployment Guide - Resume Analyzer

## Prerequisites
- GitHub account
- Render account (free tier available)

## Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Ensure your repository is public** (required for Render free tier)

### **Note for Windows Users:**
- The `chmod` commands in the build scripts are for Unix/Linux systems
- Render will automatically make the scripts executable during deployment
- You don't need to run `chmod` commands on Windows

## Step 2: Deploy Backend API on Render

1. **Go to [Render Dashboard](https://dashboard.render.com/)**
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name:** `resume-analyzer-api`
   - **Root Directory:** `backend`
   - **Environment:** `Python 3`
   - **Build Command:** `chmod +x build.sh && ./build.sh`
   - **Start Command:** `chmod +x start.sh && ./start.sh`
   - **Plan:** Free

5. **Add Environment Variables:**
   - `PYTHON_VERSION`: `3.11.0`

6. **Click "Create Web Service"**

## Step 3: Deploy Frontend on Render

1. **Go to [Render Dashboard](https://dashboard.render.com/)**
2. **Click "New +" → "Static Site"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name:** `resume-analyzer-frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `dist`
   - **Plan:** Free

5. **Add Environment Variables:**
   - `VITE_API_URL`: `https://your-backend-service-name.onrender.com`

6. **Click "Create Static Site"**

## Step 4: Update CORS Settings (if needed)

If you encounter CORS issues, update the backend CORS settings in `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-service-name.onrender.com"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

## Step 5: Test Your Deployment

1. **Backend API:** Visit `https://your-backend-service-name.onrender.com/`
2. **Frontend:** Visit `https://your-frontend-service-name.onrender.com/`

## Troubleshooting

### Common Issues:

1. **Build fails:** Check the build logs in Render dashboard
2. **CORS errors:** Ensure the frontend URL is added to CORS origins
3. **Tesseract not found:** The build script should install it automatically
4. **Environment variables:** Double-check all environment variables are set correctly

### Local Testing:

Before deploying, test locally:
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Notes

- **Free tier limitations:** Services may sleep after inactivity
- **Cold starts:** First request after inactivity may be slow
- **File uploads:** Large files may timeout on free tier
- **OCR processing:** May be slower on Render's infrastructure
