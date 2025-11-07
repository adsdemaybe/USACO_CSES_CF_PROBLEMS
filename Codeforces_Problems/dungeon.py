import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []

    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(m)]
        C = [int(next(it)) for _ in range(m)]

        # Split monsters by reward c
        pos = []  # (b, c) with c > 0
        zeros = []  # b where c == 0
        for b, c in zip(B, C):
            if c > 0:
                pos.append((b, c))
            else:
                zeros.append(b)

        # Coordinate compression over all relevant values
        vals = sorted(set(A + B + [c for _, c in pos]))
        idx_of = {v: i+1 for i, v in enumerate(vals)}  # 1-based indices for Fenwick
        K = len(vals)

        # Fenwick tree to store counts of swords per damage index
        bit = [0] * (K + 1)

        def bit_add(i: int, delta: int):
            while i <= K:
                bit[i] += delta
                i += i & -i

        def bit_sum(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        # Find smallest index j such that prefix >= k (i.e., index of k-th sword)
        # Assumes 1 <= k <= total swords
        def bit_find_kth(k: int) -> int:
            idx = 0
            bit_mask = 1 << (K.bit_length())
            while bit_mask:
                nxt = idx + bit_mask
                if nxt <= K and bit[nxt] < k:
                    k -= bit[nxt]
                    idx = nxt
                bit_mask >>= 1
            return idx + 1

        # Initialize swords
        for a in A:
            bit_add(idx_of[a], 1)

        kills = 0

        pos.sort()
        for b, c in pos:
            # Find first sword with damage >= b
            # Locate the lower_bound index for b in vals (1-based)
            i_b = bisect_left(vals, b) + 1
            if i_b > K:
                # No sword can ever meet this requirement
                continue
            left = bit_sum(i_b - 1)
            total = bit_sum(K)
            if total - left <= 0:
                continue  # no available sword with damage >= b
            j = bit_find_kth(left + 1)  # index of the smallest sword >= b
            # Current sword damage value
            vj = vals[j - 1]
            bit_add(j, -1)  # consume
            # New sword damage
            new_v = vj if vj >= c else c
            bit_add(idx_of[new_v], 1)
            kills += 1

        zeros.sort()
        for b in zeros:
            i_b = bisect_left(vals, b) + 1
            if i_b > K:
                # No sword has enough damage for this monster
                continue
            left = bit_sum(i_b - 1)
            total = bit_sum(K)
            if total - left <= 0:
                continue
            j = bit_find_kth(left + 1)
            bit_add(j, -1)  # sword disappears
            kills += 1

        out_lines.append(str(kills))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
