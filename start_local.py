#!/usr/bin/env python3
"""
Local development startup script
Starts both backend and frontend servers
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def start_backend():
    """Start the backend server"""
    print("🚀 Starting backend server...")
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        return None
    
    try:
        # Check if .env exists
        env_file = backend_dir / ".env"
        if not env_file.exists():
            print("⚠️  Warning: .env file not found in backend directory")
            print("Please create backend/.env with your GEMINI_API_KEY")
            print("Copy from backend/env_template.txt")
        
        # Start backend
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            cwd=backend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Backend server started at http://localhost:8000")
        return process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_frontend():
    """Start the frontend server"""
    print("🌐 Starting frontend server...")
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found!")
        return None
    
    try:
        # Start frontend using Python's built-in server
        process = subprocess.Popen(
            [sys.executable, "-m", "http.server", "3000"],
            cwd=frontend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Frontend server started at http://localhost:3000")
        return process
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}")
        return None

def main():
    """Main function"""
    print("🍳 Starting Fridge Whisperer Ammachi locally...")
    print("=" * 50)
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Could not start backend. Exiting.")
        sys.exit(1)
    
    # Wait a moment for backend to start
    time.sleep(2)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Could not start frontend. Exiting.")
        backend_process.terminate()
        sys.exit(1)
    
    print("=" * 50)
    print("🎉 Both servers are running!")
    print("📱 Frontend: http://localhost:3000")
    print("🔧 Backend: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop both servers")
    
    # Open browser
    try:
        webbrowser.open("http://localhost:3000")
    except:
        pass
    
    try:
        # Keep running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Servers stopped")

if __name__ == "__main__":
    main()
