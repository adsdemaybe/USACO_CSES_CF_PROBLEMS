def main():
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().strip().split()))
        target_x = int(input())
        if target_x <= max(nums) and target_x >= min(nums):
            print("yes")
        else:
            print("no")
            
main()