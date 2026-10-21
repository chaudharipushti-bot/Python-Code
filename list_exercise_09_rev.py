L1_value = ["Amit", "Rahul", "Amit", "Neha", "Amit"]

entered_name = input("Enter student name: ")

while entered_name in L1_value:
    L1_value.remove(entered_name)

print(L1_value)