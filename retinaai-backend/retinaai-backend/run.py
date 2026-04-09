import subprocess
import sys
import os

def check_and_install_dependencies():
    print("Checking dependencies...")
    try:
        import pymysql
        import uvicorn
        import sqlmodel
        print("Dependencies already installed.")
    except ImportError:
        print("Installing missing dependencies from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_server():
    import uvicorn
    # Make sure we're in the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Starting RetinaAI Backend...")
    print("Database: MySQL (Localhost, Port 3306)")
    print("Host: 0.0.0.0, Port: 8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    check_and_install_dependencies()
    run_server()
