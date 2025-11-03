def solve(k):
    if k < 10:
        return k
    
    digit = 1
    start = 1
    count = 9
    while k > digit * count:
        k -= digit * count
        digit += 1
        count *= 10
        start *= 10
    number = start + (k - 1) // digit
    
    sum_digits = (number - 1)*(number) // 2
    sum_digits += sum(map(int, list(str(number)[:(k - 1) % digit])))
    
    return sum_digits

def main():
    for _ in range(int(input())):
        print(solve(int(input())))

if __name__ == "__main__":
    main()