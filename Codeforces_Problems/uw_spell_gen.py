import math

def main():
    for _ in range(int(input())):
        print(uw_spell_gen(int(input())))

def uw_spell_gen(r):
    count = 0
    cost = 0
    for _ in range(math.floor(math.log10(r))+1):
        cost += r%10 * 2 ** count
        count += 1
        r = r // 10
    return cost

main()