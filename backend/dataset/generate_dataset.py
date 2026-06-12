import pandas as pd
import random

data = []

for _ in range(1000):

    python = random.randint(0, 10)
    sql = random.randint(0, 10)
    ml = random.randint(0, 10)
    react = random.randint(0, 10)
    docker = random.randint(0, 10)

    if ml >= 7 and python >= 7:
        career = "ML Engineer"

    elif ml >= 5 and sql >= 7:
        career = "Data Scientist"

    elif react >= 7 and python >= 5:
        career = "Frontend Developer"

    elif sql >= 7 and docker >= 5:
        career = "Backend Developer"

    else:
        career = "Full Stack Developer"

    data.append([
        python,
        sql,
        ml,
        react,
        docker,
        career
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Python",
        "SQL",
        "ML",
        "React",
        "Docker",
        "Career"
    ]
)

df.to_csv("career_data.csv", index=False)

print("Dataset created")