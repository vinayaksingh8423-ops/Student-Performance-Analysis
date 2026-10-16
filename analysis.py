
import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("students.csv")

# Calculate average marks
subjects = ["Maths", "Science", "English"]
df["Average"] = df[subjects].mean(axis=1)

# Display student performance
print("\n===== STUDENT PERFORMANCE =====")
print(df[["Name", "Average"]].round(2).to_string(index=False))

# Find class topper
topper = df.loc[df["Average"].idxmax()]

print("\n===== CLASS TOPPER =====")
print("Name:", topper["Name"])
print("Average Marks:", round(topper["Average"], 2))

# Calculate subject-wise average
subject_avg = df[subjects].mean()

print("\n===== SUBJECT-WISE AVERAGE =====")
print(subject_avg.round(2))

# Find the best-performing subject
best_subject = subject_avg.idxmax()
print("\nBest Performing Subject:", best_subject)

# Create subject-wise bar chart
plt.figure(figsize=(8, 5))
subject_avg.plot(kind="bar")
plt.title("Subject-Wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("subject_analysis.png")
plt.close()

# Create student average chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_analysis.png")
plt.close()

print("\nCharts saved successfully!")
print("Files: subject_analysis.png and student_analysis.png")
