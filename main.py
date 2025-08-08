# main.py
# The core FastAPI application with added print statements for debugging.

import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Import our custom modules
import image_procc
import recipe_gen

# Create the FastAPI app instance
app = FastAPI(title="Fridge Recipe Suggester")

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Static Files ---
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create a directory for temporary uploads
UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# --- API Endpoints ---

@app.get("/", include_in_schema=False)
async def root():
    """
    Serves the main index.html file from the static directory.
    """
    return FileResponse("static/index.html")

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    This endpoint accepts an image file, processes it to detect items,
    generates recipes, and returns the results.
    """
    print("\n--- Received new upload request ---")
    temp_file_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        # Save the uploaded file
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"[1/4] File '{file.filename}' saved successfully.")

        # --- Step 1: Detect objects in the image ---
        print("[2/4] Calling image_procc.detect_objects...")
        detected_items = image_procc.detect_objects(temp_file_path)
        print(f"-> Detection complete. Found: {detected_items}")
        
        if not detected_items:
            raise HTTPException(status_code=400, detail="Could not detect any items in the image.")

        # --- Step 2: Generate recipes based on detected items ---
        print("[3/4] Calling recipe_gen.get_recipes...")
        recipes = recipe_gen.get_recipes(detected_items)
        print("-> Recipe generation complete.")

        if "Error:" in recipes:
            # This handles errors returned from our recipe_gen function
            raise HTTPException(status_code=500, detail=recipes)
            
        # --- Step 3: Return the successful response ---
        print("[4/4] Sending successful response to frontend.")
        return {
            "detected_items": detected_items,
            "recipes": recipes
        }

    except HTTPException as e:
        # Re-raise known HTTP exceptions
        print(f"ERROR: A known HTTP error occurred: {e.detail}")
        raise e
    except Exception as e:
        # Catch any other unexpected errors
        print(f"FATAL ERROR: An unexpected error occurred in the /upload endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"An internal server error occurred: {str(e)}")
    finally:
        # --- Cleanup: Remove the temporary file ---
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"-> Temporary file '{file.filename}' deleted.")

