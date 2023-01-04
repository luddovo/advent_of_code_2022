#!/usr/bin/env python3

points = set([])

# read data

for y, line in enumerate(open('input.txt')):
    for x, c in enumerate(line):
        if c == "#": points.add( (x,y) )


cnt = 0

# 0 - north 1 -south 2- west 3 - east

moves = [ (0,-1), (0,1), (-1,0), (1,0)]

rounds = 0

while True:

    rounds += 1


    proposals = {}
    
    for p in points:
        x, y = p
        d = [False for i in range(4)]
        # check north
        d[0] = (x-1, y-1) in points or (x, y-1) in points or (x+1, y-1) in points
        # check south
        d[1] = (x-1, y+1) in points or (x, y+1) in points or (x+1, y+1) in points
        # check west
        d[2] = (x-1, y-1) in points or (x-1, y) in points or (x-1, y+1) in points
        # check east
        d[3] = (x+1, y-1) in points or (x+1, y) in points or (x+1, y+1) in points

        if not any(d):
            # no neightbors
            continue

        for i in range(4):
            s = (cnt + i) % 4
            if not d[s]:
                new_p = ( x + moves[s][0], y + moves[s][1] )
                if not new_p in proposals:
                    proposals[new_p] = [p]
                else:    
                    proposals[new_p].append(p)
                break

    nomoves = True
    # process proposals
    for p in proposals:
        if len(proposals[p]) == 1:
            points.add(p)
            points.remove(proposals[p][0])
            nomoves = False

    if nomoves: break

    cnt = (cnt + 1) % 4

# count empty squares
print(rounds)
