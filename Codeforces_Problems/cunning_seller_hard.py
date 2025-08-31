def solve():
    t = int(input())

    sols = [0] * t
    for i in range(t):
        [n, max_num_deals] = list(map(int, (input().strip().split())))
        
        base_three_num = decimal_to_base3(n)
        total_cost = calc_cost(base_three_num, max_num_deals)
        sols[i] = total_cost
        
    return sols

def calc_cost(base3_str, max_num_deals):
    """base3_str is the least number of deals needed to buy n watermelons"""
    # Convert base3 string to list of digits (reverse order like C++)
    split = [int(d) for d in base3_str[::-1]]  # Reverse to match C++ order
    
    total_sum = sum(split)
    if max_num_deals < total_sum:
        return -1
    
    used = total_sum
    
    # For each position from highest to lowest (right to left in original base3)
    for i in range(len(split) - 1, 0, -1):
        # Binary search for maximum digits we can move from position i to i-1
        l = 0
        r = split[i]
        can = 0
        
        
        iteration = 1
        while l <= r:
            m = (l + r) // 2
            
            
            # Simulate the move to show what would happen
            temp_split = split[:]
            temp_split[i] -= m
            temp_split[i-1] += (m * 3)
            
            # Check if moving m digits is within deal limit
            new_used = used + (m * 3) - m
            
            if new_used <= max_num_deals:
                can = m
                l = m + 1
            else:
                r = m - 1
            
            iteration += 1
        
        
        # Apply the optimal move
        if can > 0:
            used += (can * 3) - can
            split[i] -= can
            split[i - 1] += (can * 3)
    
    # Calculate final cost
    ans = 0
    for i in range(len(split)):
        position_cost = cost_function(i)
        contribution = position_cost * split[i]
        ans += contribution
        print(f"Position {i}: {split[i]} digits × cost {position_cost} = {contribution}")
    
    print(f"Total cost: {ans}")
    return ans

def cost_function(p):
    """Calculate cost for position p (matches C++ cost function)"""
    if p == 0:
        return 3
    return (3 ** (p + 1)) + (p * (3 ** (p - 1)))

def calc_num_deals(base3_str):
    """Calculate number of deals for a base 3 number string"""
    num_deals = 0
    for k in range(len(base3_str)):
        num_deals += int(base3_str[k])
    return num_deals

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