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

from services.ai_doctor import (
    ask_ai_doctor
)

import os
import glob

files = glob.glob("audio_*.mp3")

if len(files) > 1:

    latest = max(files, key=os.path.getctime)

    for file in files:
        if file != latest:
            os.remove(file)

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="TreeGuard AI",
    page_icon="🍃 ",
    layout="wide"
)


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
load_css("assets/chart.css")
load_css("assets/style.css")
load_css("assets/home.css")
# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "total_scans" not in st.session_state:
    st.session_state.total_scans = 0

if "healthy_count" not in st.session_state:
    st.session_state.healthy_count = 0

if "disease_count" not in st.session_state:
    st.session_state.disease_count = 0

if "result" not in st.session_state:
    st.session_state.result = None

# ----------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------

st.sidebar.title("🍃  TreeGuard AI")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Analytics", "🤖 AI Doctor"]
)

st.sidebar.markdown("---")
st.sidebar.info("Made with ❤️ using Streamlit + PyTorch")
st.sidebar.info("🌿 Powered by TreeGuard AI")
st.sidebar.info("🌱 Designed & 👨‍💻 Developed by Akash Kumar")

# ----------------------------------------------------
# HOME PAGE
# ----------------------------------------------------

if page == "🏠 Home":
    if "result" not in st.session_state:
        st.session_state.result = None
    st.title("🍃  TreeGuard AI")
    st.subheader("AI Powered Plant Disease Detection System")
    st.markdown("Upload a leaf image and get instant disease detection, confidence score, severity analysis and treatment recommendations.")
    
    st.markdown("---")
    
    # Features
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("🦠 Disease Detection")
    with col2:
        st.info("📊 Confidence Analysis")
    with col3:
        st.warning("💊 Treatment Suggestions")
    
    st.markdown("---")
            
    # Image Upload
    uploaded_file = st.file_uploader(
        "📷 Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )
    
    # Prediction Section
    if uploaded_file:

        image = Image.open(uploaded_file)

        st.success(
            f"📁 Selected File: {uploaded_file.name}"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:

            if st.button(
                "🔍 Analyze Leaf",
                use_container_width=True
            ):

                with st.spinner(
                    "🧠 Analyzing Leaf..."
                ):

                    disease, confidence = predict_image(image)

                disease, confidence = predict_image(image)
                details = recommendations.get(
                                            disease,
                                            {
                                                "treatment": "Consult plant expert.",
                                                "prevention": "Maintain plant hygiene.",
                                                "recovery": "Unknown",
                                                "severity": "Unknown"
                                            }
                                        )

                severity = get_severity(confidence)

                st.session_state.result = {
                    "disease": disease,
                    "confidence": confidence,
                    "details": details,
                    "severity": severity
                }
                if ("result" in st.session_state and st.session_state.result is not None):
                    report = generate_report(
                        disease=disease,
                        confidence=confidence,
                        treatment=details["treatment"],
                        prevention=details["prevention"],
                        recovery=details["recovery"]
                    )
                    save_scan(report)

                st.success(
                    "✅ Analysis Complete"
                )
        
        # Show Result After Analysis
        if st.session_state.result:
            result = st.session_state.result
            
            disease = result["disease"]
            confidence = result["confidence"]
            details = result["details"]
            severity = result["severity"]
                
            r1, r2 = st.columns(2)

            with r1:
                st.metric(
                    "🌿 Disease",
                    disease.replace("_", " ")
                )

            with r2:
                st.metric(
                    "🎯 Confidence",
                    f"{confidence}%"
                )

            r3, r4 = st.columns(2)

            with r3:
                st.metric(
                    "⚠️ Risk Level",
                    severity["risk"]
                )

            with r4:
                st.metric(
                    "📄 Report",
                    "Ready"
                )

            
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
                        "Download PDF",
                        file,
                        "TreeGuard_Report.pdf",
                        "application/pdf",
                        use_container_width=True
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
# ANALYTICS PAGE
# ----------------------------------------------------
elif page == "📊 Analytics":
    
    
    
    # Header
    st.markdown("""
    <div class="analytics-header">
        <h1>📊 Analytics Dashboard</h1>
        <p>📈 Track your plant health monitoring insights and patterns</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get data
    history = get_history()
    metrics = get_dashboard_metrics(history)
    
    # Statistics Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card stat-total">
            <span class="stat-icon">📊</span>
            <div class="stat-number">{metrics["total_scans"]}</div>
            <div class="stat-label">Total Scans Performed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card stat-healthy">
            <span class="stat-icon">✅</span>
            <div class="stat-number" style="color: #48bb78;">{metrics["healthy"]}</div>
            <div class="stat-label">Healthy Plants Detected</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card stat-diseased">
            <span class="stat-icon">⚠️</span>
            <div class="stat-number" style="color: #fc8181;">{metrics["diseased"]}</div>
            <div class="stat-label">Diseased Plants Detected</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional Stats Row
    if metrics["total_scans"] > 0:
        healthy_percentage = (metrics["healthy"] / metrics["total_scans"]) * 100
        diseased_percentage = (metrics["diseased"] / metrics["total_scans"]) * 100
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card" style="border-top: 4px solid #4299e1;">
                <span class="stat-icon">🌿</span>
                <div class="stat-number" style="color: #4299e1; font-size: 24px;">{healthy_percentage:.1f}%</div>
                <div class="stat-label">Healthy Rate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card" style="border-top: 4px solid #ed8936;">
                <span class="stat-icon">🔬</span>
                <div class="stat-number" style="color: #ed8936; font-size: 24px;">{diseased_percentage:.1f}%</div>
                <div class="stat-label">Disease Rate</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            avg_confidence = 0
            if history:
                avg_confidence = sum(item.get('confidence', 0) for item in history) / len(history)
            st.markdown(f"""
            <div class="stat-card" style="border-top: 4px solid #9f7aea;">
                <span class="stat-icon">🎯</span>
                <div class="stat-number" style="color: #9f7aea; font-size: 24px;">{avg_confidence:.1f}%</div>
                <div class="stat-label">Avg Confidence Score</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr class='divider-custom'>", unsafe_allow_html=True)
    
    # Charts Section
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <span style="font-size: 24px;">📈</span>
        <h3 style="margin: 5 px; color: #2d3748;">Visual Insights</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Pie Chart
    if history:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            <div class="chart-container">
                <div class="chart-title">
                    <span>🍃</span> Health Distribution
                </div>
            </div>
            """, unsafe_allow_html=True)
            pie_chart = create_health_pie_chart(history)
            st.plotly_chart(pie_chart, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="chart-container">
                <div class="chart-title">
                    <span>📊</span> Disease Breakdown
                </div>
            </div>
            """, unsafe_allow_html=True)
            disease_chart = create_disease_chart(history)
            if disease_chart:
                st.plotly_chart(disease_chart, use_container_width=True)
            else:
                st.markdown("""
                <div class="empty-state">
                    <span class="empty-state-icon">🌱</span>
                    <div class="empty-state-text">No disease data to display yet</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-state-icon">📊</span>
            <div class="empty-state-text">No data available for charts yet.<br>Start scanning plants to see insights!</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr class='divider-custom'>", unsafe_allow_html=True)
    
    # Recent Scans Section
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <span style="font-size: 24px;">🕒</span>
        <h3 style="margin: 0; color: #2d3748;">Recent Scan Activity</h3>
        <span style="margin-left: auto; font-size: 14px; color: #718096;">
            Latest {count} scans
        </span>
    </div>
    """.format(count=min(5, len(history) if history else 0)), unsafe_allow_html=True)
    
    if history:
        # Display recent scans with enhanced styling
        for idx, item in enumerate(history[:5]):
            disease = item.get('disease', 'Unknown')
            confidence = item.get('confidence', 0)
            
            # Determine confidence level class
            if confidence >= 80:
                confidence_class = "confidence-high"
                confidence_emoji = "🎯"
            elif confidence >= 60:
                confidence_class = "confidence-medium"
                confidence_emoji = "📊"
            else:
                confidence_class = "confidence-low"
                confidence_emoji = "⚠️"
            
            # Determine status
            is_healthy = disease.lower() == 'healthy'
            status_badge = "badge-healthy" if is_healthy else "badge-diseased"
            status_icon = "✅" if is_healthy else "⚠️"
            status_text = "Healthy" if is_healthy else "Diseased"
            
            # Disease icon
            disease_icons = {
                'healthy': '🌿',
                'apple_scab': '🍎',
                'black_rot': '⚫',
                'cedar_rust': '🌲',
                'powdery_mildew': '🌫️',
                'leaf_spot': '🍂',
                'bacterial_spot': '🦠',
                'early_blight': '🌧️',
                'late_blight': '☔',
                'mosaic_virus': '🧬'
            }
            
            disease_icon = disease_icons.get(disease.lower(), '🌱')
            
            # Time placeholder (you can add actual timestamps if available)
            time_text = f"Scan #{idx + 1}"
            
            st.markdown(f"""
            <div class="scan-item">
                <div class="scan-disease">
                    <span class="scan-disease-icon">{disease_icon}</span>
                    <div>
                        <div class="scan-disease-name">{disease.replace('_', ' ').title()}</div>
                        <div style="display: flex; gap: 8px; margin-top: 4px;">
                            <span class="status-badge {status_badge}">{status_icon} {status_text}</span>
                        </div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 15px;">
                    <span class="scan-confidence {confidence_class}">
                        {confidence_emoji} {confidence}%
                    </span>
                    <span class="scan-time">
                        🕐 {time_text}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # View all link
        if len(history) > 5:
            st.markdown("""
            <div style="text-align: center; margin-top: 15px;">
                <span style="color: #667eea; margin: 10 px; font-weight: 500;">
                    📋 Showing 5 of {total} scans
                </span>
            </div>
            """.format(total=len(history)), unsafe_allow_html=True)
    
    else:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-state-icon">🔍</span>
            <div class="empty-state-text">
                <strong>No scan history available</strong><br>
                Start by scanning your first leaf image on the Home page!
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Actions Footer
    st.markdown("<hr class='divider-custom'>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
        <span style="font-size: 20px;">⚡</span>
        <h4 style="margin: 5 px; color: #2d3748;">Quick Actions</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠 New Scan", use_container_width=True):
            st.session_state.page = "🏠 Home"
            st.rerun()
    
    with col2:
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.rerun()
    
    with col3:
        if st.button("🤖 AI Doctor", use_container_width=True):
            st.session_state.page = "🤖 AI Doctor"
            st.rerun()

# ----------------------------------------------------
# AI DOCTOR PAGE

elif page == "🤖 AI Doctor":
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
        # Add welcome message
        welcome_msg = "👋 Hello! I'm your AI Plant Doctor. I can help you with:\n\n• Disease identification and treatment\n• Prevention tips and best practices\n• Recovery strategies and care instructions\n\nFeel free to ask me anything about plant health!"
        st.session_state.chat_history.append({"role": "assistant", "content": welcome_msg})
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 🤖 AI Plant Doctor")
        st.markdown("<small style='color: #718096;'>Your intelligent plant health assistant</small>", unsafe_allow_html=True)
    with col2:
        status = "🟢 Online" if st.session_state.result else "🟡 Waiting"
        st.markdown(f"<div style='text-align: right; padding-top: 10px;'><span class='status-indicator status-online'></span> {status}</div>", unsafe_allow_html=True)
    
    # Disease status banner
    if st.session_state.result:
        detected_disease = st.session_state.result["disease"]
        confidence = st.session_state.result["confidence"]
        
        st.markdown(f"""
        <div class="disease-banner">
            <div>
                <strong>📋 Current Patient:</strong> <span style="font-weight: 500;">{detected_disease.replace('_', ' ')}</span>
                <span style="margin-left: 16px; color: #718096; font-size: 14px;">Confidence: {confidence}%</span>
            </div>
            <div>
                <span class="disease-tag">Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        detected_disease = "Unknown"
        st.markdown("""
        <div class="disease-banner" style="border-left-color: #fc8181;">
            <div>
                <strong>⚠️ No Active Patient</strong>
                <span style="margin-left: 16px; color: #718096; font-size: 14px;">Please scan a leaf first</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Questions (Modernized)
    st.markdown("#### ⚡ Quick Actions")
    
    cols = st.columns(4)
    
    quick_questions = [
        ("💊 Treatment", "How can I treat this disease?"),
        ("🛡 Prevention", "How can I prevent this disease?"),
        ("⏳ Recovery", "What's the recovery time?"),
        ("🌱 Organic", "Any organic treatments?")
    ]
    
    for idx, (label, question) in enumerate(quick_questions):
        with cols[idx]:
            if st.button(label, use_container_width=True, key=f"quick_{idx}"):
                with st.spinner("🤔 Thinking..."):
                    answer = ask_ai_doctor(detected_disease, question)
                    st.session_state.chat_history.append({"role": "user", "content": question})
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    st.rerun()
    
    st.markdown("---")
    
    # Chat History Display
    st.markdown("#### 💬 Conversation")
    # AI Doctor Chat Section


    # --------------------------------------------------
    # CHAT MESSAGES
    # --------------------------------------------------
    if "chat_history" not in st.session_state:

        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "👋 Hello! I'm your AI Plant Doctor. How can I help you today?"
            }
        ]

    if "last_answer" not in st.session_state:
        st.session_state.last_answer = ""

    if "audio_file" not in st.session_state:
        st.session_state.audio_file = None
        
    if st.session_state.audio_file:
        st.audio(st.session_state.audio_file)
        
    chat_container = st.container()
    with chat_container:

        for message in st.session_state.chat_history:

            if message["role"] == "user":

                st.markdown(f"""
                <div class="chat-message user-message">
                    <div class="message-bubble">
                        {message["content"]}
                    </div>
                    <div class="message-avatar user-avatar">
                        👤
                    </div>
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown(f"""
                <div class="chat-message assistant-message">
                    <div class="message-avatar assistant-avatar">
                        🌿
                    </div>
                    <div class="message-bubble">
                        {message["content"]}
                    </div>
                </div>
                """, unsafe_allow_html=True)


    # --------------------------------------------------
    # VOICE BUTTON
    # --------------------------------------------------

    st.markdown("---")

    if "last_answer" in st.session_state:

        col1, col2 = st.columns([2,  3])

        with col1:

            if st.button(
                "🎙️ Hear AI Doctor",
                use_container_width=True
            ):

                st.session_state.audio_file = generate_voice(
                    st.session_state.last_answer
                )

 
        with col2:
                if "audio_file" in st.session_state:

                    st.audio(
                    st.session_state.audio_file
                )


    # --------------------------------------------------
    # INPUT AREA
    # --------------------------------------------------

    st.markdown("---")
    st.markdown("#### ✍️ Ask Your Question for normal Q. use '/'  for normal question")

    with st.form(
        key="chat_form",
        clear_on_submit=True
    ):

        col1, col2 = st.columns([4, 1])

        with col1:

            user_question = st.text_input(
                "Type your question about plant health...",
                placeholder="e.g. What are the early signs of this disease?",
                label_visibility="collapsed"
            )

        with col2:

            submit_button = st.form_submit_button(
                "🚀 Send",
                use_container_width=True
            )


    if submit_button and user_question.strip():

        with st.spinner(
            "🌿 AI Doctor is analyzing..."
        ):

            answer = ask_ai_doctor(
                detected_disease,
                user_question
            )

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": user_question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.session_state.last_answer = answer

            if "audio_file" in st.session_state:
                del st.session_state.audio_file

            st.rerun()


    # --------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:

        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True
        ):

            st.session_state.chat_history = [
                {
                    "role": "assistant",
                    "content":
                    "👋 Hello! I'm your AI Plant Doctor. How can I help you today?"
                }
            ]

            if "last_answer" in st.session_state:
                del st.session_state.last_answer

            if "audio_file" in st.session_state:
                del st.session_state.audio_file

            st.rerun()


    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    st.markdown("""
    <div class="footer-text">
🌿 Powered by TreeGuard AI & Groq Llama 3.3    </div>
    """, unsafe_allow_html=True)

