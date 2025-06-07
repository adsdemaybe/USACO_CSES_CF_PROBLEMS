with open("INPUT.in", "r") as f:
    input_data = f.read().strip().split()
T = int(input_data[0])
pos = 1
for _ in range(T):
    N = int(input_data[pos]); pos+=1
    cakes = list(map(int, input_data[pos:pos+N]))
    pos+=N

    total = sum(cakes)
    M = (N//2) + 1

    prefix = [0]*(N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + cakes[i]

    min_sub_block = float('inf')
    for start in range(N - M + 1):
        sub_sum = prefix[start+M] - prefix[start]
        if sub_sum < min_sub_block:
            min_sub_block = sub_sum

    B = min_sub_block
    E = total - B
    print(B, E)