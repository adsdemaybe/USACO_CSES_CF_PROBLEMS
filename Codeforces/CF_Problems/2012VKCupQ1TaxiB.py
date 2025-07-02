import sys
import math

def main():
    groups = int(sys.stdin.readline().strip("\n"))
    group_vals = list(map(int, sys.stdin.readline().strip("\n").split()))

    counts = [0, 0, 0, 0]
    for k in range(groups):
        counts[group_vals[k] - 1] += 1

    one = counts[0] // 4
    one_rem = counts%4
    two = counts[1] // 2
    two_rem = counts[1]%2
    three = counts[2]
    four = 
    
print(main())