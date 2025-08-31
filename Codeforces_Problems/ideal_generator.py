# Given k, an array of length k should be made such that the array is palindromic.
# The array is valid only if the array is palindromic, and can sum to any integer greater than k.

# k = 4
# [x, y, y, x]
# in this example, this is not valid because if x = 2, regardless of if x >= 1, the number skips
# [1, 1, 1, 1] sum = 4
# [1, 2, 2, 1] sum = 6
# sum skips, so not valid

# k = 3
# [x, y, x]
# [1, 1, 1] sum = 3
# [1, 2, 1] sum = 4
# [2, 1, 2] sum = 5
# [2, 2, 2] sum = 6

# if the length is even, the array is not valid

test_cases = int(input())
for _ in range(test_cases):
    if(int(input()) % 2 == 0):
        print("NO")
    else:
        print("YES")