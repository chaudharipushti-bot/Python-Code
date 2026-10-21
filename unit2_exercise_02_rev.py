def is_prime_value(num_value):
    if num_value < 2:
        return False

    for i_value in range(2, num_value):
        # range(2, 7)
        # i = 2, 3, 4, 5, 6

        if num_value % i_value == 0:
            # Check if 7 is divisible by i

            # i = 2
            # 7 % 2 = 1
            # is it: 1 == 0  False

            # i = 3
            # 7 % 3 = 1
            # is it: 1 == 0  False

            # i = 4
            # 7 % 4 = 3
            # is it: 3 == 0  False

            # i = 5
            # 7 % 5 = 2
            # is it: 2 == 0  False

            # i = 6
            # 7 % 6 = 1
            # is it: 1 == 0  False

            return False

    return True


num_value = 7

if is_prime_value(num_value):
    print(f"{num_value} is Prime")
else:
    print(f"{num_value} is Not Prime")