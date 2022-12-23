#!/usr/bin/env python3

cubes = []

# read data
for line in open('input.txt'):
    cubes.append(line.strip().split(','))

# hack convert to ints
s = str(cubes).replace("'", '')
cubes = eval(s)

# get dimensions

maxx = max(x for x,y,z in cubes) + 1
maxy = max(y for x,y,z in cubes) + 1
maxz = max(z for x,y,z in cubes) + 1

print(cubes, maxx, maxy, maxz)

# construct 3D list, fill with cubes
shape = []
counter = 0
for i in range(maxx):
    plane = []
    for j in range(maxy):
        row = []
        for k in range(maxz):
            if [i,j,k] in cubes:    
                row.append( True )
                counter += 1
            else:
                row.append( False )
        plane.append(row)
    shape.append(plane)

removed = 0

# remove adjacent faces in three axes
for i in range(maxx):
    for j in range(maxy):
        for k in range(maxz):
            # face xy
            if k < maxz - 1:
                if shape[i][j][k] and shape [i][j][k+1]:
                    removed += 1
            # face xz
            if j < maxy - 1:
                if shape[i][j][k] and shape [i][j+1][k]:
                    removed += 1
            # face yz
            if i < maxx - 1:
                if shape[i][j][k] and shape [i+1][j][k]:
                    removed += 1

print(len(cubes), counter, removed)
print(6*counter-2*removed)