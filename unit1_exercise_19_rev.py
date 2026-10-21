# 1.19 Number Reversal & Palindrome
num_value = int(input("Enter a number: "))

original_data = num_value
reversed_num_value = 0

# Part (a): Reverse using while loop
temp_value = abs(num_value)
while temp_value > 0:
    digit_value = temp_value % 10
    reversed_num_value = (reversed_num_value * 10) + digit_value
    temp_value //= 10

if num_value < 0:
    reversed_num_value = -reversed_num_value

print(f"Reversed Number: {reversed_num_value}")

# Part (b): Check Palindrome
if original_data == reversed_num_value:
    print(f"{original_data} is a Palindrome.")
else:
    print(f"{original_data} is NOT a Palindrome.")


"""
# 1. Take input from the user
text = input("Enter a string: ")

# 2. Reverse the string using a simple loop
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Adds each letter to the front

# 3. Compare original and reversed text
if text == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""