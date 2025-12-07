import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        
        for x in range(2, 10**9 + 1):
            found = False
            for num in a:
                if gcd(num, x) == 1:
                    found = True
                    break
            
            if found:
                print(x)
                break
        else:
            print(-1)


main()