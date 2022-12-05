#!/usr/bin/env python3


# build stacks

stacks = []

for i in range(9):
    stacks.append([])

for line in open("crates.txt", "r"):
    print(line)
    for i in range(9):
        print(i,line[1+i*4])
        if line[1+i*4] != " ":
            stacks[i].append(line[1+i*4])

for s in stacks:
    print(s)

# move crates

for line in open("moves.txt", "r"):
    c, f, t = line.split()
    c, f , t = int(c), int(f) - 1, int(t) - 1

    h = []
    for i in range(c):
        h.append( stacks[f].pop(0) )

    stacks[t] = h + stacks[t]

print()

for s in stacks:
    print(s)
