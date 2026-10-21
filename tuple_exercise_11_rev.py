t_value = (10,15,20,25,30,35,40,45,50,55)

odd_value = ()
even_value = ()

odd_list_value = []
even_list_value = []

for i_value in t_value:

    if i_value % 2 == 0:
        even_list_value.append(i_value)
    else:
        odd_list_value.append(i_value)

odd_value = tuple(odd_list_value)
even_value = tuple(even_list_value)

print("Odd =", odd_value)
print("Even =", even_value)