import sys

def main():
    # sys.stdout = open("taming.out", 'w')
    # sys.stdin =  open("taming.in", 'r')
    
    n = int(input().strip("\n")) - 1
    uncertain_list = list(map(int, input().strip("\n").split()))
    uncertain_list[0] = 0
    
    current_count = -1
    for i in range(n, -1, -1):
        if uncertain_list[i] != -1:
            current_count = uncertain_list[i]
        elif uncertain_list[i] == -1 and current_count != -1:
            current_count -= 1
            uncertain_list[i] = current_count
        elif current_count != -1 and uncertain_list[i] > current_count:
            print(-1)
            return
    
    certain_breakouts = uncertain_list.count(0)
    uncertain_breakouts = uncertain_list.count(-1)
    
    print(str(certain_breakouts) + " " + str(certain_breakouts + uncertain_breakouts))

main()