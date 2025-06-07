import sys

def main():
    sys.stdin = open("maxcross.in", 'r')
    sys.stdout = open("maxcross.out", 'w')
    
    n, k, b = list(map(int, input().strip("\n").split()))
    crosswalks = [1 for i in range(n)]
    crosswalks.append(0)
    crosswalks.reverse()
    for _ in range(b):
        crosswalks[int(input().strip("\n"))] = 0
        
    # Calculate Prefix Sum
    pref_sum = crosswalks.copy()
    for i in range(1, n + 1):
        pref_sum[i] += pref_sum[i - 1]
    
    # Find the minimum to fix count
    count = -1
    for i in range(k, n + 1):
        count = max(pref_sum[i] - pref_sum[i - k], count)
    
    print(k - count)

main()