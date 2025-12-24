for i in range(int(input())):
    arr_len = int(input())
    arr = list(map(int, input().strip().split()))
    
    sum = 0
    for i in range(arr_len - 1):
        sum += abs(arr[i] - arr[i + 1])
        
    best = sum
    
    best = min(best, sum - abs(arr[0] - arr[1]))
    best = min(best, sum - abs(arr[arr_len-2] - arr[arr_len-1]))

    for k in range(1, arr_len - 1):
        best = min(best, sum - abs(arr[k - 1] - arr[k]) - abs(arr[k] - arr[k + 1]) + abs(arr[k - 1] - arr[k + 1]))
    
    print(best)