# DRY Principle Example
# DRY -> "Don't Repeat Yourself"
# Concept: Avoid repeating the same logic in multiple places.
# Instead, reuse code by creating functions or classes.
# This improves maintainability and reduces chances of bugs.

#BAD EXAMPLE (for reference)
"""
def area_circle(radius):
    return 3.14 * radius * radius

def area_of_cylinder(radius, height):
    return 3.14 * radius * radius * height
"""
# In the above code, the circle area formula is repeated twice.
# If we change the formula later, we must update it in multiple places — not DRY!



# GOOD EXAMPLE (Using DRY Principle)

# Function to calculate the area of a circle
def area_of_circle(radius):
    # Formula: π * r²
    return 3.14 * (radius ** 2)



# Function to calculate the volume (or lateral area) of a cylinder using the circle area
def area_of_cylinder(radius, height):
    # Reuse the circle area function instead of repeating the formula
    base_area = area_of_circle(radius)
    # Volume of cylinder = base area × height
    return base_area * height


# ---- Main program ----

# Take radius input from user
radius = int(input("Enter radius to get area: "))
print("Radius =", radius)

# Take height input from user
height = int(input("Enter height to get area: "))
print("Height =", height)

# Calculate area of circle using DRY function
circle_area = area_of_circle(radius)
print("Area of Circle is:", circle_area)

# Calculate area (volume) of cylinder using DRY function
cylinder_area = area_of_cylinder(radius, height)
print("Area (Volume) of Cylinder is:", cylinder_area)




"""
OUTPUT :
Enter radius to get area: 3
Radius = 3
Enter height to get area: 5
Height = 5
Area of Circle is: 28.26
Area (Volume) of Cylinder is: 141.3
"""