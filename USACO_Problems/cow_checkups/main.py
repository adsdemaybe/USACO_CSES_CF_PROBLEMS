input_seq = [1,2,3,4,5,6,3,4]
pref_sum = [0]
# pref_sum = [0, 1, 3, 6, 10, 15, 21, 24, 28] N = 8
for i in range(1, len(input_seq)):
    pref_sum.append(pref_sum[i - 1] + input_seq[i])
    
longest = -1
shortest = 99999
for i in range(len(pref_sum)):
    for j in range(i + 1, len(pref_sum)):
        if(pref_sum[j] - pref_sum[i] == 24):
            print(j - 1)
            longest = max(longest, j - i)
            shortest = min(shortest, j - i)
print(longest)
print(shortest)