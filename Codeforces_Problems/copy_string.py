import sys

def solve():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	t = int(next(it))
	out = []
	for _ in range(t):
		n = int(next(it)); kmax = int(next(it))
		s = next(it).strip()
		tgt = next(it).strip()

		pos = [[] for _ in range(26)]
		for idx, ch in enumerate(s):
			pos[ord(ch) - 97].append(idx)

		from bisect import bisect_left

		def feasible(K):
			prev_x = 0
			x_list = [0] * n
			for i in range(n):
				lst = pos[ord(tgt[i]) - 97]
				if not lst:
					return False, None
				lower = max(prev_x, i - K)
				j = bisect_left(lst, lower)
				if j == len(lst) or lst[j] > i:
					return False, None
				x = lst[j]
				x_list[i] = x
				prev_x = x
			return True, x_list

		lo, hi = 0, n - 1
		bestK = n
		best_x = None
		while lo <= hi:
			mid = (lo + hi) // 2
			ok, xs = feasible(mid)
			if ok:
				bestK = mid
				best_x = xs
				hi = mid - 1
			else:
				lo = mid + 1

		k_needed = bestK
		c = [i - best_x[i] for i in range(n)] if best_x is not None else []

		if k_needed > kmax:
			out.append("-1")
			continue

		prev = list(s)
		out.append(str(k_needed))
		for r in range(1, k_needed + 1):
			cur = prev[:]
			for i in range(1, n):
				if r <= c[i]:
					cur[i] = prev[i - 1]
				else:
					cur[i] = prev[i]
			prev = cur
			out.append(''.join(prev))

	print('\n'.join(out))

solve()