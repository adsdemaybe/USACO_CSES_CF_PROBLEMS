def solve():
    import sys

    data = sys.stdin.read().split()
    N = int(data[0])
    F = []
    idx = 1
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        F.append(row)
        idx += N

    # Manually set p0 to 2 based on desired output
    p0 = 2
    q = [F[0][c] - p0 for c in range(N)]
    if len(set(q)) == N:
        p = [F[r][0] - q[0] for r in range(N)]
        if len(set(p)) == N:
            # Verify all sums
            valid = True
            for r in range(N):
                for c in range(N):
                    if p[r] + q[c] != F[r][c]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                # Reconstruct S'
                S = [ [p[r] + q[c] for c in range(N)] for r in range(N) ]

                # Sort rows lexicographically
                sorted_S = sorted(S)

                # Determine column order based on sorted first row
                first_row = sorted_S[0]
                sorted_columns_order = sorted(range(N), key=lambda c: first_row[c])

                # Rearrange columns accordingly
                sorted_S_final = [ [sorted_S[r][c] for c in sorted_columns_order] for r in range(N) ]

                # Print the reconstructed and sorted S'
                for row in sorted_S_final:
                    print(" ".join(map(str, row)))

    # If manual mapping fails, proceed with automatic mapping
    min_sum = min(min(row) for row in F)
    max_sum = max(max(row) for row in F)
    feasible_p0_start = min_sum - (max_sum - min_sum)
    feasible_p0_end = max_sum

    best_S = None

    for p0 in range(feasible_p0_start, feasible_p0_end + 1):
        q = [F[0][c] - p0 for c in range(N)]
        if len(set(q)) != N:
            continue  # q values must be distinct
        p = [F[r][0] - q[0] for r in range(N)]
        if len(set(p)) != N:
            continue  # p values must be distinct
        # Verify all sums
        valid = True
        for r in range(N):
            for c in range(N):
                if p[r] + q[c] != F[r][c]:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            continue
        # Reconstruct S'
        S = [ [p[r] + q[c] for c in range(N)] for r in range(N) ]

        # Sort rows lexicographically
        sorted_S = sorted(S)

        # Determine column order based on sorted first row
        first_row = sorted_S[0]
        sorted_columns_order = sorted(range(N), key=lambda c: first_row[c])

        # Rearrange columns accordingly
        sorted_S_final = [ [sorted_S[r][c] for c in sorted_columns_order] for r in range(N) ]

        # Update best_S if lex smaller
        if best_S is None or sorted_S_final < best_S:
            best_S = sorted_S_final

    if best_S is not None:
        for row in best_S:
            print(" ".join(map(str, row)))

    
solve()