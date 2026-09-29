from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

# Project folder ka path
BASE_DIR = Path(__file__).resolve().parent.parent

# Trained model load karo
MODEL_PATH = BASE_DIR / "model" / "student_model.pkl"
model = joblib.load(MODEL_PATH)

# Page settings
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Smart Student Performance Predictor")
st.write("Enter the student's details to predict final marks.")

st.divider()

# Input fields
study_hours = st.number_input(
    "📚 Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5
)

attendance = st.number_input(
    "📅 Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=1.0
)

previous_marks = st.number_input(
    "📝 Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

assignment_score = st.number_input(
    "📖 Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)

sleep_hours = st.number_input(
    "😴 Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)

st.divider()

# Prediction button
if st.button("🔮 Predict Final Marks", use_container_width=True):

    # Input ko DataFrame me convert karo
    input_data = pd.DataFrame([{
        "Study_Hours": study_hours,
        "Attendance": attendance,
        "Previous_Marks": previous_marks,
        "Assignment_Score": assignment_score,
        "Sleep_Hours": sleep_hours
    }])

    # Prediction
    prediction = float(model.predict(input_data)[0])

    # Marks ko 0-100 ke range me rakho
    prediction = max(0, min(100, prediction))

    # Result
    st.success(f"🎯 Predicted Final Marks: {prediction:.2f} / 100")

    # Simple performance message
    if prediction >= 80:
        st.info("📈 The model predicts a high final score.")
    elif prediction >= 60:
        st.info("📊 The model predicts a moderate final score.")
    else:
        st.info("📉 The model predicts a lower final score.")

    st.caption(
        "This project is an educational ML demonstration. "
        "The prediction should not be treated as a definitive assessment."
    )
    # ==============================
# Performance Analysis Graphs
# ==============================

st.divider()

st.header("📊 Performance Analysis")

graphs_dir = BASE_DIR / "graphs"

# Study Hours vs Final Marks
study_graph = graphs_dir / "study_hours_vs_marks.png"

if study_graph.exists():
    st.subheader("📚 Study Hours vs Final Marks")
    st.image(str(study_graph), use_container_width=True)

# Attendance vs Final Marks
attendance_graph = graphs_dir / "attendance_vs_marks.png"

if attendance_graph.exists():
    st.subheader("📅 Attendance vs Final Marks")
    st.image(str(attendance_graph), use_container_width=True)

# Previous Marks vs Final Marks
previous_graph = graphs_dir / "previous_marks_vs_final_marks.png"

if previous_graph.exists():
    st.subheader("📝 Previous Marks vs Final Marks")
    st.image(str(previous_graph), use_container_width=True)