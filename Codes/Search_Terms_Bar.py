import matplotlib.pyplot as plt
import numpy as np

# Define categories and their respective keywords
categories = {
    "Human Task Performance": [
        "Human Task Performance",
        "Task Performance",
        "Precision Task Performance",
        "Dual Task Performance",
        "Dual Motor Task Performance",
        "Collaborative Decision Making Task Performance",
        "Performance in Remote Collaboration Task",
        "Cognitive Workload",
        "Appropriacy in Task Performance",
        "Subjective Discomfort during VR"
    ],
    "Immersive Systems": [
        "Virtual Reality",
        "Augmented Reality",
        "Mixed Reality",
        "Extended Reality",
        "VR",
        "AR",
        "MR",
        "XR",
        "Spatial Presence",
        "Vection",
        "Effects of Embodiment"
    ],
    "Factors of HTP": [
        "Cognitive Performance",
        "Multi-task Cognitive Performance",
        "Multi-task Mental Performance",
        "Cognitive Workload",
        "Executive Functioning",
        "Psychomotor"
    ],
    "User Experience": [
        "User Experience",
        "Augmented Reality Usability",
        "Spatial Processing",
        "Workload"
    ]
}

# Count the number of keywords in each category
category_counts = {category: len(keywords) for category, keywords in categories.items()}

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(category_counts.keys(), category_counts.values(), color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0'])
plt.title('Keyword Categories vs Number of Papers')
plt.xlabel('Categories')
plt.ylabel('Number of Keywords')
plt.xticks(rotation=15)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
