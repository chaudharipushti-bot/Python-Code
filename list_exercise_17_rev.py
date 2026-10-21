L_value = [10,15,8,5,9,20,7,18,11,4]

even_value = [i_value for i_value in L_value if i_value % 2 == 0]

odd_value = [i_value for i_value in L_value if i_value % 2 != 0]

print("Even =", even_value)
print("Odd =", odd_value)