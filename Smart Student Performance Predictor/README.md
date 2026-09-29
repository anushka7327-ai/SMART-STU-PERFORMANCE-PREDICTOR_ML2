# 🎓 Smart Student Performance Predictor

## 📌 Project Overview

Smart Student Performance Predictor is a Machine Learning project that predicts a student's final marks based on different academic and lifestyle factors.

The project uses a Random Forest Regression model to make predictions.

## 🎯 Objective

The main objective of this project is to demonstrate how Machine Learning can be used to analyze student-related data and estimate final academic performance.

## 📊 Input Features

The model uses the following features:

- Study Hours
- Attendance Percentage
- Previous Marks
- Assignment Score
- Sleep Hours

## 🎯 Output

The model predicts:

**Final Marks out of 100**

## 🤖 Machine Learning Algorithm

The project uses:

**Random Forest Regression**

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit

## 📁 Project Structure

```text
Smart Student Performance Predictor
│
├── data/
│   └── student_performance.csv
│
├── model/
│   ├── train_model.py
│   └── student_model.pkl
│
├── app/
│   └── app.py
│
├── graphs/
│   ├── study_hours_vs_marks.png
│   ├── attendance_vs_marks.png
│   └── previous_marks_vs_final_marks.png
│
├── notebooks/
├── report/
├── screenshots/
├── requirements.txt
└── README.md