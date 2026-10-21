# 2.1 Function Basics
def greet_value(entered_name):
    print(f"Hello, {entered_name}! Welcome to the course.")

def square_value(n_value):
    return n_value ** 2

def cube_value(n_value):
    return n_value ** 3

# Calling each function 3 times with different values
print("--- Greet Calls ---")
greet_value("Alice")
greet_value("Bob")
greet_value("Charlie")

print("\n--- Square Calls ---")
print(f"Square of 4: {square_value(4)}")
print(f"Square of 7: {square_value(7)}")
print(f"Square of 12: {square_value(12)}")

print("\n--- Cube Calls ---")
print(f"Cube of 2: {cube_value(2)}")
print(f"Cube of 3: {cube_value(3)}")
print(f"Cube of 5: {cube_value(5)}")