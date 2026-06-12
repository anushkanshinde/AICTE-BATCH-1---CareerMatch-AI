# CareerMatch AI 🚀

CareerMatch AI is an AI-powered resume analysis platform that helps users discover suitable career paths based on their resume content.

The system analyzes resumes, detects technical skills, predicts career roles using Machine Learning, identifies skill gaps, generates AI-powered career advice, and exports professional PDF reports.

---

## Features

✅ Resume PDF Upload

✅ Resume Text Extraction

✅ Skill Detection

✅ Career Prediction using Machine Learning

✅ Career Similarity Scoring

✅ Skill Gap Analysis

✅ AI Career Advice Generation

✅ Downloadable PDF Career Reports

---

## Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios

### Backend
- FastAPI
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Classifier
- TF-IDF Vectorization

### AI Integration
- Hugging Face Inference API

### Report Generation
- ReportLab

---

## Project Workflow

Resume Upload
↓
PDF Text Extraction
↓
Skill Extraction
↓
Career Prediction
↓
Similarity Analysis
↓
Skill Gap Detection
↓
AI Career Advice
↓
PDF Report Generation

---

## Screenshots

### Home Page

(Add Screenshot Here)

### Analysis Result

(Add Screenshot Here)

### Generated PDF Report

(Add Screenshot Here)

---

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Endpoints

### Analyze Resume

```http
POST /analyze
```

Returns:

- Career Prediction
- Detected Skills
- Missing Skills
- Career Advice
- Similarity Scores

### Download PDF Report

```http
POST /download-report
```

Generates a downloadable career assessment report.

---

## Future Enhancements

- User Authentication
- Resume History Dashboard
- Real-Time Job Recommendations
- Advanced NLP Skill Extraction
- Interview Preparation Suggestions

---

## Author

Anushka Shinde
