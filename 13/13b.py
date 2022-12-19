#!/usr/bin/env python3

import functools

# read input file

packets = []

for line in open("input.txt"):
    line = line.strip()
    if line: packets.append(eval(line))

# append divider packets

packets.append([[2]])
packets.append([[6]])

def compare(l,r):
    # both sides are integer
    if type(l) == int and type(r) == int:
        if l < r: return -1
        if l > r: return 1 
        if l == r: return 0 
    else:
        # at least one is list, convert the other
        if type(l) == int:
            l = [l]
        if type(r) == int:
            r = [r]
        # make copy of both lists
        l = l[:]
        r = r[:]
        # run the comparison
        while l and r:
            ret = compare(l.pop(0), r.pop(0))
            if ret != 0: return ret
        # if left and right lists are both empty, it's a draw
        if not l and not r: return 0
        # if left is empty and right is not, return True
        if not l and r: return -1
        # if right is empty and left is not, return False
        if not r and l: return 1

# sort the list
packets.sort(key = functools.cmp_to_key(compare))        

for p in packets:
    print()
    print(p)

# find divider packets
product = 1  
for i, p in enumerate(packets, start=1):
    if p == [[2]]:
        print(i,p)
        product *= i
    if p == [[6]]:
        print(i,p)
        product *= i
print(product)
