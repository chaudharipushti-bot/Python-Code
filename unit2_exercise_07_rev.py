# 3.7 Modular Calculator

def add_value(first_value, second_value):
    return first_value + second_value

def subtract_value(first_value, second_value):
    return first_value - second_value

def multiply_value(first_value, second_value):
    return first_value * second_value

def divide_value(first_value, second_value):
    try:
        return first_value / second_value
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"

def power_value(first_value, second_value):
    return first_value ** second_value

def calculator_value():
    print(" --- Modular Calculator ---")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. Power | 6. Exit")
    
    choice_value = input("Enter choice (1-6): ")
    
    if choice_value == '6':
        print("Exiting Calculator.")
        return
        
    num1_value = float(input("Enter first number: "))
    num2_value = float(input("Enter second number: "))
    
    if choice_value == '1':
        print(f"Result: {add_value(num1_value, num2_value)}")
    elif choice_value == '2':
        print(f"Result: {subtract_value(num1_value, num2_value)}")
    elif choice_value == '3':
        print(f"Result: {multiply_value(num1_value, num2_value)}")
    elif choice_value == '4':
        print(f"Result: {divide_value(num1_value, num2_value)}")
    elif choice_value == '5':
        print(f"Result: {power_value(num1_value, num2_value)}")
    else:
        print("Invalid Choice!")

# Example execution call
calculator_value()
