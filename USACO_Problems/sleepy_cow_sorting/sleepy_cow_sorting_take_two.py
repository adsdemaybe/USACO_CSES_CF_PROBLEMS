import sys

# 1 2 4 3
# 2 4 1 3
# 4 1 2 3
# 1 2 3 4

# 1 3 4 2
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4

def main():
    sys.stdin = open("sleepy.in", 'r')
    sys.stdout = open("sleepy.out", 'w')
    
    N = sys.stdin.readline()
    cows = list(map(int, sys.stdin.readline()))
    