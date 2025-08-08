# Fridge Whisperer Ammachi 🍳

A playful AI-powered recipe generator that uses computer vision to detect ingredients in your fridge and suggests personalized recipes. Features "Ammachi" (grandmother in Malayalam) as a friendly cooking assistant.

## Features

- 📸 **Image Upload**: Upload photos of your fridge contents
- 🔍 **Object Detection**: Uses YOLOv8 to identify food items
- 🤖 **AI Recipe Generation**: Google Gemini API generates personalized recipes
- 🎨 **Playful UI**: Ammachi character with Manglish (Malayalam-English) dialogue
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```bash
# Google Gemini API Key
# Get your API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Download YOLO Model

The YOLOv8 model will be automatically downloaded on first run, or you can manually download it:

```bash
# The model will be saved as yolov8n.pt
```

### 4. Run the Application

```bash
python main.py
```

The application will be available at `http://localhost:8000`

## Usage

1. **Home Page**: Visit the main page to see Ammachi
2. **Upload Image**: Click "Upload Fridge" to upload a photo of your fridge
3. **Detect Ingredients**: The AI will identify food items in your image
4. **Get Recipes**: Ammachi will suggest 3 personalized recipes using your ingredients

## Project Structure

```
fridge_ammachi/
├── main.py              # FastAPI application
├── image-pros.py        # YOLOv8 object detection
├── response.py          # Google Gemini API integration
├── requirements.txt     # Python dependencies
├── static/             # Frontend assets
│   ├── index.html      # Main landing page
│   ├── upload.html     # Image upload interface
│   ├── style.css       # Main styling
│   ├── upload-style.css # Upload page styling
│   └── ammachi image.jpg # Ammachi character image
└── yolov8n.pt          # YOLOv8 model file
```

## API Endpoints

- `GET /`: Serve the main application
- `POST /upload`: Upload and process fridge images
- `GET /health`: Health check endpoint

## Technical Stack

- **Backend**: FastAPI, Python
- **Computer Vision**: YOLOv8 (Ultralytics)
- **AI**: Google Gemini API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with pastel blue theme

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
2. **API Key Issues**: Verify your Gemini API key is correct
3. **Model Download**: Ensure internet connection for YOLO model download
4. **Image Upload**: Check file format (supports jpg, jpeg, png, gif, bmp, webp)

### Error Messages

- "No items detected": Try with a clearer image of your fridge
- "API Error": Check your Gemini API key and internet connection
- "File type error": Ensure you're uploading an image file

## Contributing

Feel free to contribute by:
- Adding new Ammachi dialogue lines
- Improving the UI/UX
- Enhancing recipe generation prompts
- Adding support for more image formats

## License

This project is open source and available under the MIT License.
