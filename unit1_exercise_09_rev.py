# 1.9 Swap Without Temp
first_value = int(input("Enter first number (a): "))
second_value = int(input("Enter second number (b): "))
print(f"\nOriginal Values: a = {first_value}, b = {second_value}")
# Method 1: Tuple Swap
first_value, second_value = second_value, first_value
print(f"After Tuple Swap: a = {first_value}, b = {second_value}")
# Method 2: Arithmetic Swap
first_value = first_value + second_value
second_value = first_value - second_value
first_value = first_value - second_value
print(f"After Arithmetic Swap (back to original): a = {first_value}, b = {second_value}")
