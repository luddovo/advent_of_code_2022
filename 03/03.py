#!/usr/bin/env python3

total = 0

for line in open("input.txt", "r"):
    
    # split line in two
    assert len(line) % 2 == 1

    a = line[:len(line)/2]
    b = line[len(line)/2:]

    both = ''
    # go through the first half and see if in second half
    for c in a:
      if c in b:
        both = c
        break
        
    print(both)

    # add to priority
    if ord('a') <= ord(both) <= ord('z'):
        total += ord(both) - ord('a') + 1
    elif ord('A') <= ord(both) <= ord('Z'):
        total += ord(both) - ord('A') + 27

print(total)