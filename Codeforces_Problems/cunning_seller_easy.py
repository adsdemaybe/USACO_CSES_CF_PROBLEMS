def solve():
    # Read input
    t = int(input())

    sols = [0] * t
    for i in range(t):
        n = int(input())
        
        base_three_num = decimal_to_base3(n)
        total_cost = calc_cost(base_three_num)
        sols[i] = total_cost
        
    return sols

def calc_cost(base3_str):
    """Calculate total cost for a base 3 number string"""
    total_cost = 0
    for k in range(len(base3_str)):
        digit = int(base3_str[k])
        x = len(base3_str) - 1 - k  # position from right (0-indexed)
        cost = 3**(x+1) + x*(3**(x-1)) if x > 0 else 3
        total_cost += digit * cost
    return total_cost

def decimal_to_base3(n):
    if n == 0:
        return "0"
    
    result = ""
    while n:
        result = str(n % 3) + result
        n //= 3
    return result

def main():
    sols = solve()
    for i in range(len(sols)): # type: ignore
        print(int(sols[i])) # type: ignore

if __name__ == "__main__":
    main()