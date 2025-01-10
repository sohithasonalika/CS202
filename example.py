import math
import matplotlib.pyplot as plt

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
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
threshold = 30
large_areas = [area for area in areas if area > threshold]
print(f"Areas greater than {threshold}:", large_areas)
