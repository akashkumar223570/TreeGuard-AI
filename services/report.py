from datetime import datetime


def generate_report(
    disease,
    confidence,
    treatment,
    prevention,
    recovery
):

    report = {

        "date":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            ),

        "disease":
            disease,

        "confidence":
            confidence,

        "treatment":
            treatment,

        "prevention":
            prevention,

        "recovery":
            recovery
    }

    return report