import os
import shutil
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import image_procc
import recipe_gen

app = FastAPI(title="Fridge Whisperer Ammachi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("static/index.html")


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    temp_path = os.path.join(UPLOAD_DIR, file.filename)

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        items = image_procc.detect_objects(temp_path)

        if not items:
            raise HTTPException(status_code=400, detail="No items detected")

        recipes = recipe_gen.get_recipes(items)

        if recipes.startswith("Error"):
            raise HTTPException(status_code=500, detail=recipes)

        return {
            "detected_items": items,
            "recipes": recipes
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
