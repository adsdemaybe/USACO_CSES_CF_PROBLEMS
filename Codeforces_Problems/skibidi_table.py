# Given n, the table is of size 2^n x 2^n
# Break the table into 2x2 pieces, and fill with recursion
# The table is filled in this way: first fill the top left, bottom right, bottom left, and top right.

# Queries are given as (x, y) where you need to give the number at (x, y)
# Queries are given a single number k, where you need to return the coordinate location of n as (x, y)
# Return while recursion occurs

def find_quadrant(k, n, top_x, top_y, bottom_x, bottom_y):
    if n == 1:
        cells = [
            (top_x, top_y),       # top-left (1)
            (bottom_x, bottom_y), # bottom-right (2)
            (bottom_x, top_y),    # bottom-left (3)
            (top_x, bottom_y)     # top-right (4)
        ]
        return str(cells[k - 1][0] + 1) + " " + str(cells[k - 1][1] + 1)
    
    size = 2**(n-1)
    cells_per_quadrant = size * size
    
    mid_x = (top_x + bottom_x) // 2
    mid_y = (top_y + bottom_y) // 2
    
    if k <= cells_per_quadrant:
        # Top-left quadrant
        return find_quadrant(k, n-1, top_x, top_y, mid_x, mid_y)
    elif k <= 2 * cells_per_quadrant:
        # Bottom-right quadrant
        k_new = k - cells_per_quadrant
        return find_quadrant(k_new, n-1, mid_x + 1, mid_y + 1, bottom_x, bottom_y)
    elif k <= 3 * cells_per_quadrant:
        # Bottom-left quadrant
        k_new = k - 2 * cells_per_quadrant
        return find_quadrant(k_new, n-1, mid_x + 1, top_y, bottom_x, mid_y)
    else:
        # Top-right quadrant
        k_new = k - 3 * cells_per_quadrant
        return find_quadrant(k_new, n-1, top_x, mid_y + 1, mid_x, bottom_y)

def find_k(n, targ_x, targ_y, top_x, top_y, bottom_x, bottom_y):
    if n == 1:
        if targ_x == top_x and targ_y == top_y:           # top-left
            return 1
        elif targ_x == bottom_x and targ_y == bottom_y:   # bottom-right
            return 2
        elif targ_x == bottom_x and targ_y == top_y:      # bottom-left
            return 3
        else:                                             # top-right
            return 4

    size = 2**(n-1)
    cells_per_quadrant = size * size

    mid_x = (top_x + bottom_x) // 2
    mid_y = (top_y + bottom_y) // 2

    if targ_x <= mid_x and targ_y <= mid_y:
        # Top-left quadrant
        return find_k(n-1, targ_x, targ_y, top_x, top_y, mid_x, mid_y)
    elif targ_x > mid_x and targ_y > mid_y:
        # Bottom-right quadrant (adjust boundaries only)
        return cells_per_quadrant + find_k(n-1, targ_x, targ_y, mid_x + 1, mid_y + 1, bottom_x, bottom_y)
    elif targ_x > mid_x and targ_y <= mid_y:
        # Bottom-left quadrant (adjust boundaries only)
        return 2 * cells_per_quadrant + find_k(n-1, targ_x, targ_y, mid_x + 1, top_y, bottom_x, mid_y)
    else:
        # Top-right quadrant (adjust boundaries only)
        return 3 * cells_per_quadrant + find_k(n-1, targ_x, targ_y, top_x, mid_y + 1, mid_x, bottom_y)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for _ in range(q):
        query = input().split()
        if(query[0] == "->"):
            print(find_k(n, int(query[1]) - 1, int(query[2]) - 1, 0, 0, 2**n - 1, 2**n - 1))
        elif(query[0] == "<-"):
            print(find_quadrant(int(query[1]), n, 0, 0, 2**n - 1, 2**n - 1))