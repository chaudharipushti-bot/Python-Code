L1_value = ["Amit", "Rahul", "Neha"]

print(len(L1_value))          # Returns total number of elements.
print(max([10,20,5]))   # Returns the largest element.
print(min([10,20,5]))   # Returns the smallest element.
print(sum([1,2,3]))     # Returns the total of all numbers.
print(sorted(L1_value))       # Returns a new sorted list.
L1_value.sort()               # Sorts the original list.
L1_value.reverse()            # Reverses the list.
L1_value.append("Riya")       # Adds one element at the end.
L1_value.extend(["A","B"])    # Adds multiple elements.
L1_value.insert(1,"Karan")    # Inserts element at given index.
L1_value.remove("Rahul")      # Removes first matching element.
L1_value.pop()                # Removes and returns last element.
L1_value.pop(1)               # Removes element at given index.
L1_value.clear()              # Removes all elements.
print(L1_value.count("Amit")) # Counts occurrences of an element.
print(L1_value.index("Amit")) # Returns first index of element.
print("Amit" in L1_value)     # Checks if element exists.
print("Raj" not in L1_value)  # Checks if element does not exist.
L2_value = L1_value.copy()          # Creates a copy of the list.