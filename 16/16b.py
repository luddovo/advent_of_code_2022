#!/usr/bin/env python3

import parse, itertools

TICKS = 26

# read input

neighbors = {}

rates = {}

for line in open('input.txt'):
    d = parse.parse("Valve {name} has flow rate={rate}; tunnels lead to valves {valves}",line.strip())
    neighbors[d['name']] = [x.strip() for x in d['valves'].split(',')]
    rates[d['name']] = int(d['rate'])

# print(neighbors, rates)

# pick only valves that open (they are 15)

openable = [k for k in rates if rates[k] > 0]

# find the shortest path between each pair of openable valves

def bfs(pair):
    s, e = pair
    
    # enque start pos as first path
    q = [[s]]

    # empty set of visited nodes
    visited = set([])
    
    while q:

        # pop the first path from the queue
        path = q.pop(0)

        # get the last node from the path
        node = path[-1]

        # if node has not been visited yet, process it and enqueue neighbors
        if node not in visited:

            # visit neighbors
            for n in neighbors[node]:

                    # check if reached the destination
                    if n == e:
                        return path

                    # enqueue path for this node
                    new_path = path[:]
                    new_path.append(n)
                    q.append(new_path)

            visited.add(node)


paths = {}

for pair in itertools.permutations(openable, 2):
    paths[pair] = len(bfs(pair))

# add paths from AA

for o in openable:
    p = ('AA', o)
    paths[p] = len(bfs(p))

print(paths)

# dict of max_flow in unique trail, keys will be frozensets
maxflows = {}

def dfs(node, open_valves, flow, ticks):
    global max_flow, trails

    # open valve
    if node != 'AA': open_valves.append(node)
    # add to total flow
    flow += (TICKS - ticks) * rates[node]

    # visit neigbors

    for n in openable:
        if n not in open_valves:
            l = paths[(node,n)]

            if ticks + l + 1 > TICKS:
                # end this branch
                fs = frozenset(open_valves)
                if fs not in maxflows:
                    maxflows[fs] = flow
                else:
                    maxflows[fs] = max(maxflows[fs], flow)
            else:
                # go to neighbor
                dfs(n, open_valves[:], flow, ticks + l + 1)

# get all possible distinct combinations of trails, and max flow for each

dfs("AA", [], 0, 0)

# make pairs, check if they are complementary and get max score

max_flow = 0

for pair in itertools.combinations(maxflows, 2):
    a, b = pair
    
    
    # check if complementary
    if len(a.union(b)) == len(a) + len(b):
        #print(a, maxflows[a], b, maxflows[b])
        max_flow = max(maxflows[a] + maxflows[b], max_flow)
 
print(max_flow)