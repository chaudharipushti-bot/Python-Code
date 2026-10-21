# Accessing keys using bracket notation and .get() with defaults
student_value = {"name": "Aniket", "age": 21, "course": "M.Sc. IT"}

print("Name:", student_value["name"])
print("Age:", student_value.get("age"))
print("Grade (Default):", student_value.get("grade", "Not Assigned"))