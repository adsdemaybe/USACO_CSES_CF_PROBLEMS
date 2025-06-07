import sys

num_of_cows = 6
num_of_officers = 3
input = [3, 1, 4159, 2, 6, 5]

min_suffix_sum = 0
current_min = min(input[:2])
for i in range(6):
    if(input[i] < current_min):
        