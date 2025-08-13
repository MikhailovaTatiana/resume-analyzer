#!/usr/bin/env bash
# exit on error
set -o errexit

# Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port $PORT
