L1_value = ["Amit", "Rahul", "Amit", "Neha"]

entered_name = input("Enter student name: ")

if entered_name in L1_value:
    print("Count =", L1_value.count(entered_name))
    print("First Position =", L1_value.index(entered_name))
else:
    print("Student Not Found")