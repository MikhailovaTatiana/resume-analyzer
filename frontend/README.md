# Resume Analyzer Frontend

A React + TypeScript frontend application for the Resume Analyzer project. This application provides a user-friendly interface for uploading resumes and analyzing them against job descriptions.

## Features

- Modern React 19 with TypeScript
- File upload for PDF resumes
- Job description input
- Real-time analysis results
- Responsive design
- Built with Vite for fast development

## Prerequisites

- Node.js 18 or higher
- npm or yarn package manager

## Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and set your backend API URL:
   ```
   VITE_API_URL=http://localhost:8000
   ```

## Development

1. **Start the development server:**
   ```bash
   npm run dev
   ```

2. **Open your browser:**
   - The app will be available at: http://localhost:5173

3. **Make sure the backend is running:**
   - Backend should be running on http://localhost:8000

## Building for Production

1. **Build the application:**
   ```bash
   npm run build
   ```

2. **Preview the production build:**
   ```bash
   npm run preview
   ```

## Project Structure

```
src/
├── App.tsx          # Main application component
├── App.css          # Application styles
├── main.tsx         # Application entry point
└── index.css        # Global styles
```

## Technologies Used

- **React 19**: UI library
- **TypeScript**: Type safety
- **Vite**: Build tool and dev server
- **Axios**: HTTP client for API calls
- **CSS**: Styling

## API Integration

The frontend communicates with the backend API for:
- File upload and analysis
- Keyword matching
- Score calculation

## Environment Variables

- `VITE_API_URL`: Backend API URL (default: http://localhost:8000)

## Scripts

- `npm run dev`: Start development server
- `npm run build`: Build for production
- `npm run preview`: Preview production build
- `npm run lint`: Run ESLint

## Troubleshooting

### Common Issues:

1. **Backend connection failed:**
   - Ensure the backend server is running
   - Check the `VITE_API_URL` environment variable

2. **File upload issues:**
   - Ensure the file is a valid PDF
   - Check file size limits

3. **Build errors:**
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`

## License

This project is for educational purposes.
