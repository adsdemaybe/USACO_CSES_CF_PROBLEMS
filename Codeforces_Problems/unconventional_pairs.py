def main():
    t = int(input())
    res_list = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = uncon_pairs(n, arr)
        res_list.append(result)
    print(*res_list, sep="\n")

def uncon_pairs(n, arr):
    arr.sort()
    maximum_diff = -1
    for i in range(0,n//2):
        maximum_diff = max(maximum_diff, abs(arr[2*i] - arr[2*i + 1]))
    return maximum_diff

if __name__ == "__main__":
    main()