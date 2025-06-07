import sys

class cow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return repr((self.x, self.y))

def main():
    n = int(input())
    
    cows = []
    for _ in range(n):
        xy_inputs = list(map(int, input().strip().split()))
        cows.append(cow(xy_inputs[0], xy_inputs[1]))
    
    # Compress Cow Coords
    cows.sort(key=lambda cow: cow.x)
    ind = 1
    for cow_i in cows:
        cow_i.x = ind
        ind += 1
        
    max_x = ind
    
    cows.sort(key=lambda cow: cow.y)
    ind = 1
    for cow_i in cows:
        cow_i.y = ind
        ind += 1
    
    max_y = ind
    
    locs = [[0 for i in range(max_x)] for i in range(max_y)]
    for cow_ind in range(n):
        locs[cows[cow_ind].y][cows[cow_ind].x] = 1
    
    # Make prefix sum
    
    pref_sum = [row.copy() for row in locs]
    for i in range(1, max_y):
        for j in range(1, max_x):
            pref_sum[i][j] += pref_sum[i - 1][j] + pref_sum[i][j - 1] - pref_sum[i - 1][j - 1]
    
    # Count Cows Above and Below
    cows.sort(key=lambda cow: cow.x)
    count = n + 1
    for anchor_ind in range(n):
        for target_ind in range(anchor_ind + 1, n):
            
            left_x = cows[anchor_ind].x 
            right_x = cows[target_ind].x
            bott_y = max(cows[anchor_ind].y, cows[target_ind].y)
            top_y = min(cows[anchor_ind].y, cows[target_ind].y)
            
            top_cows_count = pref_sum[top_y][right_x] - pref_sum[top_y][left_x-1]
            bot_cows_count = pref_sum[max_y - 1][right_x] - pref_sum[max_y - 1][left_x-1] - pref_sum[bott_y - 1][right_x] + pref_sum[bott_y - 1][left_x -1]
            count += (top_cows_count) * (bot_cows_count)
    print(count)
main()