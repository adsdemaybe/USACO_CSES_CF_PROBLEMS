def main():
    for _ in range(int(input())):
        t = int(input())
        nums = list(map(int, input().strip().split()))
        status = False
        
        # Try all pairs (x, y) where x < y
        for i in range(t):
            if status:
                break
            x = nums[i]
            for j in range(i + 1, t):
                y = nums[j]
                remainder = y % x
                
                # Check if remainder is even
                if remainder % 2 == 0:
                    print(f"{x} {y}")
                    status = True
                    break
        
        if not status:
            print(-1)
            
main()