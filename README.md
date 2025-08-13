# Resume Analyzer

A modern web application that analyzes resumes against job descriptions to provide keyword matching scores and identify missing skills. Built with React, TypeScript, and FastAPI.

![Resume Analyzer](https://img.shields.io/badge/React-19-blue?style=for-the-badge&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.8-blue?style=for-the-badge&logo=typescript)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)

## 🚀 Features

- **PDF Resume Upload**: Upload and analyze PDF resumes
- **OCR Support**: Extract text from scanned documents using Tesseract OCR
- **Keyword Matching**: Compare resume content against job descriptions
- **Score Calculation**: Get percentage match scores
- **Missing Skills**: Identify skills that are missing from your resume
- **Modern UI**: Clean, responsive interface built with React
- **Real-time Analysis**: Instant results with detailed feedback

## 🎯 How It Works

1. **Upload Resume**: Users upload their resume in PDF format
2. **Input Job Description**: Paste the job description or list specific keywords
3. **Text Extraction**: The system extracts text from the PDF (with OCR fallback for scanned documents)
4. **Analysis**: Compares resume content against the provided keywords
5. **Results**: Returns a match score and lists missing keywords

## 📁 Project Structure

```
resume-analyzer/
├── backend/                 # FastAPI backend service
│   ├── main.py             # API endpoints and logic
│   ├── ml_utils.py         # Keyword matching algorithms
│   ├── requirements.txt    # Python dependencies
│   ├── build.sh           # Deployment build script
│   └── start.sh           # Deployment start script
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── App.tsx        # Main application component
│   │   ├── App.css        # Application styles
│   │   └── main.tsx       # Application entry point
│   ├── package.json       # Node.js dependencies
│   └── env.example        # Environment variables template
├── render.yaml            # Render deployment configuration
└── DEPLOYMENT.md          # Detailed deployment guide
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **pdfplumber**: PDF text extraction
- **pytesseract**: OCR for scanned documents
- **Pillow**: Image processing

### Frontend
- **React 19**: UI library with latest features
- **TypeScript**: Type safety and better development experience
- **Vite**: Fast build tool and development server
- **Axios**: HTTP client for API communication

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** and **Node.js 18+**
- **Tesseract OCR** (for PDF text extraction)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd resume-analyzer
   ```

2. **Set up the backend:**
   ```bash
   cd backend
   python -m venv resume-venv
   
   # Activate virtual environment
   # Windows:
   resume-venv\Scripts\activate
   # macOS/Linux:
   source resume-venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Set up the frontend:**
   ```bash
   cd ../frontend
   npm install
   cp env.example .env
   ```

4. **Install Tesseract OCR:**
   
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

### Running the Application

1. **Start the backend server:**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at: http://localhost:8000

2. **Start the frontend development server:**
   ```bash
   cd frontend
   npm run dev
   ```
   The app will be available at: http://localhost:5173

3. **Open your browser** and navigate to http://localhost:5173

## 📖 Usage

1. **Upload Resume**: Click "Choose File" and select your PDF resume
2. **Add Job Description**: Paste the job description or list keywords separated by commas
3. **Analyze**: Click "Analyze" to process your resume
4. **Review Results**: View your match score and missing keywords

### Example Job Description Keywords:
```
python, fastapi, react, typescript, machine learning, docker, aws, sql, git, agile
```

## 🌐 API Endpoints

- `GET /` - Health check
- `POST /analyze` - Analyze resume with keywords

### API Response Format:
```json
{
  "score": 75.5,
  "missing_keywords": ["docker", "aws", "kubernetes"]
}
```

## 🚀 Deployment

This application is designed to be deployed on Render. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Live Demo
🌐 **Try it out:** [The Render App Link Here](https://resume-analyzer-frontend-c04f.onrender.com)

### Quick Deployment Steps:
1. Push your code to GitHub
2. Connect your repository to Render
3. Deploy both backend and frontend services
4. Configure environment variables

## 🔧 Configuration

### Environment Variables

**Frontend (.env):**
```
VITE_API_URL=http://localhost:8000
```

**Backend:**
- `PORT`: Server port (set automatically by Render)
- `PYTHON_VERSION`: Python version (3.11.0)

## 🐛 Troubleshooting

### Common Issues:

1. **Tesseract not found:**
   - Ensure Tesseract is installed and in PATH
   - Restart terminal after installation

2. **Backend connection failed:**
   - Check if backend server is running
   - Verify `VITE_API_URL` in frontend .env file

3. **File upload issues:**
   - Ensure file is a valid PDF
   - Check file size limits

4. **Build errors:**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Python dependencies: `pip install -r requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [React](https://react.dev/) for the frontend library
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text extraction
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF processing

---

**Made with ❤️ for better resume analysis**
