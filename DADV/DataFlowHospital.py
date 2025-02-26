import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits and aspect of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Remove the axes
ax.axis('off')

# Draw the external entity (Patient)
patient_box = patches.Rectangle((1, 7), 2, 1, fill=True, edgecolor='black', facecolor='lightblue')
ax.add_patch(patient_box)
ax.text(2, 7.5, "Patient", ha='center', va='center', fontsize=10, fontweight='bold')

# Draw the process (Receptionist Receives Details)
process_circle = patches.Circle((5, 7.5), 1, fill=True, edgecolor='black', facecolor='lightgreen')
ax.add_patch(process_circle)
ax.text(5, 7.5, "Receive\nDetails", ha='center', va='center', fontsize=8, fontweight='bold')

# Draw the data flow from Patient to Receptionist
ax.annotate('', xy=(3, 7.5), xytext=(4, 7.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
ax.text(3.5, 7.8, "Patient Info", ha='center', va='center', fontsize=8)

# Draw the process (Store Patient Information)
store_process_circle = patches.Circle((5, 4.5), 1, fill=True, edgecolor='black', facecolor='lightgreen')
ax.add_patch(store_process_circle)
ax.text(5, 4.5, "Store\nInformation", ha='center', va='center', fontsize=8, fontweight='bold')

# Draw the data flow from Receptionist to Store Information
ax.annotate('', xy=(5, 6.5), xytext=(5, 5.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
ax.text(5.5, 6, "Patient Info Entry", ha='center', va='center', fontsize=8)

# Draw the data store (Patient Database)
database_box = patches.Rectangle((3.5, 1.5), 3, 1, fill=True, edgecolor='black', facecolor='lightyellow')
ax.add_patch(database_box)
ax.text(5, 2, "D1: Patient Database", ha='center', va='center', fontsize=10, fontweight='bold')

# Draw the data flow from Store Information to Database
ax.annotate('', xy=(5, 3.5), xytext=(5, 2.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
ax.text(5.5, 3, "Stored Info", ha='center', va='center', fontsize=8)

# Show the plot
plt.show()
