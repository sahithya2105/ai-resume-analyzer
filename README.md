# 🤖 AI Resume Analyzer + ATS Score Checker

An AI-powered Resume Analysis tool that automatically analyzes your resume against a job description, calculates an ATS match score, detects missing keywords, and generates intelligent interview questions in real-time.

---

## 🌐 Live Demo

| Service | Link |
|---|---|
| 🏠 Home | https://ai-resume-analyzer-2s78.onrender.com |
| 📡 Backend API | https://ai-resume-analyzer-backend-aygp.onrender.com/docs |

---

## ✨ Features

### 📊 ATS Score Checker
- Compares your resume with the job description
- Calculates a **match score (0–100%)** using TF-IDF cosine similarity
- Gives a verdict: Strong Match / Moderate Match / Needs Work

### 🔍 Skill Extraction
- Automatically detects technical skills from your resume
- Covers: Python, React, FastAPI, Machine Learning, Docker, AWS, and more

### ❌ Missing Keywords Detection
- Identifies important keywords in the job description that are missing from your resume
- Helps you tailor your resume for specific roles

### 💡 Resume Suggestions
- Actionable tips to improve your resume
- Specific advice based on your match score

### 🎯 Interview Question Generator
- Generates likely interview questions based on your skills and the role
- Helps you prepare before applying

---

## 🧠 How It Works

```
User Uploads Resume PDF
        ↓
PDF Text Extracted (pdfplumber)
        ↓
Job Description Entered
        ↓
TF-IDF Cosine Similarity Calculated
        ↓
Skills Extracted via Keyword Matching
        ↓
Missing Keywords Identified
        ↓
Suggestions & Interview Questions Generated
        ↓
Results Displayed on Frontend
```

---

## 🛠️ Tools & Technologies Used

| Category | Tools / Technologies |
|---|---|
| Backend Framework | FastAPI |
| Programming Language | Python |
| PDF Extraction | pdfplumber |
| NLP | spaCy |
| ML / Scoring | scikit-learn (TF-IDF, Cosine Similarity) |
| Frontend | React (Vite) |
| HTTP Client | Axios |
| Styling | CSS |
| Cloud Deployment | Render.com |
| Version Control | Git & GitHub |
| Server | Uvicorn |

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Language |
| FastAPI | API Framework |
| pdfplumber | Extract text from PDF resumes |
| spaCy | Natural Language Processing |
| scikit-learn | TF-IDF vectorization & cosine similarity |
| React + Vite | Frontend UI |
| Axios | API communication |
| Render.com | Cloud Hosting |

---

## 🏗️ Project Structure

```
ai-resume-analyzer/
├── backend/
│   ├── main.py               # FastAPI backend
│   ├── requirements.txt      # Python dependencies
│   └── uploads/              # Uploaded resume storage
└── frontend/
    ├── package.json
    ├── index.html
    └── src/
        ├── App.jsx            # Main React component
        ├── main.jsx           # React entry point
        └── style.css          # Styling
```

---

## 🚀 Installation & Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/sahithya2105/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2️⃣ Setup Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`

### 4️⃣ Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/analyze` | Analyze resume against job description |

### Request (multipart/form-data)

| Field | Type | Description |
|---|---|---|
| `resume` | File (PDF) | Resume PDF file |
| `job_description` | String | Job description text |

### Response

```json
{
  "ats_score": 78.45,
  "skills": ["python", "fastapi", "react", "docker"],
  "missing_keywords": ["kubernetes", "postgresql", "redis"],
  "suggestions": [
    "Your resume matches well with the job description.",
    "Try to include missing keywords naturally in your resume.",
    "Add measurable achievements like percentages and project results."
  ],
  "interview_questions": [
    "Explain your experience with Python.",
    "What project have you built using FastAPI?",
    "Tell me about yourself."
  ]
}
```

---

## 🧪 ATS Score Interpretation

| Score | Verdict | Meaning |
|---|---|---|
| 75–100 | ✅ Strong Match | Resume aligns well with the role |
| 50–74 | 🟡 Moderate Match | Good fit but needs improvement |
| 0–49 | 🔴 Needs Work | Significant mismatch, tailor your resume |

---

## 📌 Example Output

```
ATS Score: 82%  →  Strong Match ✅

Skills Found: python, fastapi, react, git, docker, aws

Missing Keywords: kubernetes, postgresql, terraform

Suggestions:
→ Your resume matches well with the job description.
→ Add measurable achievements like percentages or project results.
→ Keep resume sections clear: Skills, Projects, Education, Experience.

Interview Questions:
Q1. Explain your experience with Python.
Q2. What project have you built using FastAPI?
Q3. Explain your experience with React.
```

---

## ☁️ Cloud Deployment (Render.com)

### Backend (Web Service)

| Field | Value |
|---|---|
| Root Directory | `backend` |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt && python -m spacy download en_core_web_sm` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port 10000` |

### Frontend (Static Site)

| Field | Value |
|---|---|
| Root Directory | `frontend` |
| Build Command | `npm install && npm run build` |
| Publish Directory | `dist` |

---

## 🔮 Future Improvements

- AI-powered suggestions using LLMs (GPT / Gemini)
- LinkedIn profile integration
- Resume scoring history & tracking
- Support for DOCX resume format
- Multi-language resume support
- Downloadable improved resume suggestions

---

## 👩‍💻 Author

**Sahithya** — [github.com/sahithya2105](https://github.com/sahithya2105)

---

## ⭐ Project Goal

Help job seekers optimize their resumes for ATS systems, identify skill gaps, and prepare for interviews — all in one place.
