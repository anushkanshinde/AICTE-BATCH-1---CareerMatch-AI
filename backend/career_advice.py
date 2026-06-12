import os
from dotenv import load_dotenv

load_dotenv()
import requests

API_URL = "https://router.huggingface.co/featherless-ai/v1/completions"


HF_TOKEN = os.getenv("HF_TOKEN")


def get_career_advice(
        detected_skills,
        career,
        missing_skills
):

    prompt = f"""
You are an AI Career Mentor.

Detected Skills:
{", ".join(detected_skills)}

Predicted Career:
{career}

Missing Skills:
{", ".join(missing_skills)}

Provide:

1. Strengths
2. Weaknesses
3. Learning Roadmap
4. Career Advice

Keep response concise.
"""

    headers = {
        "Authorization":
        f"Bearer {HF_TOKEN}"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": prompt,
        "max_tokens": 300
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    data = response.json()

    try:
        return data["choices"][0]["text"]

    except:
        return "AI advice unavailable."