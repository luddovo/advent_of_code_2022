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

# find interior empty cubes

def is_enclosed(pos):
    visited = set([])
    q = [pos]

    while q:
        voxel = q.pop(0)
        if voxel not in visited:
            x, y, z = voxel
            # test if reached the bounding box
            if x == 0 or x == maxx - 1 or y == 0 or y == maxy - 1 or z == 0 or z == maxz - 1:
                return False
            # test all neighbors
            if x > 0:
                if not shape[x-1][y][z]:
                    q.append((x-1,y,z))    
            if x < maxx - 1:
                if not shape[x+1][y][z]:
                    q.append((x+1,y,z))    
            if y > 0:
                if not shape[x][y-1][z]:
                    q.append((x,y-1,z))    
            if y < maxy - 1:
                if not shape[x][y+1][z]:
                    q.append((x,y+1,z))    
            if z > 0:
                if not shape[x][y][z-1]:
                    q.append((x,y,z-1))    
            if z < maxz - 1:
                if not shape[x][y][z+1]:
                    q.append((x,y,z+1))    

            visited.add(voxel)
    # no path to the outside found
    print(voxel)    
    return True

# initialize air pockets 3D list

air_pockets = []
for i in range(maxx):
    plane = []
    for j in range(maxy):
        row = []
        for k in range(maxz):
            row.append(False)
        plane.append(row)
    air_pockets.append(plane)

# map all interior empty cubes            
for i in range(maxx):
    for j in range(maxy):
        for k in range(maxz):
            if not shape[i][j][k]:
                air_pockets[i][j][k] = is_enclosed((i,j,k))

# remove adjacent faces in three axes
for i in range(maxx):
    for j in range(maxy):
        for k in range(maxz):
            # face xy
            if k > 0:
                if shape[i][j][k] and air_pockets[i][j][k-1]:
                    removed += 1
            if k < maxz - 1:
                if shape[i][j][k] and shape [i][j][k+1]:
                    removed += 2
                if shape[i][j][k] and air_pockets[i][j][k+1]:
                    removed += 1
            # face xz
            if j > 0:
                if shape[i][j][k] and air_pockets[i][j-1][k]:
                    removed += 1
            if j < maxy - 1:
                if shape[i][j][k] and shape [i][j+1][k]:
                    removed += 2
                if shape[i][j][k] and air_pockets[i][j+1][k]:
                    removed += 1
            # face yz
            if i > 0:
                if shape[i][j][k] and air_pockets[i-1][j][k]:
                    removed += 1
            if i < maxx - 1:
                if shape[i][j][k] and shape [i+1][j][k]:
                    removed += 2
                if shape[i][j][k] and air_pockets[i+1][j][k]:
                    removed += 1

# cube is inside

print(len(cubes), counter, removed)
print(6*counter-removed)