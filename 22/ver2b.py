#!/usr/bin/env python3

import math, re

def pos_mod(map, dx, dy):
    x, y = map
    x = ((x + dx) % 5 + 5) % 5
    y = ((y + dy) % 5 + 5) % 5
    return (x,y)

# Dir
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def password(cursor, size):
    x = cursor['map'][0] * size + cursor['inner'][0] + 1
    y = cursor['map'][1] * size + cursor['inner'][1] + 1
    dir = cursor['dir']
    return y * 1000 + x * 4 + dir

def enter_map(dir, offset, size):
    if dir == UP:
        return (offset, size - 1)
    elif dir == RIGHT:
        return (0, offset)
    elif dir == DOWN:
        return (size - offset - 1, 0)
    elif dir == LEFT:
        return (size - 1, size - offset - 1)

def run():
    global cursor

    for inst in instructions:
        if type(inst) is int:
            for i in range(inst):
                # go inst steps
                if cursor['dir'] == UP:
                    if cursor['inner'][1] == 0:
                        new_dir = maps[cursor['map']]['exits'][UP][1]
                        new_map = maps[cursor['map']]['exits'][UP][0]
                        new_inner = enter_map(new_dir, cursor['inner'][0], size)
                    else:
                        new_dir = cursor['dir']
                        new_map = cursor['map']
                        new_inner = (cursor['inner'][0], cursor['inner'][1]-1)

                elif cursor['dir'] == RIGHT:
                    if cursor['inner'][0] == size - 1:
                        new_dir = maps[cursor['map']]['exits'][RIGHT][1]
                        new_map = maps[cursor['map']]['exits'][RIGHT][0]
                        new_inner = enter_map(new_dir, cursor['inner'][1], size)
                    else:
                        new_dir = cursor['dir']
                        new_map = cursor['map']
                        new_inner = (cursor['inner'][0]+1, cursor['inner'][1])

                elif cursor['dir'] == DOWN:
                    if cursor['inner'][1] == size - 1:
                        new_dir = maps[cursor['map']]['exits'][DOWN][1]
                        new_map = maps[cursor['map']]['exits'][DOWN][0]
                        new_inner = enter_map(new_dir, size-cursor['inner'][0]-1, size)
                    else:
                        new_dir = cursor['dir']
                        new_map = cursor['map']
                        new_inner = (cursor['inner'][0], cursor['inner'][1]+1)

                elif cursor['dir'] == LEFT:
                    if cursor['inner'][0] == 0:
                        new_dir = maps[cursor['map']]['exits'][LEFT][1]
                        new_map = maps[cursor['map']]['exits'][LEFT][0]
                        new_inner = enter_map(new_dir, size-cursor['inner'][1]-1, size)
                    else:
                        new_dir = cursor['dir']
                        new_map = cursor['map']
                        new_inner = (cursor['inner'][0]-1, cursor['inner'][1])

                if maps[new_map]['content'][new_inner[1]][new_inner[0]] == '.':
                    cursor['dir'] = new_dir   
                    cursor['map'] = new_map   
                    cursor['inner'] = new_inner   
        

        elif inst == 'R':
            cursor['dir'] = ( cursor['dir'] + 1 ) % 4
        elif inst == 'L':
            cursor['dir'] = ( cursor['dir'] + 3 ) % 4
        else:
            print('PANIC', inst)
            exit()
        
# read input
board, inst, dummy = ''.join(open('input.txt')).split('\n\n')

board = board.split('\n')
h = len(board)
w = max(len(line) for line in board)
size = math.gcd(h,w)

cursor = {}

maps = {}

# read board

for y, line in enumerate(board):
    for x, c in enumerate(line):
        if c in ['.','#']:
            map_pos = (x // size, y // size)
            inner_pos = (x % size, y % size)
            if map_pos in maps:
                maps[map_pos]['content'][inner_pos[1]][inner_pos[0]] = c
            else:
                content = []
                for j in range(size):
                    row = []
                    for i in range(size):
                        row.append('.')
                    content.append(row)
                content[inner_pos[1]][inner_pos[0]] = c
                maps[map_pos] = {}
                maps[map_pos]['content'] = content

            if not cursor and c == '.':
                cursor = {'dir': RIGHT, 'map': map_pos, 'inner': inner_pos}

# read instructions
instructions = re.findall(r"(R|L|\d+)", inst)
for i, x in enumerate(instructions):
    if str.isnumeric(x): instructions[i] = int(x)


# part 2 find exits

for map in maps: maps[map]['exits'] = {}

for map in maps:
    if pos_mod(map, -1, 0) in maps:
        maps[map]['exits'][LEFT] = [pos_mod(map, -1, 0), LEFT]
    if pos_mod(map, 1, 0) in maps:
        maps[map]['exits'][RIGHT] = [pos_mod(map, 1, 0), RIGHT]
    if pos_mod(map, 0, -1) in maps:
        maps[map]['exits'][UP] = [pos_mod(map, 0, -1), UP]
    if pos_mod(map, 0, 1) in maps:
        maps[map]['exits'][DOWN] = [pos_mod(map, 0, 1), DOWN]

while True:
    for map in maps:
        for d in range(4):
            if d in maps[map]['exits']:
                e1 = maps[map]['exits'][d]
                if (d+1) % 4 in maps[map]['exits']:
                    e2 = maps[map]['exits'][(d+1) % 4]
                    m1 = maps[e1[0]]
                    fd1 = ( e1[1] + 1) % 4
                    td1 = ( e2[1] + 1) % 4
                    m1['exits'][fd1] = [e2[0], td1]
                    m2 = maps[e2[0]]
                    fd2 = (e2[1] + 3) % 4
                    td2 = (e1[1] + 3) % 4
                    m2['exits'][fd2] = [e1[0], td2]

    cnt = 0
    for map in maps: cnt += len(maps[map]['exits'])
    if cnt == 24: break 

# run
run()

print("Result: ", password(cursor, size))
