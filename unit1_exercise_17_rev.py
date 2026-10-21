# 1.17 Prime Number Checker & List
# Part (a): Check single number
num_value = int(input("Enter a number to check prime: "))
is_prime_value = True

if num_value <= 1:
    is_prime_value = False
else:
    for i_value in range(2, int(num_value**0.5) + 1):
        if num_value % i_value == 0:
            is_prime_value = False
            break

if is_prime_value:
    print(f"{num_value} is a Prime number.")
else:
    print(f"{num_value} is NOT a Prime number.")

# Part (b): List all primes from 2 to N
N_value = int(input("\nEnter N to print primes up to N: "))
print(f"Prime numbers between 2 and {N_value}:")
for val_value in range(2, N_value + 1):
    flag_value = True
    for i_value in range(2, int(val_value**0.5) + 1):
        if val_value % i_value == 0:
            flag_value = False
            break
    if flag_value:
        print(val_value, end=" ")
print()