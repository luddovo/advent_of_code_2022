#!/usr/bin/env python3

import math, copy

# read data
data = []
for line in open('input.txt'):
    row = []
    for c in line.strip():
        row.append([c] if c != '.' else [])
    data.append(row)

for row in data:
    for c in row:
        if not c:
            print(".", end='')
        elif len(c) > 1:
            print("2", end='')
        else:
            print(c[0], end='')
    print()
print()


# empty board
empty = copy.deepcopy(data)
for y in range(len(empty)):
    for x in range(len(empty[y])):
        if empty[y][x] and empty[y][x][0] != '#':
            empty[y][x] = []

for row in empty:
    for c in row:
        if not c:
            print(".", end='')
        elif len(c) > 1:
            print("2", end='')
        else:
            print(c[0], end='')
    print()
print()

# find dimensions 
h = len(data)
w = max(len(r) for r in data)

# calculate number of states
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

n_states = lcm(w - 2, h - 2)

print(w, h, n_states)

states = []
# pre-compute states
for s in range(n_states):

    states.append(data)

    # next state empty board
    next_data = copy.deepcopy(empty)

    # compute next state
    for y in range(len(data)):
        for x in range(len(data[y])):
            for c in data[y][x]:
                if c != '#':
                    nx = x
                    ny = y
                    if   c == '>':
                        nx += 1
                    elif c == '<':
                        nx -= 1
                    elif c == '^':
                        ny -= 1
                    elif c == 'v':
                        ny += 1

                    # (x - 1) % (w - 2) + 1
                    # (y - 1) % (h - 2) + 1

                    #print(y , x, c, "next", (ny - 1) % (h - 2) + 1, (nx - 1) % (w - 2) + 1)

                    next_data[(ny - 1) % (h - 2) + 1][(nx - 1) % (w - 2) + 1].append(c)

    data = next_data

for s in states:
    for row in s:
        for c in row:
            if not c:
                print(".", end='')
            elif len(c) > 1:
                print("2", end='')
            else:
                print(c[0], end='')
        print()
    print()

# bfs

pos = (1,0)

visited = set([])

q = [[pos]]

while q:

    path = q.pop(0)

    pos = path[-1]

    cycle = (len(path) - 1) % n_states

    if (pos, cycle) not in visited:
        if pos == (w - 2, h - 1):
            break
        x, y = pos
        if len(path) == 1:
            # at the beginning canonly stay or go down
            moves = [(0,0), (0,1)]
        else:
            moves = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in moves:
            if not states[cycle][y+dy][x+dx]:
                new_path = path[:]
                new_path.append((x+dx, y+dy))
                q.append(new_path)

    visited.add( (pos, cycle) )

print(len(path)-2)