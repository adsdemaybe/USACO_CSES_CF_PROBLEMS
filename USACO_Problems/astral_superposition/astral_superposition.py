import sys

def solve_single_case(N, A, B, image):
    forced = [[False]*N for _ in range(N)]
    usedAsShifter = [[False]*N for _ in range(N)]

    forced_count = 0

    def force_cell(r, c):
        nonlocal forced_count
        if not forced[r][c]:
            forced[r][c] = True
            forced_count += 1

    for i in range(N):
        for j in range(N):
            if image[i][j] == 'B':
                if i - B < 0 or j - A < 0:
                    return -1  
                r, c = i - B, j - A
                if usedAsShifter[r][c]:
                    return -1

                usedAsShifter[r][c] = True
                force_cell(i, j)      
                force_cell(r, c)      

    for i in range(N):
        for j in range(N):
            if image[i][j] == 'G':
                costG1 = 0 if forced[i][j] else 1
                costG2 = float('inf')
                if i - B >= 0 and j - A >= 0:
                    r, c = i - B, j - A
                    if not usedAsShifter[r][c]:
                        costG2 = 0 if forced[r][c] else 1

                if costG1 <= costG2:
                    if costG1 == 1:
                        force_cell(i, j)
                else:
                    r, c = i - B, j - A
                    force_cell(r, c)
                    usedAsShifter[r][c] = True

                if costG1 == float('inf') and costG2 == float('inf'):
                    return -1

    for i in range(N):
        for j in range(N):
            if image[i][j] == 'W':
                if forced[i][j]:
                    return -1
                r, c = i - B, j - A
                if 0 <= r < N and 0 <= c < N:
                    if forced[r][c] and usedAsShifter[r][c]:
                        return -1
    return forced_count


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N, A, B = map(int, input().split())
        image = [input().strip() for _ in range(N)]
        ans.append(solve_single_case(N, A, B, image))
    
    for a in ans:
        print(a)
        
main()