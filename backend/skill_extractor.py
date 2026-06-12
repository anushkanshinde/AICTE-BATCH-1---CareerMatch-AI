skills_db = [
    "python",
    "sql",
    "machine learning",
    "tensorflow",
    "pytorch",
    "react",
    "javascript",
    "node.js",
    "java",
    "docker",
    "kubernetes",
    "aws",
    "html",
    "css",
    "pandas",
    "numpy"
]

def extract_skills(text):

    text = text.lower()

    detected_skills = []

    for skill in skills_db:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills