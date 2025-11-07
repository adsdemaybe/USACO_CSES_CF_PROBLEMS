for _ in range(int(input())):
    inp = list(map(int, input().strip().split()))
    status = False
    for i in range(1, 4):
        if(inp[i] != inp[i-1]):
            print("no")
            status = True
            break
    if not status:
        print("yes")