import plotly.express as px
import pandas as pd


# ----------------------------------
# HEALTH COUNTS
# ----------------------------------

def get_health_counts(history):

    healthy = 0
    diseased = 0

    for item in history:

        if item["disease"] == "Tomato_healthy":
            healthy += 1
        else:
            diseased += 1

    return healthy, diseased


# ----------------------------------
# PIE CHART
# ----------------------------------

def create_health_pie_chart(history):

    healthy, diseased = get_health_counts(history)

    df = pd.DataFrame({
        "Category": [
            "Healthy",
            "Diseased"
        ],
        "Count": [
            healthy,
            diseased
        ]
    })

    fig = px.pie(
        df,
        values="Count",
        names="Category",
        hole=0.4,
        title="Plant Health Distribution"
    )

    fig.update_layout(
        height=450
    )

    return fig


# ----------------------------------
# DISEASE FREQUENCY
# ----------------------------------

def get_disease_frequency(history):

    disease_frequency = {}

    for item in history:

        disease = item["disease"]

        if disease not in disease_frequency:

            disease_frequency[disease] = 1

        else:

            disease_frequency[disease] += 1

    return disease_frequency


# ----------------------------------
# BAR CHART
# ----------------------------------

def create_disease_chart(history):

    disease_frequency = get_disease_frequency(
        history
    )

    if len(disease_frequency) == 0:

        return None

    df = pd.DataFrame({

        "Disease":
            list(
                disease_frequency.keys()
            ),

        "Count":
            list(
                disease_frequency.values()
            )
    })

    fig = px.bar(
        df,
        x="Disease",
        y="Count",
        title="Disease Distribution"
    )

    fig.update_layout(
        height=450
    )

    return fig


# ----------------------------------
# DASHBOARD METRICS
# ----------------------------------

def get_dashboard_metrics(history):

    total_scans = len(history)

    healthy, diseased = get_health_counts(
        history
    )

    return {

        "total_scans":
            total_scans,

        "healthy":
            healthy,

        "diseased":
            diseased
    }

