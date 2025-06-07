def solve():
    import sys

    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    arr = list(map(int, input_data[1:]))
    prefixDistinct = [0] * (N + 1)
    lastOcc = [0] * (N + 1)  
    countDistinct = 0

    for i in range(1, N + 1):
        x = arr[i - 1]
        if lastOcc[x] == 0:
            countDistinct += 1
        lastOcc[x] = i
        prefixDistinct[i] = countDistinct

    positions = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        val = arr[i - 1]
        positions[val].append(i)
        
    answer = 0
    for y in range(1, N + 1):
        if len(positions[y]) >= 2:
            second_last = positions[y][-2] 
            if second_last > 1:
                distinct_before = prefixDistinct[second_last - 1]
                if positions[y][0] <= second_last - 1:
                    contribution = distinct_before - 1
                else:
                    contribution = distinct_before

                if contribution < 0:
                    contribution = 0
                answer += contribution

    print(answer)

solve()