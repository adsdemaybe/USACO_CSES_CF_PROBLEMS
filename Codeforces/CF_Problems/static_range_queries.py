import sys

n, q = list(map(int, input().split()))
changes = []
for _ in range(n):
    L, R, addend = list(map(int, input().split()))
    L += 1
    R += 1
    changes.append([L, +addend, -1]) # delta[L] += addend
    changes.append([R, -addend, -1]) # delta[R + 1] += -addend

for query_index in range(q):
    L, R = list(map(int, input().split()))
    L += 1
    R += 1
    changes.append([L - 1, 0, query_index, -1])
    changes.append([R - 1, 0, query_index, +1])

changes.sort(key = lambda x: [x[0], x[2]])

prev_sum = 0
prev_pref_sum = 0
prev_index = 0
answers = [0] * q
for change in changes:
    index = change[0]
    sum = change[1] + prev_sum
    pref_sum = sum + prev_pref_sum + prev_sum * (index - 1 - prev_index)
    prev_sum = sum
    prev_pref_sum = pref_sum
    prev_index = index
    if change[2] != -1:
        query_index = change[2]
        answers[query_index] += change[3] * pref_sum


for answer in answers:
    print(answer)
