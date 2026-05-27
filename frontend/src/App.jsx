import { useState } from "react";
import axios from "axios";
import "./style.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResume = async () => {
    if (!resume || !jobDescription) {
      alert("Please upload resume and enter job description");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8001/analyze",
        formData
      );

      setResult(response.data);
    } catch (error) {
      alert("Error analyzing resume");
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Resume Analyzer + ATS Score Checker</h1>
      <p className="subtitle">
        Upload your resume and compare it with a job description.
      </p>

      <div className="card">
        <label>Upload Resume PDF</label>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setResume(e.target.files[0])}
        />

        <label>Paste Job Description</label>
        <textarea
          placeholder="Paste job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button onClick={analyzeResume}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </div>

      {result && (
        <div className="result">
          <h2>ATS Score: {result.ats_score}%</h2>

          <h3>Extracted Skills</h3>
          <div className="tags">
            {result.skills.map((skill, index) => (
              <span key={index}>{skill}</span>
            ))}
          </div>

          <h3>Missing Keywords</h3>
          <div className="tags missing">
            {result.missing_keywords.map((word, index) => (
              <span key={index}>{word}</span>
            ))}
          </div>

          <h3>Resume Suggestions</h3>
          <ul>
            {result.suggestions.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>Interview Questions</h3>
          <ul>
            {result.interview_questions.map((q, index) => (
              <li key={index}>{q}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;