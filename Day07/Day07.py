import numpy as np
test_input = """16,1,2,0,4,2,7,1,2,14"""

with open("input") as fh:
    test_input = fh.read().strip()
pos = map(int, test_input.split(","))
inputty = np.fromiter(pos, dtype=int)
cost = (np.inf, 0)
cost_p2 = (np.inf, 0)
for position in range(max(inputty+1)):
    new_costs = abs(inputty - position)
    new_cost_p1 = sum(new_costs)
    cost = (new_cost_p1, position) if new_cost_p1 < cost[0] else cost
    new_cost_p2 = sum(map(lambda x: sum(range(x+1)), new_costs))
    cost_p2 = (new_cost_p2, position) if new_cost_p2 < cost_p2[0] else cost_p2
    # new_cost_p2 = np.sum()

print(cost[0])
print(cost_p2[0])