import bisect
from collections import defaultdict

def solve():
    import sys
    input_data = sys.stdin.read().split()
    index = 0
    count = int(input_data[index])
    index += 1
    list_a = list(map(int, input_data[index:index + count]))
    index += count
    list_b = list(map(int, input_data[index:index + count]))
    index += count
    total_pairs = count * (count + 1) // 2  

    result_one = 0
    for pos in range(count):
        if list_a[pos] == list_b[pos]:
            included_count = (pos + 1) * (count - pos)
            result_one += (total_pairs - included_count)

    dict_a = defaultdict(list)
    for idx in range(count):
        dict_a[list_a[idx]].append(idx + 1)  
    dict_b = defaultdict(list)
    for idx in range(count):
        dict_b[list_b[idx]].append(idx + 1)  

    result_two = 0
    unique_values = set(dict_a.keys()).union(set(dict_b.keys()))
    for value in unique_values:
        indices_b = dict_b.get(value, [])  
        indices_a = dict_a.get(value, [])  
        if not indices_b or not indices_a:
            continue 

        sorted_b = sorted(indices_b)
        sorted_a = sorted(indices_a)
        len_b = len(sorted_b)
        len_a = len(sorted_a)

        prefix_sum_a = [0]
        for num in sorted_a:
            prefix_sum_a.append(prefix_sum_a[-1] + num)

        min_sum = 0
        count_c = 0  
        for b_value in sorted_b:
            max_a_allowed = (count + 1) - b_value  
            if max_a_allowed < 1:
                continue
            k = bisect.bisect_right(sorted_a, max_a_allowed)
            count_c += k  
            if k == 0:
                continue
            m = bisect.bisect_right(sorted_a, b_value)
            m = min(m, k)
            sum_j_part = prefix_sum_a[m]
            count_i_part = k - m
            min_sum += sum_j_part + b_value * count_i_part

        max_sum_all = 0
        for b_value in sorted_b:
            pos = bisect.bisect_left(sorted_a, b_value)
            sum_less = pos * b_value  
            sum_greater = prefix_sum_a[-1] - prefix_sum_a[pos] 
            max_sum_all += sum_less + sum_greater

        total_max_sum = (count + 1) * len_b * len_a - max_sum_all
        max_min_sum = 0
        for b_value in sorted_b:
            max_a_allowed = (count + 1) - b_value
            if max_a_allowed < 1:
                continue
            k = bisect.bisect_right(sorted_a, max_a_allowed)
            if k == 0:
                continue
            m = bisect.bisect_right(sorted_a, b_value)
            m = min(m, k)
            sum_i_part = b_value * m
            sum_j_part = prefix_sum_a[k] - prefix_sum_a[m]
            max_min_sum += sum_i_part + sum_j_part

        max_min_result = (count + 1) * count_c - max_min_sum
        max_result = total_max_sum - max_min_result

        result_two += min_sum + max_result

    print(result_one + result_two)

solve()