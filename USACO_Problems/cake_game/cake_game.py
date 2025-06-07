"""
Input - [_, _, _, _, _, _]
1 -> Find Max Adjacent Sum 
2 -> Find Max for Bessie
3 -> Combine everything else
4 -> Put into Stash (Max Edge)
5 -> Repeat 3 and 4.
"""

cakes_order = [10, 20, 30, 40]
adj_sum = [0]
ellie_stach = 0
for i in range(1, len(cakes_order)):
    adj_sum.append(cakes_order[i] + cakes_order[i - 1])
    
combined_ind = adj_sum.index(max(adj_sum))
cakes_order[combined_ind] = max(adj_sum)
cakes_order.pop(combined_ind - 1)
adj_sum.pop(combined_ind - 1)

ellie_best_cake = 