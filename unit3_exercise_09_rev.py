# 3.9 Student Gradebook
gradebook_value = {
    "Alice": [88, 92, 95],
    "Bob": [70, 65, 80],
    "Charlie": [90, 94, 89],
    "David": [82, 85, 88]
}

# Calculate averages
averages_value = {student_value: sum(marks_data) / len(marks_data) for student_value, marks_data in gradebook_value.items()}

# Sort by average (highest first)
sorted_gradebook_value = sorted(averages_value.items(), key=lambda x_value: x_value[1], reverse=True)

print(f"{'Student Name':<15} | {'Average Mark':<12}")
print("-" * 32)
for student_value, average_value in sorted_gradebook_value:
    print(f"{student_value:<15} | {average_value:<12.2f}")

top_student_value = sorted_gradebook_value[0]
print("-" * 32)
print(f"Top Student: {top_student_value[0]} with Average: {top_student_value[1]:.2f}")