def sacred_perm(n: int) -> list[int]:
    a = [0]
    for k in range(1, n + 1):
        half = 1 << (k - 1)
        a = [(x << 1) | 1 for x in a] + [x << 1 for x in range(half)]
    return a


t = int(input())
i = 1
out_lines = []
for _ in range(t):
    n = int(input())
    i += 1
    perm = sacred_perm(n)
    print(" ".join(map(str, perm)))