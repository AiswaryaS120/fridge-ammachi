#!/usr/bin/env python3
"""
Startup script for Fridge Whisperer Ammachi
"""

import os
import sys
import subprocess
import uvicorn
from pathlib import Path
from dotenv import load_dotenv

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import ultralytics
        import google.generativeai
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has required variables"""
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  Warning: .env file not found")
        print("Please create a .env file with your GEMINI_API_KEY")
        print("Copy env_template.txt to .env and add your API key")
        print("Example:")
        print("GEMINI_API_KEY=your_api_key_here")
        return False
    
    # Check if GEMINI_API_KEY is set
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("⚠️  Warning: GEMINI_API_KEY not set in .env file")
        print("Please add your Google Gemini API key to the .env file")
        return False
    
    print("✅ Environment variables configured")
    return True

def main():
    """Main startup function"""
    print("🍳 Starting Fridge Whisperer Ammachi...")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment file
    check_env_file()
    
    # Start the server
    print("🚀 Starting server at http://localhost:8000")
    print("📱 Open your browser and visit: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the server")
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
