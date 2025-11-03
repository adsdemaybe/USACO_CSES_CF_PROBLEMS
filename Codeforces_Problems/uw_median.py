import sys

def main():
    t = input()
    for _ in range(int(t)):
        n = int(input())
        arr = list(map(int, input().split()))
    
def uw_median(arr, n):
    curr_med = arr[0]//2
    print(curr_med)
    for i in range(1, n):
        if(i%2 == 1):
            curr_med = arr[i] - curr_med
        elif(i%2 == 0):
            if():
    return