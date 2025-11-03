import math

# 1. process MY TEAMS statistics
# 2. process all submissions from OTHER TEAM
# 3. add accepted penalty to OTHER TEAM total penalty
# 4. add rejected penalty to pd_list_OTHER_TEAM
# -- if they havent solved as many questions or they have and their penalty is higher than ours: we win (ret -1)
# -- else, do the following
# 5. add earliest penalty to each problem in pd_list_OTHER_TEAM
# 6. pick the least penalty for the remaining problems (to tie with MY TEAM)
            
def main():
    for _ in range(int(input())):
        num_probs, MT_solved, MT_penalty = list(map(int, input().strip().split()))
        OT_num_submissions = int(input())
        stats = []
        for _ in range(OT_num_submissions):
            curr_sub = list(input().strip().split())
            OT_time, OT_problem, OT_status = int(curr_sub[0]), curr_sub[1], curr_sub[2]
            stats.append((OT_time, OT_problem, OT_status))
        
        print(predict(stats, MT_solved, MT_penalty))
    
def predict(stats:dict, MT_solved, MT_penalty):
    OT_total_penalty = 0
    OT_solved = 0
    solved_problems = set()
    rejected_count = {}
    pending_problems = {}
    
    for OT_time, OT_problem, OT_status in stats:
        if OT_status == "ac":
            penalty = OT_time + rejected_count.get(OT_problem, 0) * 20
            OT_total_penalty += penalty
            OT_solved += 1
            solved_problems.add(OT_problem)
            if OT_problem in pending_problems:
                pending_problems.pop(OT_problem)
        elif OT_status == "rj":
            if OT_problem in rejected_count:
                rejected_count[OT_problem] += 1
            else:
                rejected_count[OT_problem] = 1
        elif OT_status == "pd":
            if OT_problem not in pending_problems:
                pending_problems[OT_problem] = OT_time + rejected_count.get(OT_problem, 0) * 20
    
    if OT_solved > MT_solved or (OT_solved == MT_solved and OT_total_penalty < MT_penalty):
        return 0
    
    solved = 0
    for penalty in sorted(pending_problems.values()):
        OT_total_penalty += penalty
        OT_solved += 1
        solved += 1
        if OT_solved > MT_solved or (OT_solved == MT_solved and OT_total_penalty < MT_penalty):
            return solved
    return -1
        
main()