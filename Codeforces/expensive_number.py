# Given a number k, minimize the cost where cost = k/sum_of_digits(k)
# You can remove as many digits as needed, but the number has to be atleast one digit and has to be greater than 0.

# 666
# 666/18 = 37
# 66/12 = 5.5
# 6/6 = 1 (ideal)

# 102030
# 003/3 = 1 (ideal)

# 13700
# Remove atleast 2 (leading zeros)
# 137 -> How many to remove to get 1

# Goal is to get to 1 -> include leading zeros, remove trailing zeros and all other numbers
# Answer is trailing zeros + num_non_zero - 1

t = int(input())
for _ in range(t):
    k = input()
    # Remove leading zeros
    k = k.lstrip('0')
    # Count trailing zeros
    trailing_zeros = len(k) - len(k.rstrip('0'))
    # Count non-zero digits
    non_zero_digits = len([d for d in k if d != '0'])
    # Answer is trailing zeros + non-zero digits - 1
    answer = trailing_zeros + non_zero_digits - 1
    print(answer)
    
