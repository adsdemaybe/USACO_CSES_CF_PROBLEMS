import sys

def main():
    sys.stdin = open("div7.in", 'r')
    sys.stdout = open("div7.out", 'w')
    n = int(input())
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + int(input()))%7
        # prefix_sum.append((prefix_sum[-1] + int(input()))%7)
    
    prefix_sum.pop(0)
    max_length = 0
    for i in range(6):
        if(i in prefix_sum):
            first_occur = prefix_sum.index(i)
            last_occur = len(prefix_sum) - prefix_sum[::-1].index(i) - 1
            max_length = max(last_occur - first_occur, max_length)
        
    print(max_length) 

if "__main__" == __name__:
    main()