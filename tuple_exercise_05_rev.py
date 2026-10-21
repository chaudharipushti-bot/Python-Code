t1_value = ("Rahul","Kumar","Patel")
t2_value = (75,82,90,68,88)

t3_value = (t1_value,t2_value)

x_value = input("Enter value: ")

found_value = False

for i_value in t3_value:
    if x_value in i_value:
        found_value = True

if found_value:
    print("Found")
else:
    print("Not Found")