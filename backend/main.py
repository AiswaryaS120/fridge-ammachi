# backend/main.py
import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

# Import custom modules
import image_procc
import recipe_gen

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Fridge Recipe API", version="1.0.0")

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
        "https://*.vercel.app",  # Allow all Vercel subdomains
        "https://*.onrender.com"  # Allow Render subdomains
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Create upload directory
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
async def root():
    """Serve the frontend or API health check"""
    return FileResponse("../frontend/index.html")

@app.get("/api")
async def api_root():
    """API health check"""
    return {
        "message": "Fridge Whisperer API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {"status": "healthy"}

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    Process uploaded image and return detected items with recipes
    """
    print(f"\n--- Processing upload: {file.filename} ---")
    
    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    # Validate file size (max 10MB)
    file_size = 0
    content = await file.read()
    file_size = len(content)
    if file_size > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail="File size too large. Maximum 10MB allowed.")
    
    # Reset file position for processing
    await file.seek(0)
    
    temp_file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        # Save uploaded file
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"✅ File saved: {file.filename}")

        # Detect objects
        print("🔍 Detecting ingredients...")
        detected_items = image_procc.detect_objects(temp_file_path)
        print(f"📋 Found items: {detected_items}")
        
        if not detected_items:
            return {
                "success": False,
                "message": "No food items detected in the image. Try a clearer image with visible ingredients.",
                "detected_items": [],
                "recipes": ""
            }

        # Generate recipes
        print("👩‍🍳 Generating recipes...")
        recipes = recipe_gen.get_recipes(detected_items)
        print("✅ Recipes generated successfully")

        if "Error:" in recipes:
            return {
                "success": False,
                "message": "Could not generate recipes at this time.",
                "detected_items": detected_items,
                "recipes": recipes
            }
            
        return {
            "success": True,
            "detected_items": detected_items,
            "recipes": recipes
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    
    finally:
        # Cleanup
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"🗑️  Cleaned up: {file.filename}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))