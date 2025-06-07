N, Q = map(int, input().split())
original_bool_list = input().strip("\n").split()
answer_string = ""

def parse(list):
    for i in range(len(list)):
        if(list[i] == "false"):
            list[i] = False
        elif (list[i] == "true"):
            list[i] = True
    return list

original_bool_list = parse(original_bool_list)

def operate(bool_A, operator, bool_B):
    if(operator == "and"):
        return bool_A and bool_B
    elif(operator == "or"):
        return bool_A or bool_B

def replace(list, f: int, t: int, change):
    del list[f:t+1]
    list.insert(f, change)
    return list

def solve(list):
    i = len(list) - 2
    while(i > 0):
        if(list[i] == "and"):
            list = replace(list, i-1, i+1, operate(list[i-1], list[i], list[i+1]))
        i -= 2
        
    i = len(list) - 2
    while(i > 0):
        list = replace(list, i-1, i+1, operate(list[i-1], list[i], list[i+1]))
        i -= 2
    return list
    

for _ in range(Q):
    copy_list_A = original_bool_list.copy()
    copy_list_B = original_bool_list.copy()
    f, t, change = input().split() # [bool, operand, bool, operand, bool]
    f = int(f) - 1
    t = int(t) - 1
    if(change == "true"):
        change = True
    elif(change == "false"):
        change = False
        
    change_A = solve(replace(copy_list_A, f, t, True))[0]
    change_B = solve(replace(copy_list_B, f, t, False))[0]
    
    if(change_A == change or change_B == change):
        answer_string += "Y"
    else:
        answer_string += "N"
        
print(answer_string)


# print(solve(parse(["false", "or", "true", "and", "false", "and", "false", "and", "true", "or", "true", "and", "false"])))