#!/usr/bin/env python3
"""
Setup script for Resume Analyzer Backend
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def main():
    print("Setting up Resume Analyzer Backend...")
    
    # Check if Python is installed
    python_version = run_command("python --version")
    if python_version:
        print(f"Python version: {python_version.strip()}")
    else:
        print("Error: Python is not installed or not in PATH")
        sys.exit(1)
    
    # Check if pip is installed
    pip_version = run_command("pip --version")
    if pip_version:
        print(f"Pip version: {pip_version.strip()}")
    else:
        print("Error: Pip is not installed or not in PATH")
        sys.exit(1)
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists("resume-venv"):
        print("Creating virtual environment...")
        result = run_command("python -m venv resume-venv")
        if result is None:
            print("Error: Failed to create virtual environment")
            sys.exit(1)
        print("Virtual environment created successfully!")
    else:
        print("Virtual environment already exists.")
    
    # Activate virtual environment and install dependencies
    print("Installing dependencies...")
    
    # Determine the activation script based on OS
    if os.name == 'nt':  # Windows
        activate_script = "resume-venv\\Scripts\\activate"
        pip_path = "resume-venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_script = "resume-venv/bin/activate"
        pip_path = "resume-venv/bin/pip"
    
    # Install requirements
    install_result = run_command(f"{pip_path} install -r requirements.txt")
    if install_result:
        print("Dependencies installed successfully!")
        print("\nSetup completed! To run the backend:")
        print("1. Activate the virtual environment:")
        if os.name == 'nt':
            print("   resume-venv\\Scripts\\activate")
        else:
            print("   source resume-venv/bin/activate")
        print("2. Run the server:")
        print("   uvicorn main:app --reload")
    else:
        print("Error: Failed to install dependencies")
        sys.exit(1)

if __name__ == "__main__":
    main()
