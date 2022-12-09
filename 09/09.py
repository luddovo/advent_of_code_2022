#!/usr/bin/env python3

DIRS = {
    "U": [0, 1],
    "D":  [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}


visited = []

hx, hy, tx, ty = 0, 0, 0, 0

def dst():
    return abs( tx - hx ) + abs( ty - hy )

def mark():
    if not any(v[0] == tx and v[1] == ty for v in visited):
        visited.append([tx, ty])

for line in open('input.txt', 'r'):
    
    dir, steps = line.split()

    for i in range(int(steps)):

        # move head
        hx += DIRS[dir][0]
        hy += DIRS[dir][1]

        # if diagonal, first move to the same row / column
        if dst() == 3:
            if (abs(tx - hx) == 1): tx = hx
            else: ty = hy

        if dst() < 2: pass  # same row or col
        elif dst() == 2 and tx != hx and ty != hy: pass # diagonally next to each other
        elif dst() == 2 and tx == hx: # above or bellow
            if ty > hy: ty -= 1
            else: ty += 1
            mark()
        elif dst() == 2 and ty == hy: # left or right
            if tx > hx: tx -= 1
            else: tx += 1
            mark()

print("Uloha 1: ", len(visited))


