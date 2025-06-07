import sys

def main(): 
    sys.stdin = open('USACO_Problems/painting_the_barn/paintbarn.in', 'r')
    sys.stdout = open('USACO_Problems/painting_the_barn/paintbarn.out', 'w')
    n, k = map(int, input().strip().split())
    grid = [[0 for i in range(201)] for i in range(201)]
    
    for _ in range(n):
        max_x = -1
        min_x = 2000
        max_y = -1
        min_y = 2000
        
        x1, y1, x2, y2 = list(map(int, input().split()))
        x1 += 1
        x2 += 1
        y1 += 1
        y2 += 1
        
        max_x = max(max_x, x1, x2)
        min_x = min(min_x, x1, x2)
        max_y = max(max_y, y1, y2)
        max_y = max(min_y, y1, y2)
        
        grid[x1][y1] += 1
        grid[x1][y2] += -1
        grid[x2][y2] += 1 
        grid[x2][y1] += -1
    
    
    
    # 2D Prefix-Sum
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            grid[i][j] += grid[i][j - 1] + grid[i - 1][j] - grid[i - 1][j - 1]
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == k: count += 1


    print(count)
    

if __name__ == "__main__":
    main()