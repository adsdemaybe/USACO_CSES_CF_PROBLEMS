def main():
    t = int(input())
    res_arr = []
    for _ in range(t):
        n, targ = map(int, input().split())
        arr = list(map(int, input().split()))
        result = mex_rose(n, targ, arr)
        res_arr.append(result)
    print(*res_arr, sep="\n")

def mex_rose(n, targ, arr):
    exists = {i: 0 for i, _ in enumerate(range(targ))}
    ops = 0
    for i in arr:
        if i in exists:
            exists.pop(i)
        elif i == targ:
            ops += 1
            
    # exists = [0] * (targ)
    # set_arr = set(arr)
    # for i in range(len(exists)):
    #     if i in set_arr:
    #         exists[i] = 1
    #         set_arr.remove(i)
    
    return max(arr.count(targ), exists.count(0))

if __name__ == "__main__":
    main()