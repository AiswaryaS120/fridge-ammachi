# Fridge Whisperer Ammachi 🍳

A fun recipe recommendation app that detects ingredients from fridge photos and suggests recipes using AI.

## Features

- 📸 Upload fridge photos to detect ingredients
- 🤖 AI-powered recipe suggestions using Google Gemini
- 🎭 Interactive Ammachi character with different moods
- 🎨 Beautiful animated UI with falling vegetables
- 🌐 Full-stack web application

## Local Development Setup

### Prerequisites

- Python 3.8+
- Node.js (optional, for local frontend serving)
- Google Gemini API key

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Copy the template
   cp env_template.txt .env
   
   # Edit .env and add your Gemini API key
   # Get your API key from: https://makersuite.google.com/app/apikey
   ```

4. **Run the backend server:**
   ```bash
   python run.py
   # or
   python main.py
   ```

   The backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Serve the frontend (choose one):**
   
   **Option A: Using Python (simple)**
   ```bash
   python -m http.server 3000
   ```
   
   **Option B: Using Node.js**
   ```bash
   npx serve .
   ```
   
   **Option C: Using Live Server (VS Code extension)**
   - Install Live Server extension
   - Right-click on `index.html` and select "Open with Live Server"

3. **Access the app:**
   - Frontend: `http://localhost:3000` (or the port shown)
   - Backend API: `http://localhost:8000`

## Deployment

### Frontend Deployment (Vercel)

1. **Push your code to GitHub**

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Set the root directory to `frontend`
   - Deploy

3. **Update API URL:**
   - After deployment, update the API URL in `frontend/index.html`
   - Replace `https://your-render-backend-url.onrender.com` with your actual Render backend URL

### Backend Deployment (Render)

1. **Push your code to GitHub**

2. **Create a new Web Service on Render:**
   - Go to [render.com](https://render.com)
   - Connect your GitHub repository
   - Set the following:
     - **Name:** `fridge-whisperer-backend`
     - **Root Directory:** `backend`
     - **Runtime:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Add Environment Variables:**
   - `GEMINI_API_KEY`: Your Google Gemini API key

4. **Deploy**

### Update Frontend with Backend URL

After deploying the backend, update the frontend:

1. **Get your Render backend URL** (e.g., `https://fridge-whisperer-backend.onrender.com`)

2. **Update the API URL in `frontend/index.html`:**
   ```javascript
   const apiUrl = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
     ? 'http://localhost:8000/api/upload'
     : 'https://your-actual-render-url.onrender.com/api/upload';
   ```

3. **Redeploy the frontend on Vercel**

## API Endpoints

- `GET /` - Serve frontend
- `GET /api` - API health check
- `GET /health` - Health check for Render
- `POST /api/upload` - Upload and process images

## Environment Variables

- `GEMINI_API_KEY` - Google Gemini API key (required)
- `PORT` - Server port (optional, defaults to 8000)

## Troubleshooting

### Common Issues

1. **"No module named 'ultralytics'"**
   - Run: `pip install -r requirements.txt`

2. **"GEMINI_API_KEY not found"**
   - Create `.env` file in backend directory
   - Add your API key: `GEMINI_API_KEY=your_key_here`

3. **CORS errors**
   - Check that your frontend URL is in the CORS allow_origins list
   - Update the API URL in frontend to match your backend URL

4. **Image upload fails**
   - Check file size (max 10MB)
   - Ensure file is an image format

### Local Development Tips

- Use `python run.py` for better error checking
- Check console logs for detailed error messages
- Test API endpoints using tools like Postman or curl

## Tech Stack

- **Backend:** FastAPI, Python, YOLOv8, Google Gemini AI
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Vercel (frontend), Render (backend)

## License

MIT License
