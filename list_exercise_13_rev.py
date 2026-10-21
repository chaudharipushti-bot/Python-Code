employees_value = [
["Amit",22,25000,"Python"],
["Rahul",25,35000,"Java"],
["Neha",24,30000,"Testing"]
]

entered_name = input("Enter Employee Name: ")

found_value = False

for emp_value in employees_value:
    if emp_value[0] == entered_name:
        print(emp_value)
        found_value = True

if found_value == False:
    print("Employee Not Found")