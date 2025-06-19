from dataHelpers import *  # Import helper functions from another file
from collections import Counter  # Built-in Python library to count frequency

# Extract the car brand names from the 0th column of the dataset
brands = colToList('car_data.txt', 0)

# Count how many times each brand appears
brand_counts = Counter(brands)

# Create the pie chart labels and values
labels = list(brand_counts.keys())
nums = list(brand_counts.values())

# Display the pie chart
simplePie(nums, labels)
