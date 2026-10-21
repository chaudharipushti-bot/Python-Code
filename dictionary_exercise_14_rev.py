# Reading and updating nested values
student_items = {
    "S101": {"name": "Aarav", "grade": "A"},
    "S102": {"name": "Diya", "grade": "B"}
}

# Read nested item
print("S101 Name:", student_items["S101"]["name"])

# Update nested item
student_items["S102"]["grade"] = "A+"
print("Updated S102:", student_items["S102"])