# 3.12 Lambda Sort

student_items = [("Alice", 75), ("Bob", 45), ("Charlie", 92), ("Diana", 58), ("Ethan", 84)]

# Sort by marks descending using lambda
sorted_items = sorted(student_items, key=lambda student_value: student_value[1], reverse=True)

print("Students sorted by marks (Descending):")
for entered_name, marks_data in sorted_items:
    print(f"  {entered_name:<8}: {marks_data}")

# Filter students with marks >= 60 using lambda
passed_items = list(filter(lambda student_value: student_value[1] >= 60, sorted_items))

print("\nStudents with marks >= 60:")
for entered_name, marks_data in passed_items:
    print(f"  {entered_name:<8}: {marks_data}")
