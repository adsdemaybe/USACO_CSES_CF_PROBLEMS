def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    y = int(x**0.5)
    return y * y == x

def int_cuberoot(x: int) -> int:
    # integer cube root (floor)
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid**3 <= x:
            low = mid + 1
        else:
            high = mid - 1
    return high

def uw_numerology(n: int):
    b = -1
    max_i = int_cuberoot(6 * n)
    for i in range(1, max_i + 1):
        denom = i * (i + 1) * (2 * i + 1)
        if (6 * n) % denom != 0:
            continue
        val = (6 * n) // denom
        if is_perfect_square(val):
            b = i
    if b != -1:
        a = int((6 * n // (b * (b + 1) * (2 * b + 1))) ** 0.5)
        print("YES")
        print(a, b)
    else:
        print("NO")

def main():
    n = int(input())
    uw_numerology(n)

if __name__ == "__main__":
    main()