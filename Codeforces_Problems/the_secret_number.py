import sys


def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        xs = []
        p = 10  # 10**1
        while p + 1 <= n:
            d = p + 1  # 10^k + 1
            if n % d == 0:
                xs.append(n // d)
            p *= 10
        xs.sort()
        if xs:
            out_lines.append(str(len(xs)))
            out_lines.append(" ".join(map(str, xs)))
        else:
            out_lines.append("0")
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()