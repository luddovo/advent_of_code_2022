#!/usr/bin/env python3

total = 0
lines = []

# read lines

for line in open("input.txt", "r"):
    lines.append(line.strip())

# process lines

for i in range(len(lines),3):
    for c in lines[i]:
        if c in lines[i+1] and c in lines[i+2]:
            # add to total
            if ord('a') <= ord(both) <= ord('z'):
                total += ord(both) - ord('a') + 1
            elif ord('A') <= ord(both) <= ord('Z'):
                total += ord(both) - ord('A') + 27

print(total)