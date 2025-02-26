import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

# Define the project tasks and their start and end dates with new dates
tasks = [
    {"Task": "Requirement Analysis", "Start": "2024-06-12", "End": "2024-07-02"},
    {"Task": "Gather Requirements", "Start": "2024-06-12", "End": "2024-06-25"},
    {"Task": "Document Requirements", "Start": "2024-06-26", "End": "2024-07-02"},
    {"Task": "Design", "Start": "2024-07-03", "End": "2024-08-06"},
    {"Task": "System Architecture Design", "Start": "2024-07-03", "End": "2024-07-16"},
    {"Task": "User Interface Design", "Start": "2024-07-17", "End": "2024-07-30"},
    {"Task": "Technical Specifications", "Start": "2024-07-31", "End": "2024-08-06"},
    {"Task": "Implementation", "Start": "2024-08-07", "End": "2024-09-01"},
    {"Task": "Front-end Development", "Start": "2024-08-07", "End": "2024-08-27"},
    {"Task": "Back-end Development", "Start": "2024-08-28", "End": "2024-09-17"},
    {"Task": "Integration of APIs", "Start": "2024-09-18", "End": "2024-10-01"},
    {"Task": "Testing", "Start": "2024-10-02", "End": "2024-11-20"},
    {"Task": "Unit Testing", "Start": "2024-10-02", "End": "2024-10-15"},
    {"Task": "Integration Testing", "Start": "2024-10-16", "End": "2024-10-29"},
    {"Task": "System Testing", "Start": "2024-10-30", "End": "2024-11-12"},
    {"Task": "User Acceptance Testing", "Start": "2024-11-13", "End": "2024-11-20"},
    {"Task": "Deployment", "Start": "2024-11-21", "End": "2024-12-11"},
    {"Task": "Deploy to Staging", "Start": "2024-11-21", "End": "2024-11-27"},
    {"Task": "Final Adjustments", "Start": "2024-11-28", "End": "2024-12-04"},
    {"Task": "Go Live", "Start": "2024-12-05", "End": "2024-12-11"},
]

# Convert to a DataFrame
df = pd.DataFrame(tasks)

# Convert dates to datetime format
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Calculate the duration of each task
df["Duration"] = df["End"] - df["Start"]

# Create a figure and axis for the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each task as a bar in the Gantt chart
for i, task in df.iterrows():
    start = date2num(task["Start"])
    end = date2num(task["End"])
    ax.barh(task["Task"], task["Duration"].days, left=start, height=0.5, align='center')

# Format the x-axis to show dates
ax.xaxis_date()
plt.gca().invert_yaxis()

# Set labels and title
plt.xlabel("Date")
plt.ylabel("Task")
plt.title("Gantt Chart for 'Travel Saathi' Project")

# Show the Gantt chart
plt.tight_layout()
plt.show()
