def _min_required_winner_votes(p_list: list[int], loser_total: int) -> int:
	total_p = 0
	cap_total = 0
	slack_total = 0
	min_at_cap_sum = 0

	for pi in p_list:
		total_p += pi
		cap_total += (pi - 1) // 2
		if (pi & 1) == 0:
			slack_total += 1
		min_at_cap_sum += (pi // 2) + 1

	if loser_total <= cap_total:
		return total_p - loser_total
	if loser_total <= cap_total + slack_total:
		return min_at_cap_sum
	return min_at_cap_sum + (loser_total - (cap_total + slack_total))


def solve() -> None:
	t_line = input().strip()
	if not t_line:
		return
	t = int(t_line)
	out_lines: list[str] = []

	for _ in range(t):
		n, x, y = map(int, input().split())
		s = input().strip()
		p_list = list(map(int, input().split()))

		total_votes = x + y
		total_p = sum(p_list)
		if total_votes < total_p:
			out_lines.append("NO")
			continue

		has0 = "0" in s
		has1 = "1" in s

		if has0 and has1:
			low_a0 = 0
			high_a0 = 0
			for ch, pi in zip(s, p_list):
				if ch == "0":
					low_a0 += (pi // 2) + 1
					high_a0 += pi
				else:
					high_a0 += (pi - 1) // 2

			low = max(low_a0, total_p - y)
			high = min(high_a0, x)
			out_lines.append("YES" if low <= high else "NO")
			continue

		if has0:
			min_x = _min_required_winner_votes(p_list, loser_total=y)
			out_lines.append("YES" if x >= min_x else "NO")
		else:
			min_y = _min_required_winner_votes(p_list, loser_total=x)
			out_lines.append("YES" if y >= min_y else "NO")

	print("\n".join(out_lines))

solve()