t = input()
for i in range(int(t)):
    n = int(input())
    a = list(input().strip()) # change this one
    m  = int(input())
    b = list(input().strip()) 
    order = list(input().strip())
    
    for i in range(len(order)):
        if(order[i] == 'D'):
            a.append(b.pop(0))
        elif(order[i] == 'V'):
            a.insert(0, b.pop(0))
    print("".join(a))