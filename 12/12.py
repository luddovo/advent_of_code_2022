#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2000)

m = []

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

endx = 0
endy = 0

# BFS algorithm for shortest path
def climb(posx, posy):

    # enque start pos as first path
    q = [[(posx, posy)]]

    # empty list of visited nodes
    visited = set([])
    
    while q:

        # pop the first path from the queue
        path = q.pop(0)

        # get the last node from the path
        posx, posy = path[-1]

        # if node has not been visited yet, process it and enqueue neighbors
        if (posx, posy) not in visited:

            # try all four directions
            for x, y in dirs:
                newx = posx + x
                newy = posy + y
                if ( 0 <= newx < len(m[0]) and 
                    0 <= newy and newy < len(m) and
                    (newx, newy) not in visited and
                    ord(m[newy][newx]) - ord(m[posy][posx]) <= 1):

                    # process neighbor

                    # check if reached the destination
                    if newx == endx and newy == endy:
                        return path

                    # enqueue path for this node
                    new_path = path[:]
                    new_path.append((newx, newy))
                    q.append(new_path)

            visited.add((posx, posy))
    
# load map
for line in open('input.txt'):
    line = line.strip()
    r = []
    for c in line:
        r.append(c)
    m.append(r)

# find start pos
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "S":
            m[y][x] = 'a'
            posx = x
            posy = y
            break
    else:
        continue
    break

# find end pos
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "E":
            m[y][x] = 'z'
            endx = x
            endy = y
            break
    else:
        continue
    break

print(f"Starting at ({posx},{posy}) going to ({endx},{endy}).")

# run
print("Part 1: ", len(climb(posx, posy)))

# Part II

trails = []

for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == "a":
            res = climb(x,y)
            if res:
                trails.append(len(res))    
print("Part 2: ", min(trails))