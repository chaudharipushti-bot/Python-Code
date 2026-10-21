# 1.14 Grade Calculator
marks_data = float(input("Enter total marks: "))

if marks_data >= 90:
    grade_value = "A+"
elif marks_data >= 80:
    grade_value = "A"
elif marks_data >= 70:
    grade_value = "B"
elif marks_data >= 60:
    grade_value = "C"
elif marks_data >= 35:
    grade_value = "D"
else:
    grade_value = "Fail"

print(f"Grade: {grade_value}")
if marks_data >= 90:
    print("Distinction!")