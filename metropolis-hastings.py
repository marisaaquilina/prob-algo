import random
from collections import Counter

num_sim = 10000
p = {0:.15, 1: .18, 2:.35, 3:.2, 4:.08, 5:.04} #Probability distribution
states_visited = []
curr_state = BoxModel([i for i in range(len(p))]).draw() #Random initial state

for i in range(num_sim):
    prop_state = ((curr_state - 1) % len(p)) if random.uniform(0, 1) < 0.5 else ((curr_state + 1) % len(p)) #Make random walk left or right
    if p[prop_state] > p[curr_state]: #If proposed state has higher prob, accept
        curr_state = prop_state
    else:
        acceptance_prob = p[prop_state] / p[curr_state] #I proposed state has lower prob, accept with prob of ratio
        if random.uniform(0, 1) < acceptance_prob:
            curr_state = prop_state
    states_visited.append(curr_state)
    
c  = Counter(states_visited)
total = sum(c.values(), 0.0)
for key in c:
    c[key] /= total
c # Show time spent in each state
