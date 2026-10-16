
import pandas as pd
import matplotlib.pyplot as plt

# Read student data from CSV file
df = pd.read_csv("students.csv")

# Calculate average marks
subjects = ["Maths", "Science", "English"]
df["Average"] = df[subjects].mean(axis=1).round(2)

# Calculate result: pass if every subject has at least 33 marks
df["Result"] = (df[subjects] >= 33).all(axis=1)
df["Result"] = df["Result"].map({
    True: "Pass",
    False: "Fail"
})

# Display student performance
print("\nSTUDENT PERFORMANCE ANALYSIS")
print(df.to_string(index=False))

# Find topper
topper = df.loc[df["Average"].idxmax()]
print("\nTop Performer:", topper["Name"])
print("Highest Average:", topper["Average"])

# Subject-wise average
print("\nSUBJECT-WISE AVERAGE")
print(df[subjects].mean().round(2))

# Count pass and fail students
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\nPASS/FAIL SUMMARY")
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)


# Draw average marks chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

# Save graph as image
plt.savefig("performance_chart.png")
plt.show()

# Count pass and fail students
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\nPASS/FAIL SUMMARY")
print("Passed Students:", pass_count)
print("Failed Students:", fail_count)
