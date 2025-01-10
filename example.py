"""
This script calculates the areas of circles given their radii, performs some basic 
mathematical operations on the results, and visualizes them using a bar chart. 
Additionally, the script includes examples of array manipulations, element-wise 
operations, and filtering based on specific conditions.
"""

import math
import matplotlib.pyplot as plt

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius**2

# Create a list of radii
radii = [1, 2, 3, 4, 5]

# Calculate areas for the radii using list comprehension
areas = [calculate_circle_area(r) for r in radii]

# Print the results
print("Radii:", radii)
print("Areas:", areas)

# Perform basic mathematical operations
sum_areas = sum(areas)
average_area = sum_areas / len(areas)

print("Sum of areas:", sum_areas)
print("Average area:", average_area)

# Generate a simple bar chart to visualize the areas
plt.bar(radii, areas, color='blue', alpha=0.7)
plt.title("Circle Areas for Given Radii")
plt.xlabel("Radius")
plt.ylabel("Area")
plt.show()

# Additional array manipulations
squared_radii = [r**2 for r in radii]
print("Squared Radii:", squared_radii)

# Element-wise operations
radii_plus_one = [r + 1 for r in radii]
print("Radii + 1:", radii_plus_one)

# Finding maximum and minimum areas
max_area = max(areas)
min_area = min(areas)

print("Maximum area:", max_area)
print("Minimum area:", min_area)

# Filter areas greater than a threshold
THRESHOLD = 30
large_areas = [area for area in areas if area > THRESHOLD]
print(f"Areas greater than {THRESHOLD}:", large_areas)
