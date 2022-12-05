#!/usr/bin/env python3

total = 0

for line in open("input.txt", "r"):
    p1, p2 = line.split(",")
    e1mins, e1maxs = p1.split("-")
    e2mins, e2maxs = p2.split("-")
    e1min = int(e1mins)
    e1max = int(e1maxs)
    e2min = int(e2mins)
    e2max = int(e2maxs)

    print(line, p1, p2, e1min, e1max, e2min, e2max)

    if (e1min >= e2min and e1max <= e2max):
        total += 1
    elif (e2min >= e1min and e2max <= e1max):
        total += 1

print(total)