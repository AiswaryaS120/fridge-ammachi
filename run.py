#!/usr/bin/env python3
"""
Startup script for Fridge Whisperer Ammachi
"""

import os
import sys
import subprocess
import uvicorn
from pathlib import Path

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
    """Check if .env file exists"""
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  Warning: .env file not found")
        print("Please create a .env file with your GEMINI_API_KEY")
        print("Example:")
        print("GEMINI_API_KEY=your_api_key_here")
        return False
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
