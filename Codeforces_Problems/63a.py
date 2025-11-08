import sys
import math

def main():
    n = int(sys.stdin.readline().strip("\n"))
    all_sum = 0
    x_list = []
    y_list = []
    z_list = []
    for _ in range(n):
        [x, y, z] = list(map(int, sys.stdin.readline().strip("\n").split()))
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)

    if sum(x_list) == sum(y_list) == sum(z_list) == 0:
        print("YES")
        return
    print("NO")

main()