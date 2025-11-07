def main():
    for _ in range(int(input())):
        length = int(input())
        [s, t] = input().strip().split()
        if("".join(sorted(s)) == "".join(sorted(t))):
            print("YES")
        else:
            print("NO")
    
main()