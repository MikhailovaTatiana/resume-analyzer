# Resume Analyzer Backend

A FastAPI-based backend service for analyzing resumes and matching them against job descriptions or keywords.

## Features

- PDF text extraction with OCR fallback for scanned documents
- Keyword matching and similarity scoring
- RESTful API endpoints
- CORS support for frontend integration

## Prerequisites

- Python 3.8 or higher
- Tesseract OCR (for PDF text extraction)

### Installing Tesseract OCR

**Windows:**
```bash
winget install UB-Mannheim.TesseractOCR
```

**macOS:**
```bash
brew install tesseract
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

## Installation

1. **Create virtual environment:**
   ```bash
   python -m venv resume-venv
   ```

2. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   resume-venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source resume-venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

1. **Activate the virtual environment** (if not already activated)
2. **Start the server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API:**
   - API will be available at: http://localhost:8000
   - API documentation: http://localhost:8000/docs

## API Endpoints

- `GET /` - Health check
- `POST /analyze` - Analyze resume with keywords

### Example usage:

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@resume.pdf" \
  -F "keywords=python,fastapi,machine learning"
```

## Dependencies

- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **pdfplumber**: PDF text extraction
- **pytesseract**: OCR for PDF images
- **Pillow**: Image processing
- **python-multipart**: File upload handling

## Troubleshooting

### Common Issues:

1. **Tesseract not found:**
   - Ensure Tesseract is installed and in PATH
   - On Windows, restart terminal after installation

2. **Port already in use:**
   - Change port: `uvicorn main:app --reload --port 8001`

3. **Memory issues:**
   - Large PDFs may require more memory
   - Consider processing files in chunks

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## License

This project is for educational purposes.
