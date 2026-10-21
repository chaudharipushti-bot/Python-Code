import math
# 1.5 Area & Perimeter
length_value = float(input("Enter length of rectangle: "))
breadth_value = float(input("Enter breadth of rectangle: "))
rect_area_value = length_value * breadth_value
rect_perimeter_value = 2 * (length_value + breadth_value)
circle_area_value = math.pi * (length_value ** 2)
print(f"Rectangle Area: {rect_area_value:.2f}")
print(f"Rectangle Perimeter: {rect_perimeter_value:.2f}")
print(f"Circle Area (Radius = {length_value}): {circle_area_value:.2f}")
