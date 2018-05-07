# CTI-110: Area of Rectangles
# Juan Hernaez
# 03/06/2018

# Define variables and/or get user input.

# Get dimensions of rectangle 1.
length_1 = int(input("Enter the length of rectangle 1: "))
width_1 = int(input("Enter the width of rectangle 1: "))

# Get dimensions of rectangle 2.
length_2 = int(input("Enter the length of rectangle 2: "))
width_2 = int(input("Enter the width of rectangle 2: "))

# Calculate the areas of the rectangles.
area_1 = length_1 * width_1
area_2 = length_2 * width_2

# Determine which rectangle has the greatest area.
if area_1 > area_2:
    print("Rectangle 1 has the greatest area.")
elif area_2 > area_1:
    print("Rectangle 2 has the greatest area.")
else:
    print("Both rectangles have the same area.")


