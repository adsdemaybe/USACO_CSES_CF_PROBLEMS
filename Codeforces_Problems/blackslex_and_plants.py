def lsb(x: int) -> int:
    if x == 0:
        return 0
    return x & -x
