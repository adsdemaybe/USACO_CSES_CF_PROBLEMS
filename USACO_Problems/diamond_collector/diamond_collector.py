import sys

def main():
    # sys.stdin = open("diamond.in", 'r')
    # sys.stdout = open("diamond.out", 'w')
    
    [n, k] = list(map(int, sys.stdin.readline().strip().split()))
    diamonds = []
    for _ in range(n):
        diamonds.append(int(sys.stdin.readline().strip("\n")))
    diamonds = sorted(diamonds)

    max_num = 0

    for i in range(n):
        count = 0
        for j in range(i, n):
            if abs(diamonds[i] - diamonds[j]) <= k:
                count += 1
        if max_num < count:
            max_num = count

    print(max_num)


main()