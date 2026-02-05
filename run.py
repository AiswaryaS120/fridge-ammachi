#!/usr/bin/env python3
"""
Startup script for Fridge Whisperer Ammachi
"""
import sys
import uvicorn
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent


def check_dependencies():
    try:
        import fastapi
        import ultralytics
        import transformers
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False


def check_env_file():
    env_file = PROJECT_ROOT / ".env"
    if not env_file.exists():
        print("⚠️  Warning: .env file not found")
        print("Create a .env file with:")
        print("GEMINI_API_KEY=your_api_key_here")
        return False
    return True


def main():
    print("🍳 Starting Fridge Whisperer Ammachi...")

    # Ensure working directory is project root
    import os
    os.chdir(PROJECT_ROOT)

    if not check_dependencies():
        sys.exit(1)

    check_env_file()

    print("🚀 Server running at http://127.0.0.1:8000")
    print("🛑 Press Ctrl+C to stop")

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()
