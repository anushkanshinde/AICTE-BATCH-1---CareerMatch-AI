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

## 🔄 Project Workflow


                ┌──────────────────┐
                │   Resume Upload  │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ PDF Text Parsing │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Skill Extraction │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Career Prediction│
                │ (ML Classifier)  │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Job Role Matching│
                │  (TF-IDF + NLP)  │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Skill Gap Analysis│
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ AI Career Advice │
                │ (Hugging Face)   │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ PDF Report Export│
                └──────────────────┘

---

## Screenshots

### Home Page
<img width="1920" height="1020" alt="carrerMatch" src="https://github.com/user-attachments/assets/9e889750-18ab-4f6e-b86b-532c67cedb99" />

### Analysis Result
<img width="1920" height="1080" alt="analysis1" src="https://github.com/user-attachments/assets/c5f73786-66c3-426f-8394-a3072d1bf005" />

### Generated PDF Report
<img width="1920" height="1080" alt="downloadedReport" src="https://github.com/user-attachments/assets/94e011ad-f337-47e9-9afd-f25c7470101e" />

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

## Running the Project

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


## Author
Anushka Shinde
