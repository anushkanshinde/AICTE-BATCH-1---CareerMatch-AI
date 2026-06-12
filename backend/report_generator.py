from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    career,
    detected_skills,
    missing_skills,
    advice,
    similarity_scores
):

    filename = "career_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CareerMatch AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Best Career Match:</b> {career}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # ------------------------
    # Detected Skills
    # ------------------------

    content.append(
        Paragraph(
            "<b>Detected Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in detected_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # ------------------------
    # Missing Skills
    # ------------------------

    content.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # ------------------------
    # Career Scores
    # ------------------------

    content.append(
        Paragraph(
            "<b>Career Scores</b>",
            styles["Heading2"]
        )
    )

    for role, score in similarity_scores.items():

        content.append(
            Paragraph(
                f"{role}: {score}%",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    # ------------------------
    # AI Career Advice
    # ------------------------

    content.append(
        Paragraph(
            "<b>AI Career Advice</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    for line in advice.split("\n"):

        line = line.strip()

        if line:

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 4)
            )

    # ------------------------
    # Build PDF
    # ------------------------

    doc.build(content)

    return filename