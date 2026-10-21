entered_name = "Rahul"
hobbies_value = ("Reading","Music")
friends_value = ("Amit","Neha")
degree_value = "BCA"

t4_value = (entered_name,hobbies_value,friends_value,degree_value)

x_value = input("Enter element: ")

found_value = False

for i_value in range(len(t4_value)):

    if type(t4_value[i_value]) == tuple:
        if x_value in t4_value[i_value]:
            print("Found at",i_value)
            found_value = True

    else:
        if x_value == t4_value[i_value]:
            print("Found at",i_value)
            found_value = True

if found_value == False:
    print("Not Found")