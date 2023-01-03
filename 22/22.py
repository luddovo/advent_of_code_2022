#!/usr/bin/env python3

# read board and instructions

b, i = ''.join(open('input.txt')).split("\n\n")

board = b.split('\n')

# extend board strings

maxw = max(len(r) for r in board)

for r in range(len(board)):
    while (len(board[r])) < maxw:
        board[r] += ' '

for r in board: print(len(r))


instructions = i.strip()

for r in board: print(len(r))


# get to the beginning of the board
row = 0
col = board[row].index('.')

# directions
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

dir = 0

# follow instructions
cnt = 0
while cnt < len(instructions):
    print(col, row)
    nl = []
    while cnt < len(instructions) and instructions[cnt] in ['0','1','2','3','4','5','6','7','8','9']:
        nl.append(instructions[cnt])
        cnt += 1
    if nl:
        # number
        n = int(''.join(nl))
        print("Move ", n)
        dx, dy = dirs[dir]
        for s in range(n):
            nx = ( col + dx ) % len(board[0])
            ny = ( row + dy ) % len(board)
            print(nx, ny)
            if board[ny][nx] == ' ':
                # loop till we get . or #
                while board[ny][nx] == ' ':
                    nx = ( nx + dx ) % len(board[0])
                    ny = ( ny + dy ) % len(board)
                if board[ny][nx] == '#':
                    break
                else:
                    col = nx
                    row = ny
            elif board[ny][nx] == '.':
                # go there
                col = nx
                row = ny
            elif board[ny][nx] == '#':
                # stop
                break
    else:
        # rotation
        rot = instructions[cnt]
        if rot == "R":
            dir = (dir + 1) % len(dirs)
        else:
            dir = (dir - 1) % len(dirs)
        cnt += 1
        print("Turn ", dir)

print(f"Column: {col+1}, row: {row+1}, direction: {dir}, res = {1000*(row+1)+ 4*(col+1) + dir}")