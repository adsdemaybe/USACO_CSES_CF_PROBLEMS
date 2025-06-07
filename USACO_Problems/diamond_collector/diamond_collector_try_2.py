import sys

def main():
    n, k = list(map(int, input().strip("\n").split()))
    diamonds = []
    for _ in range(n):
        diamonds.append(int(input().strip("\n")))
    diamonds.sort()
    
    counts = []
    pointer_ind_one = 0
    pointer_ind_two = 1
    for i in range(n):
        