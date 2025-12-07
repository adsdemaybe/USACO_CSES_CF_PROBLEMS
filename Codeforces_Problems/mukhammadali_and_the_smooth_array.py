import sys


def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = [0] + list(map(int, sys.stdin.readline().strip().split()))
        c = [0] + list(map(int, sys.stdin.readline().strip().split()))

        # Prefix sums of costs (keep your style and use prefix sums)
        pref_sum_cost = [0] * (n + 1)
        for i in range(1, n + 1):
            pref_sum_cost[i] = pref_sum_cost[i - 1] + c[i]

        total_cost = pref_sum_cost[n]

        # Coordinate compression of values in a (1-indexed like your arrays)
        vals = sorted(set(a[1:]))
        idx_of = {v: i + 1 for i, v in enumerate(vals)}  # 1..m
        m = len(vals)

        # Fenwick tree for prefix maximum (stores max saved cost)
        bit = [0] * (m + 2)

        def quer(pos):
            # prefix max on [1..pos]
            res = 0
            while pos > 0:
                if bit[pos] > res:
                    res = bit[pos]
                pos &= pos - 1
            return res

        def upd(pos, val):
            # point update with max
            while pos <= m + 1:
                if val > bit[pos]:
                    bit[pos] = val
                pos += pos & -pos

        # Weighted LNDS: maximize saved cost sum(c[i]) over non-decreasing subsequence of a
        max_saved = 0
        for i in range(1, n + 1):
            p = idx_of[a[i]]
            best_before = quer(p)  # allow equal values (non-decreasing)
            cur = best_before + c[i]
            if cur > max_saved:
                max_saved = cur
            upd(p, cur)

        # Minimum cost to modify = total_cost - max_saved
        print(total_cost - max_saved)


if __name__ == "__main__":
    solve()