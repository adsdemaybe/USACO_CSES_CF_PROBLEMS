import sys

def main():
    
    sys.stdin = open("hps.in", 'r')
    sys.stdout = open("hps.out", 'w')

    n = int(input())
    current_count = {"H":0, "P":0, "S":0}
    actions_fj = []
    for i in range(n):
        actions_fj.append(input())
    
    prefix_sums_left = []
    for i in range(n):
        current_count[actions_fj[i]] += 1
        prefix_sums_left.append(list(current_count.values()))
    
    current_count = {"H":0, "P":0, "S":0}
    prefix_sums_right = [0] * n
    for i in range(n - 1, -1, -1):
        current_count[actions_fj[i]] += 1
        prefix_sums_right[i] = (list(current_count.values()))
        
    maximum_wins = max(prefix_sums_left[n - 1])
    for i in range(n - 1):
        maximum_wins = max(maximum_wins, max(prefix_sums_left[i]) + max(prefix_sums_right[i + 1]))
    print(maximum_wins)
    return maximum_wins

if "__main__" == __name__:
    main()
    
#COMPLETE