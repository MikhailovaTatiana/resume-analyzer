import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState<{ score: number; missing_keywords: string[] } | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("keywords", jobDesc);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";
      const res = await axios.post(`${apiUrl}/analyze`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="app-container">
      <h1>Resume Analyzer</h1>
      <form onSubmit={handleSubmit} className="resume-form">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}
          accept=".pdf"
          className="file-input"
        />
        <textarea
          placeholder="Paste job description"
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          rows={5}
          className="job-description"
        />
        <button type="submit" className="submit-button">Analyze</button>
      </form>

      {result && (
        <div className="result-container">
          <h2>Score: {result.score}%</h2>
          <p>Missing Keywords: {result.missing_keywords.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
