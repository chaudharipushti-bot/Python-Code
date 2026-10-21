# 3.10 Report Card with f-strings

student_name_value = "Alex Morgan"
roll_no_value = 20261012
marks_data = [85, 92, 78, 88, 95]

total_value = sum(marks_data)
percentage_value = total_value / len(marks_data)

if percentage_value >= 90:
    grade_value = "A+"
elif percentage_value >= 80:
    grade_value = "A"
elif percentage_value >= 70:
    grade_value = "B"
else:
    grade_value = "C"

print("=" * 40)
print(f"{'STUDENT REPORT CARD':^40}")
print("=" * 40)
print(f"Name   : {student_name_value:<25}")
print(f"Roll No: {roll_no_value:<25}")
print("-" * 40)

# Loop with auto-incrementing index numbers
for idx_value, mark_value in enumerate(marks_data, start=1):
    print(f"Subject {idx_value} Marks : {mark_value:>5}")

print("-" * 40)
print(f"Total Marks     : {total_value:>5} / 500")
print(f"Percentage      : {percentage_value:>5.2f}%")
print(f"Grade Obtained  : {grade_value:>5}")
print("=" * 40)
