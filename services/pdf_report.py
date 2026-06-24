
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
    disease,
    confidence,
    severity,
    treatment,
    prevention,
    recovery,
    filename="treeguard_report.pdf"
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        " TreeGuard AI Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"<b>Disease:</b> {disease}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Severity:</b> {severity}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"<b>Treatment:</b> {treatment}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"<b>Prevention:</b> {prevention}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"<b>Recovery Time:</b> {recovery}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return filename
