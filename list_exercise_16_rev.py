L_value = [10,15,8,5,9,20,7,18,11,4]

odd_value = 0
even_value = 0

for i_value in L_value:
    if i_value % 2 == 0:
        even_value += i_value
    else:
        odd_value += i_value

print("Even Total =", even_value)
print("Odd Total =", odd_value)