from bisect import bisect_left, bisect_right

def solve_farm_problem(test_cases):
    results = []
    
    for case in test_cases:
        N, K, positions, restrictions = case

        all_positions = set(positions)
        for l, r, _ in restrictions:
            all_positions.add(l)
            all_positions.add(r)
        compressed = sorted(all_positions) 
        pos_to_index = {pos: i for i, pos in enumerate(compressed)}
        
        compressed_length = len(compressed)
        tree_array = [0] * compressed_length 
        for pos in positions:
            tree_array[pos_to_index[pos]] = 1  
        
        prefix_sum = [0] * (compressed_length + 1)
        for i in range(compressed_length):
            prefix_sum[i + 1] = prefix_sum[i] + tree_array[i]
        
        def count_trees(l, r):
            l_idx = pos_to_index[l]
            r_idx = pos_to_index[r]
            return prefix_sum[r_idx + 1] - prefix_sum[l_idx]
        
        low, high = 0, N
        while low <= high:
            mid = (low + high) // 2  
            
            cut_trees = set(positions[:mid])
            valid = True
            
            for l, r, t in restrictions:
                trees_in_range = count_trees(l, r)
                remaining_trees = trees_in_range - len(cut_trees & set(range(l, r + 1)))
                if remaining_trees < t:
                    valid = False
                    break
            
            if valid:
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(high)
    
    return results

if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        N, K = map(int, input().split())
        positions = list(map(int, input().split()))
        restrictions = [tuple(map(int, input().split())) for _ in range(K)]
        test_cases.append((N, K, positions, restrictions))
    
    results = solve_farm_problem(test_cases)
    for res in results:
        print(res)