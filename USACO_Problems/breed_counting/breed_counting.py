import sys

class count:
    
    def __init__(self, h, g, j):
        self.h = h
        self.g = g
        self.j = j
    
def main():
    sys.stdin = open("bcount.in", "r")
    sys.stdout = open("bcount.out", "w")
    
    n, q = list(map(int, input().strip("\n").split()))
    breed_list = [count(0, 0, 0)] * (n + 1)
    
    for i in range(1, n + 1):
        curr = int(input().strip("\n"))
        if(curr == 1):
            breed_list[i] = count(breed_list[i - 1].h + 1, breed_list[i - 1].g, breed_list[i - 1].j)
        elif(curr == 2):
            breed_list[i] = count(breed_list[i - 1].h , breed_list[i - 1].g + 1, breed_list[i - 1].j)
        elif(curr == 3):
            breed_list[i] = count(breed_list[i - 1].h, breed_list[i - 1].g, breed_list[i - 1].j + 1)
    
    for _ in range(q):
        f, t = map(int, input().strip().split())
        print(str(breed_list[t].h - breed_list[f - 1].h) + " " + str(breed_list[t].g - breed_list[f - 1].g) + " " + str(breed_list[t].j - breed_list[f - 1].j))
        
main()