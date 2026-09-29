import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path.cwd()
data = pd.read_csv(BASE_DIR / "data" / "student_performance.csv")

graphs = BASE_DIR / "graphs"
graphs.mkdir(exist_ok=True)

# 1. Study Hours vs Final Marks
plt.figure()
plt.scatter(data["Study_Hours"], data["Final_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.savefig(graphs / "study_hours_vs_marks.png")
plt.close()

# 2. Attendance vs Final Marks
plt.figure()
plt.scatter(data["Attendance"], data["Final_Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.savefig(graphs / "attendance_vs_marks.png")
plt.close()

# 3. Previous Marks vs Final Marks
plt.figure()
plt.scatter(data["Previous_Marks"], data["Final_Marks"])
plt.xlabel("Previous Marks")
plt.ylabel("Final Marks")
plt.title("Previous Marks vs Final Marks")
plt.savefig(graphs / "previous_marks_vs_final_marks.png")
plt.close()

print("All graphs created successfully!")