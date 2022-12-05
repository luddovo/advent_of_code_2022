#!/usr/bin/env python3

total = 0
lines = []

# read lines

for line in open("input.txt", "r"):
    lines.append(line.strip())

# process lines

for i in range(0,len(lines)-2,3):
    print(lines[i], lines[i+1], lines[i+2])
    for c in lines[i]:
        if c in lines[i+1] and c in lines[i+2]:
            print(c)
            # add to total
            if ord('a') <= ord(c) <= ord('z'):
                total += ord(c) - ord('a') + 1
            elif ord('A') <= ord(c) <= ord('Z'):
                total += ord(c) - ord('A') + 27
            break

print(total)
