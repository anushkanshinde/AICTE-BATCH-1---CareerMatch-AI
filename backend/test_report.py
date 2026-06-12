from report_generator import generate_report

generate_report(
    "ML Engineer",
    ["Python", "SQL", "Machine Learning"],
    ["Docker", "TensorFlow"],
    "Learn Docker and TensorFlow. Build projects and deploy them.",
    {
        "ML Engineer": 89,
        "Data Scientist": 76,
        "Backend Developer": 40
    }
)

print("PDF Generated")