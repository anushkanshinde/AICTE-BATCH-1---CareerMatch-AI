from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.career_advice import get_career_advice
from skill_extractor import extract_skills
from report_generator import generate_report

import fitz
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.job_roles import job_roles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Load ML Model
# ------------------------

model = joblib.load("career_model.pkl")
encoder = joblib.load("encoder.pkl")


# ------------------------
# PDF Text Extraction
# ------------------------

def extract_text(pdf_bytes):

    text = ""

    pdf = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text


# ------------------------
# Home Route
# ------------------------

@app.get("/")
def home():

    return {
        "message": "CareerMatch AI Backend Running"
    }


# ------------------------
# Analyze Resume
# ------------------------

@app.post("/analyze")
async def analyze_resume(
        file: UploadFile = File(...)
):

    contents = await file.read()

    resume_text = extract_text(contents)

    detected_skills = extract_skills(
        resume_text
    )

    features = [[
        1 if "python" in detected_skills else 0,
        1 if "sql" in detected_skills else 0,
        1 if "machine learning" in detected_skills else 0,
        1 if "react" in detected_skills else 0,
        1 if "docker" in detected_skills else 0
    ]]

    prediction = model.predict(features)

    career = encoder.inverse_transform(
        prediction
    )[0]

    role_skills = {

        "ML Engineer": [
            "python",
            "machine learning",
            "tensorflow",
            "pytorch",
            "docker"
        ],

        "Data Scientist": [
            "python",
            "sql",
            "machine learning"
        ],

        "Backend Developer": [
            "java",
            "sql",
            "docker"
        ],

        "Frontend Developer": [
            "react",
            "javascript",
            "html",
            "css"
        ],

        "Full Stack Developer": [
            "react",
            "javascript",
            "node.js",
            "sql"
        ],

        "DevOps Engineer": [
            "docker",
            "kubernetes",
            "aws"
        ]
    }

    required_skills = role_skills.get(
        career,
        []
    )

    missing_skills = []

    for skill in required_skills:

        if skill not in detected_skills:

            missing_skills.append(skill)

    documents = [resume_text]

    role_names = []

    for role, description in job_roles.items():

        documents.append(description)

        role_names.append(role)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        documents
    )

    resume_vector = vectors[0]

    results = {}

    for i, role in enumerate(role_names):

        similarity = cosine_similarity(
            resume_vector,
            vectors[i + 1]
        )[0][0]

        results[role] = round(
            similarity * 100,
            2
        )

    sorted_results = dict(
        sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    advice = get_career_advice(
        detected_skills,
        career,
        missing_skills
    )

    return {

        "career_prediction": career,

        "similarity_scores": sorted_results,

        "detected_skills": detected_skills,

        "missing_skills": missing_skills,

        "career_advice": advice
    }


# ------------------------
# Download PDF Report
# ------------------------

@app.post("/download-report")
async def download_report(
        file: UploadFile = File(...)
):

    contents = await file.read()

    resume_text = extract_text(contents)

    detected_skills = extract_skills(
        resume_text
    )

    features = [[
        1 if "python" in detected_skills else 0,
        1 if "sql" in detected_skills else 0,
        1 if "machine learning" in detected_skills else 0,
        1 if "react" in detected_skills else 0,
        1 if "docker" in detected_skills else 0
    ]]

    prediction = model.predict(features)

    career = encoder.inverse_transform(
        prediction
    )[0]

    role_skills = {

        "ML Engineer": [
            "python",
            "machine learning",
            "tensorflow",
            "pytorch",
            "docker"
        ],

        "Data Scientist": [
            "python",
            "sql",
            "machine learning"
        ],

        "Backend Developer": [
            "java",
            "sql",
            "docker"
        ],

        "Frontend Developer": [
            "react",
            "javascript",
            "html",
            "css"
        ],

        "Full Stack Developer": [
            "react",
            "javascript",
            "node.js",
            "sql"
        ],

        "DevOps Engineer": [
            "docker",
            "kubernetes",
            "aws"
        ]
    }

    required_skills = role_skills.get(
        career,
        []
    )

    missing_skills = []

    for skill in required_skills:

        if skill not in detected_skills:

            missing_skills.append(skill)

    documents = [resume_text]

    role_names = []

    for role, description in job_roles.items():

        documents.append(description)

        role_names.append(role)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        documents
    )

    resume_vector = vectors[0]

    results = {}

    for i, role in enumerate(role_names):

        similarity = cosine_similarity(
            resume_vector,
            vectors[i + 1]
        )[0][0]

        results[role] = round(
            similarity * 100,
            2
        )

    sorted_results = dict(
        sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    advice = get_career_advice(
        detected_skills,
        career,
        missing_skills
    )

    pdf_file = generate_report(
        career,
        detected_skills,
        missing_skills,
        advice,
        sorted_results
    )

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="CareerMatch_Report.pdf"
    )