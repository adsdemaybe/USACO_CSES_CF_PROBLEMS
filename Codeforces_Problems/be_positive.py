def main(): 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(be_positive(arr))
    

def be_positive(arr):
    ops = arr.count(0) + (2 if arr.count(-1) % 2 == 1 else 0)
    return ops

if __name__ == "__main__":
    main()