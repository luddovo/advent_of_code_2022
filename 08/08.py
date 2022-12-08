#!/usr/bin/env python3

import math

# read matrix

matrix = []

for line in open("input.txt"):
    matrix.append( [*line.strip()] )

total = 0

# rotate array 4 times
for i in range(4):

    # check visibility
    for r in range(len(matrix)):
        bar = -1
        for c in range(len(matrix[r])):
            v = int(matrix[r][c]) 
            if v > bar:
                bar = v
                if not isinstance(matrix[r][c], float):
                    matrix[r][c] = float(matrix[r][c])
                    total += 1

    # turn
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]


print("Uloha 1: ", total)

# exc. 2

# add total to each element
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix[r][c] = [int(matrix[r][c]),-1]

# calculate distances 4 directions, rotate matrix
for i in range(4):

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            i = c - 1
            d = 0
            while i >= 0:
                d = d + 1
                if matrix[r][i][0] >= matrix[r][c][0]: break
                i -= 1
            if matrix[r][c][1] == -1:
                matrix[r][c][1] = d
            else:
                matrix[r][c][1] *= d
                
    # turn
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

# find highest score
total = 0
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        v = matrix[r][c][1]
        if v > total: total = v

print("Uloha 2: ", total)