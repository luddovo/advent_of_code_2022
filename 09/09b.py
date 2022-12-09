#!/usr/bin/env python3

DIRS = {
    "U": [0, 1],
    "D":  [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}


visited = []

# create snake

snake = []
for i in range(10):
    snake.append([0,0])

def dst(a,b):
    return abs( a[0] - b[0] ) + abs( a[1] - b[1] )

def mark(pos):
    if not any(v[0] == pos[0] and v[1] == pos[1] for v in visited):
        visited.append([pos[0],pos[1]])

for line in open('input.txt', 'r'):

    dir, steps = line.split()

    for i in range(int(steps)):

        # move head
        snake[0][0] += DIRS[dir][0]
        snake[0][1] += DIRS[dir][1]

        # move tail
        for j in range(1,10):

            # if diagonal distance 4, move diagonally
            if dst(snake[j], snake[j-1]) == 4:
                snake[j][0] += ( snake[j-1][0] - snake[j][0] ) / 2
                snake[j][1] += ( snake[j-1][1] - snake[j][1] ) / 2
            
            # if diagonal distance 3, first move to the same row / column
            if dst(snake[j], snake[j-1]) == 3:
                if (abs(snake[j][0] - snake[j-1][0]) == 1): snake[j][0] = snake[j-1][0]
                else: snake[j][1] = snake[j-1][1]

            if dst(snake[j], snake[j-1]) < 2: pass  # same row or col

            elif dst(snake[j], snake[j-1]) == 2 and snake[j][0] != snake[j-1][0] and snake[j][1] != snake[j-1][1]: pass # diagonally next to each other

            elif dst(snake[j], snake[j-1]) == 2 and snake[j][0] == snake[j-1][0]: # above or bellow
                if snake[j][1] > snake[j-1][1]: snake[j][1] -= 1
                else: snake[j][1] += 1
            
            elif dst(snake[j], snake[j-1]) == 2 and snake[j][1] == snake[j-1][1]: # left or right
                if snake[j][0] > snake[j-1][0]: snake[j][0] -= 1
                else: snake[j][0] += 1
        
        mark(snake[9])

print("Uloha 2: ", len(visited))


