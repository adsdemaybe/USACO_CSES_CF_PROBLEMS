import bisect

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx +=2
        a = list(map(int, data[idx:idx+N]))
        idx +=N
        
        S = [x % M for x in a]
        S.sort()
        extended = S.copy()
        for x in S:
            extended.append(x + M)
        prefix = [0] * (len(extended) + 1)
        for i in range(len(extended)):
            prefix[i+1] = prefix[i] + extended[i]
        
        min_sum = float('inf')
        half = N // 2
        for start in range(N):
            end = start + N -1
            mid = start + half
            median = extended[mid]
            
            left_count = mid - start
            left_sum = median * left_count - (prefix[mid] - prefix[start])
            
            right_count = (start + N -1) - mid
            right_sum = (prefix[start + N] - prefix[mid +1]) - median * right_count
            
            total = left_sum + right_sum
            if total < min_sum:
                min_sum = total
        
        print(min_sum)

solve()