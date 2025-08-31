# x is the number that is being repeated k times
# find if x is a prime

# if k is not one, then the answer is NO
# if x is not prime, then the answer is NO
# else the answer is YES
    
def is_valid(x, k):
    if k == 1:
        if x == 1:
            return False
        else: 
            return is_prime(x) 
    else: # if k != 1
        if x == 1:
            return is_prime(int("1" * k))
        else:
            return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n, k = map(int, input().split())
    print("YES" if is_valid(n, k) else "NO")