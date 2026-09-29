import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Load dataset
data = pd.read_csv("../data/student_performance.csv")

print("Dataset loaded successfully!")
print(data.head())


# 2. Features and target
X = data[
    [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignment_Score",
        "Sleep_Hours"
    ]
]

y = data["Final_Marks"]


# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4. Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# 5. Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")


# 6. Make predictions
predictions = model.predict(X_test)


# 7. Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("----------------")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# 8. Save trained model
joblib.dump(model, "student_model.pkl")

print("\nModel saved as student_model.pkl")