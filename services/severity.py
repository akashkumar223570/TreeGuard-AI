def get_severity(confidence):

    if confidence >= 95:

        return {
            "level": "High Confidence",
            "risk": "🔴 High",
            "color": "red"
        }

    elif confidence >= 85:

        return {
            "level": "Medium Confidence",
            "risk": "🟡 Medium",
            "color": "orange"
        }

    else:

        return {
            "level": "Low Confidence",
            "risk": "🟢 Low",
            "color": "green"
        }