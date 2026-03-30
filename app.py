import streamlit as st
import subprocess
import speech_recognition as sr

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Disease Predictor", page_icon="🩺")

# -------------------------------
# SESSION INIT
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# USER DATABASE
# -------------------------------
users = {
    "anindo": "1234",
    "admin": "admin123"
}

# -------------------------------
# LOGIN PAGE
# -------------------------------
def login_page():
    st.title("🔐 Login System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and password == users[username]:
            st.session_state.logged_in = True
            st.success("✅ Login Successful")
            st.rerun()
        else:
            st.error("❌ Invalid Credentials")

# -------------------------------
# LOGOUT
# -------------------------------
def logout():
    st.sidebar.button("🚪 Logout", on_click=lambda: st.session_state.update({"logged_in": False}))

# -------------------------------
# VOICE INPUT FUNCTION
# -------------------------------
def get_voice_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("🎤 Speak now...")
            audio = r.listen(source, timeout=5)
        text = r.recognize_google(audio)
        return text
    except:
        return None

# -------------------------------
# CHATBOT LOGIC (OFFLINE AI)
# -------------------------------
def chatbot_response(query):
    q = query.lower()

    # Disease-based answers
    if "diabetes" in q:
        return "Diabetes is caused by high blood sugar. Control it with diet, exercise, and regular monitoring."

    elif "bp" in q or "blood pressure" in q:
        return "High BP can lead to heart problems. Reduce salt, exercise daily, and avoid stress."

    elif "fever" in q:
        return "Fever may indicate infection. Stay hydrated and take rest."

    elif "headache" in q:
        return "Headaches are often due to stress or dehydration. Drink water and rest."

    elif "cold" in q or "cough" in q:
        return "Common cold is usually viral. Drink warm fluids and take rest."

    elif "diet" in q:
        return "Eat fruits, vegetables, protein, and avoid junk food."

    elif "exercise" in q:
        return "Exercise daily for at least 30 minutes to stay healthy."

    # General fallback
    else:
        return "I recommend consulting a doctor for accurate diagnosis."

# -------------------------------
# MAIN APP
# -------------------------------
def main_app():

    st.sidebar.title("Dashboard")
    logout()

    st.markdown("<h1 style='text-align:center;'>🩺 Disease Prediction System</h1>", unsafe_allow_html=True)

    st.subheader("Enter Your Health Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 10, 80, 25)
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:
        exercise = st.selectbox("Exercise", ["Yes", "No"])
        bp = st.selectbox("Blood Pressure", ["Normal", "High"])

    # Convert values
    gender = 1 if gender == "Male" else 0
    exercise = 1 if exercise == "Yes" else 0
    bp = 1 if bp == "High" else 0

    # -------------------------------
    # PREDICTION
    # -------------------------------
    if st.button("Predict"):

        r_path = r"C:\Program Files\R\R-4.5.3\bin\Rscript.exe"

        result = subprocess.run([
            r_path,
            "predict_model.R",
            str(age), str(gender),
            str(exercise), str(bp)
        ], capture_output=True, text=True)

        output = result.stdout.strip()

        st.markdown("---")

        if output == "1":
            st.error("⚠️ High Risk of Disease")
            st.write("### Precautions:")
            st.write("- Regular health checkups")
            st.write("- Maintain diet")
            st.write("- Exercise regularly")

        else:
            st.success("✅ Low Risk")
            st.write("### Advice:")
            st.write("- Keep healthy habits")

    # -------------------------------
    # CHATBOT UI
    # -------------------------------
    st.markdown("---")
    st.subheader("🤖 AI Doctor Assistant")

    # FAQ QUICK BUTTONS
    st.write("💡 Try asking:")
    col1, col2, col3 = st.columns(3)

    if col1.button("Diabetes"):
        user_input = "diabetes"
    elif col2.button("Blood Pressure"):
        user_input = "blood pressure"
    elif col3.button("Fever"):
        user_input = "fever"
    else:
        user_input = None

    # Voice button
    if st.button("🎤 Speak"):
        voice = get_voice_input()
        if voice:
            user_input = voice

    # Chat input
    text_input = st.chat_input("Ask your health question...")
    if text_input:
        user_input = text_input

    # Process input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        reply = chatbot_response(user_input)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

    # Show history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

# -------------------------------
# APP FLOW
# -------------------------------
if not st.session_state.logged_in:
    login_page()
else:
    main_app()
