import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Disease Prediction System", page_icon="🩺")

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
    "admin": "admin123",
    "user": "1234"
}

# -------------------------------
# LOGIN PAGE
# -------------------------------
def login_page():

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users and users[username] == password:

            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid username or password")

# -------------------------------
# LOGOUT
# -------------------------------
def logout():

    st.sidebar.button(
        "Logout",
        on_click=lambda: st.session_state.update({"logged_in": False})
    )

# -------------------------------
# DISEASE PREDICTION MODEL
# -------------------------------
def predict_disease(age, gender, exercise, bp):

    risk_score = 0

    if age > 50:
        risk_score += 1

    if bp == 1:
        risk_score += 1

    if exercise == 0:
        risk_score += 1

    if risk_score >= 2:
        return 1
    else:
        return 0

# -------------------------------
# CHATBOT
# -------------------------------
def chatbot_response(query):

    q = query.lower()

    if "diabetes" in q:
        return "Diabetes is related to high blood sugar. Maintain diet and exercise."

    elif "bp" in q or "blood pressure" in q:
        return "High blood pressure can cause heart disease. Reduce salt and stress."

    elif "fever" in q:
        return "Fever may indicate infection. Stay hydrated and rest."

    elif "diet" in q:
        return "Eat fruits, vegetables and protein. Avoid junk food."

    elif "exercise" in q:
        return "Exercise at least 30 minutes daily."

    else:
        return "Please consult a doctor for accurate diagnosis."

# -------------------------------
# MAIN APP
# -------------------------------
def main_app():

    st.sidebar.title("Dashboard")
    logout()

    st.title("🩺 Disease Prediction System")

    st.subheader("Enter Health Details")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider("Age", 10, 80, 25)
        gender = st.selectbox("Gender", ["Male", "Female"])

    with col2:

        exercise = st.selectbox("Exercise", ["Yes", "No"])
        bp = st.selectbox("Blood Pressure", ["Normal", "High"])

    gender = 1 if gender == "Male" else 0
    exercise = 1 if exercise == "Yes" else 0
    bp = 1 if bp == "High" else 0

    # -------------------------------
    # PREDICT BUTTON
    # -------------------------------
    if st.button("Predict"):

        result = predict_disease(age, gender, exercise, bp)

        st.markdown("---")

        if result == 1:

            st.error("⚠️ High Risk of Disease")

            st.write("### Precautions")

            st.write("- Regular health checkups")
            st.write("- Maintain healthy diet")
            st.write("- Exercise regularly")

        else:

            st.success("✅ Low Risk")

            st.write("### Advice")

            st.write("- Continue healthy lifestyle")

    # -------------------------------
    # CHATBOT
    # -------------------------------
    st.markdown("---")
    st.subheader("🤖 AI Doctor Assistant")

    user_input = st.chat_input("Ask health question")

    if user_input:

        st.session_state.messages.append({"role":"user","content":user_input})

        st.chat_message("user").write(user_input)

        reply = chatbot_response(user_input)

        st.session_state.messages.append({"role":"assistant","content":reply})

        st.chat_message("assistant").write(reply)

# -------------------------------
# APP FLOW
# -------------------------------
if not st.session_state.logged_in:

    login_page()

else:

    main_app()
