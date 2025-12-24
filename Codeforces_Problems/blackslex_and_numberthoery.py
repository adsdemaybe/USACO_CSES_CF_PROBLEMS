t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = float("inf")
    second = float("inf")

    for v in a:
        if v < mn:
            second = mn
            mn = v
        elif v < second:
            second = v

    print(max(mn, second - mn))