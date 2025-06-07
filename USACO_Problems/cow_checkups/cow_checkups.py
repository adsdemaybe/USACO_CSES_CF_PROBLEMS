def solve():
    N = int(input().strip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    baseCount = 0
    for i in range(N):
        if a[i] == b[i]:
            baseCount += 1

    countFinal = [0] * (N + 1)

    for K in range(2, 2*N + 1):
        S = [0] * (N + 1)
        
        for x in range(1, N + 1):
            delta = 0
            j = K - x
            if 1 <= j <= N:
                if a[j-1] == b[x-1]:
                    delta += 1
            if a[x-1] == b[x-1]:
                delta -= 1
            S[x] = S[x-1] + delta

        startL = max(1, K - N)
        endL   = min(K - 1, N)
        for l in range(startL, endL + 1):
            r = K - l
            if l > r:
                continue
            finalCount = baseCount + (S[r] - S[l-1])
            countFinal[finalCount] += 1

    for cf in countFinal:
        print(cf)

if __name__ == "__main__":
    solve()