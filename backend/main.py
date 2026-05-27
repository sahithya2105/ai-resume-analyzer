from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

COMMON_SKILLS = [
    "python", "java", "c", "c++", "javascript", "react", "node", "express",
    "fastapi", "flask", "django", "html", "css", "sql", "mongodb",
    "postgresql", "machine learning", "deep learning", "nlp", "ai",
    "data analysis", "pandas", "numpy", "tensorflow", "pytorch",
    "git", "github", "aws", "docker", "kubernetes", "rest api"
]

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def extract_skills(text):
    found = []
    for skill in COMMON_SKILLS:
        if skill.lower() in text:
            found.append(skill)
    return list(set(found))

def calculate_ats_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

def get_missing_keywords(resume_text, jd_text):
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())

    missing = jd_words - resume_words

    useful_missing = [
        word for word in missing
        if len(word) > 4 and word.isalpha()
    ]

    return useful_missing[:20]

def generate_suggestions(score, missing_keywords):
    suggestions = []

    if score < 50:
        suggestions.append("Your resume has low match with the job description.")
        suggestions.append("Add more job-related keywords and skills.")
    elif score < 75:
        suggestions.append("Your resume is good, but it can be improved.")
        suggestions.append("Add more missing keywords from the job description.")
    else:
        suggestions.append("Your resume matches well with the job description.")

    if missing_keywords:
        suggestions.append("Try to include these missing keywords naturally in your resume.")

    suggestions.append("Add measurable achievements like percentages, numbers, or project results.")
    suggestions.append("Keep resume sections clear: Skills, Projects, Education, Experience.")

    return suggestions

def generate_interview_questions(skills):
    questions = []

    for skill in skills[:8]:
        questions.append(f"Explain your experience with {skill}.")
        questions.append(f"What project have you built using {skill}?")

    if not questions:
        questions = [
            "Tell me about yourself.",
            "Explain one project from your resume.",
            "What are your technical strengths?"
        ]

    return questions

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(resume)
    jd_text = job_description.lower()

    skills = extract_skills(resume_text)
    ats_score = calculate_ats_score(resume_text, jd_text)
    missing_keywords = get_missing_keywords(resume_text, jd_text)
    suggestions = generate_suggestions(ats_score, missing_keywords)
    interview_questions = generate_interview_questions(skills)

    return {
        "ats_score": ats_score,
        "skills": skills,
        "missing_keywords": missing_keywords,
        "suggestions": suggestions,
        "interview_questions": interview_questions
    }