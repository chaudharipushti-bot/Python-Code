L1_value = ["Amit", "Rahul", "Neha"]

entered_name = input("Enter student name: ")

if entered_name in L1_value:
    L1_value.remove(entered_name)
    print(L1_value)
else:
    print("Student Not Found")