# 3.2 Stack Simulator
class Stack_value:
    def __init__(self_value):
        self_value.items = []

    def push_value(self_value, item_value):
        self_value.items.append(item_value)

    def pop_value(self_value):
        if not self_value.is_empty_value():
            return self_value.items.pop_value()
        return "Stack Underflow"

    def peek_value(self_value):
        if not self_value.is_empty_value():
            return self_value.items[-1]
        return "Stack is Empty"

    def is_empty_value(self_value):
        return len(self_value.items) == 0

    def display_value(self_value):
        print(f"Current Stack (Top -> Bottom): {self_value.items[::-1]}")


# Simulation
stack_value = Stack_value()
print("1. Pushing 5 items: 10, 20, 30, 40, 50")
for val_value in [10, 20, 30, 40, 50]:
    stack_value.push_value(val_value)

print(f"2. Peek top element: {stack_value.peek_value()}")

print(f"3. Popped element: {stack_value.pop_value()}")
print(f"   Popped element: {stack_value.pop_value()}")

print("4. Display stack state:")
stack_value.display_value()