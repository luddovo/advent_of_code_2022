#!/usr/bin/env python3

import re, pygame, functools

# Defines

AIR = 0
ROCK = 1
SAND = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 5
HEIGHT = 4
 
# This sets the margin between each cell
MARGIN = 1

# get dimensions of the field

l = [ eval('(' + x + ')') for x in re.findall(r'[0-9]+,[0-9]+', ''.join(open('input.txt'))) ]

minx = min([x for x,y in l])
maxx = max([x for x,y in l])
miny = min([y for x,y in l])
maxy = max([y for x,y in l])

# adjust for overflow
miny -= 1

w = maxx-minx + 1
h = maxy-miny + 1

print(w,h)

# create grid

grid = [[AIR for x in range(w)] for y in range(h)]

# coordinate conversion function

def c(x, y):
    return(x - minx, y - miny)

# draw walls

def draw_wall(grid, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # go from min to max
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1

    # draw
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            cx, cy = c(x, y)
            grid[cy][cx] = ROCK
    
    # next value for reduce
    return p2

for line in open('input.txt'):
    pts = [eval('(' + x + ')') for x in re.findall(r'[0-9]+,[0-9]+', line)]
    print(pts)
    functools.reduce(lambda p1,p2: draw_wall(grid, p1,p2), pts)

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [w * (WIDTH + MARGIN) , h * (HEIGHT + MARGIN)]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("AOC Day 14")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Grain counter
counter = 0

# -------- Main Program Loop -----------
while not done:

    move = False

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # no interaction yet
 
    # grain of sand
    gx, gy = c(500,0)
    while True:
        if grid[gy+1][gx] == AIR: gy += 1
        elif grid[gy+1][gx-1] == AIR:
            gy += 1
            gx -= 1
        elif grid[gy+1][gx+1] == AIR:      
            gy += 1
            gx += 1
        else:
            grid[gy][gx] = SAND
            counter += 1
            break

        if gy == h - 1:
            done = True
            break

    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            color = WHITE
            if grid[row][column] == ROCK:
                color = BLACK
            elif grid[row][column] == SAND:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(100)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

print(counter)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()


