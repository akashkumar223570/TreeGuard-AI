
import streamlit as st
from PIL import Image

from services.predictor import predict_image
from services.recommendations import recommendations
from services.severity import get_severity
from services.report import generate_report
from services.history import (
    save_scan,
    get_history
)
from services.analytics import (
    create_health_pie_chart,
    create_disease_chart,
    get_dashboard_metrics
)
from services.pdf_report import (
    create_pdf_report
)
from services.voice import generate_voice

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="TreeGuard AI",
    page_icon="🌳",
    layout="wide"
)


# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        #22C55E,
        #14B8A6,
        #06B6D4
    );
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.metric-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

.footer {
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "total_scans" not in st.session_state:
    st.session_state.total_scans = 0

if "healthy_count" not in st.session_state:
    st.session_state.healthy_count = 0

if "disease_count" not in st.session_state:
    st.session_state.disease_count = 0


# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🌳 TreeGuard AI</h1>

<h3>AI Powered Plant Disease Detection System</h3>

<p>
Upload a leaf image and get instant disease detection,
confidence score, severity analysis and treatment recommendations.
</p>

</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# FEATURES
# ----------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🦠 Disease Detection")

with col2:
    st.info("📊 Confidence Analysis")

with col3:
    st.warning("💊 Treatment Suggestions")


st.markdown("---")


# ----------------------------------------------------
# IMAGE UPLOAD
# ----------------------------------------------------

uploaded_file = st.file_uploader(
    "📷 Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)


# ----------------------------------------------------
# PREDICTION SECTION
# ----------------------------------------------------


if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(
            image,
            caption="Uploaded Leaf",
            use_container_width=True
        )

    with col2:

        if st.button("🔍 Analyze Leaf"):

            with st.spinner("Analyzing Leaf..."):

                disease, confidence = predict_image(image)

            details = recommendations[disease]
            severity = get_severity(confidence)

            # Save result in session state
            st.session_state.result = {
                "disease": disease,
                "confidence": confidence,
                "details": details,
                "severity": severity
            }

            report = generate_report(
                disease=disease,
                confidence=confidence,
                treatment=details["treatment"],
                prevention=details["prevention"],
                recovery=details["recovery"]
            )

            save_scan(report)

        # Show Result After Analysis
        if "result" in st.session_state:

            result = st.session_state.result

            disease = result["disease"]
            confidence = result["confidence"]
            details = result["details"]
            severity = result["severity"]

            st.success("✅ Analysis Complete")

            r1, r2, r3 = st.columns(3)

            with r1:
                st.metric(
                    "Disease",
                    disease.replace("_", " ")
                )

            with r2:
                st.metric(
                    "Confidence",
                    f"{confidence}%"
                )

            with r3:
                st.metric(
                    "Risk Level",
                    severity["risk"]
                )

            # PDF
            pdf_file = create_pdf_report(
                disease=disease,
                confidence=confidence,
                severity=severity["risk"],
                treatment=details["treatment"],
                prevention=details["prevention"],
                recovery=details["recovery"]
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    "📄 Download Report",
                    file,
                    "TreeGuard_Report.pdf",
                    "application/pdf"
                )

            st.markdown("---")

            st.subheader("💊 Treatment")
            st.info(details["treatment"])

            st.subheader("🛡 Prevention")
            st.info(details["prevention"])

            st.subheader("⏳ Recovery Time")
            st.success(details["recovery"])

            # Voice
            if st.button("🔊 Speak Result"):

                text = f"""
                Disease detected is {disease}.
                Confidence is {confidence} percent.
                Treatment is {details['treatment']}
                """

                audio_file = generate_voice(text)

                st.audio(audio_file)


# ----------------------------------------------------
# ANALYTICS
# ----------------------------------------------------

st.markdown("---")

st.subheader("📊 Dashboard")
st.markdown("---")
st.subheader("📊 Analytics Dashboard")

history = get_history()

metrics = get_dashboard_metrics(history)

c1, c2, c3 = st.columns(3)

c1.metric("Total Scans", metrics["total_scans"])
c2.metric("Healthy", metrics["healthy"])
c3.metric("Diseased", metrics["diseased"])


pie_chart = create_health_pie_chart(history)

st.plotly_chart(
    pie_chart,
    use_container_width=True
)

disease_chart = create_disease_chart(history)

if disease_chart:

    st.plotly_chart(
        disease_chart,
        use_container_width=True
    )


c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Scans",
        st.session_state.total_scans
    )

with c2:
    st.metric(
        "Healthy",
        st.session_state.healthy_count
    )

with c3:
    st.metric(
        "Diseased",
        st.session_state.disease_count
    )

st.markdown("---")

st.subheader("🕒 Recent Scans")

history = get_history()

if history:

    for item in history[:5]:

        st.write(
            f"🌿 {item['disease']} "
            f"({item['confidence']}%)"
        )

else:

    st.info(
        "No scan history available."
    )
# ----------------------------------------------------
# AI DOCTOR
# ----------------------------------------------------

st.markdown("---")

st.subheader("🤖 AI Doctor")

user_query = st.text_input(
    "Ask about plant diseases..."
)

if user_query:

    st.info(
        "Gemini AI Integration Coming Next Step"
    )


# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)