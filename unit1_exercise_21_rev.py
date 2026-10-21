# 1.21 Armstrong Number Finder
# Part (a): Check single number
num_value = int(input("Enter a number: "))
order_value = len(str(num_value))
temp_value = num_value
sum_pow_value = 0

while temp_value > 0:
    digit_value = temp_value % 10
    sum_pow_value += digit_value**order_value
    temp_value //= 10

if num_value == sum_pow_value:
    print(f"{num_value} is an Armstrong number.")
else:
    print(f"{num_value} is NOT an Armstrong number.")

# Part (b): Armstrong numbers between 1 and 999
print("\nArmstrong numbers between 1 and 999:")
for i_value in range(1, 1000):
    p_order_value = len(str(i_value))
    t_value = i_value
    text_value = 0
    while t_value > 0:
        d_value = t_value % 10
        text_value += d_value**p_order_value
        t_value //= 10
    if i_value == text_value:
        print(i_value, end=" ")
print()