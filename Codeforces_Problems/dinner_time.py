# Given n, m, p, q you need to make sure that there exists:
# - an array of size n which sums to m
# - every group of size p in that array sums to q
# - the array can contain negative numbers

# n = 3, m = 2, p = 2, q = 1
# [1, 0, 1] 
# 5 4 2 3
# [-2, 5, -2, 5, -2]
# 4 4 1 3 -> if p = 1, and q > n/m, print NO (obs.)
# [3, 3, 3, 3]
# 10 7 5 2 -> if 
# [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
# 3 1 2 1
# [0, 1, 0]