#!/usr/bin/env python3


# read input file

data = ''.join(open("input.txt")).strip().split('\n\n')

pairs = []

for item in data:
    l, r = tuple(item.split('\n'))
    pairs.append((eval(l),eval(r)))

def compare(l,r):
    # both sides are integer
    if type(l) == int and type(r) == int:
        if l < r: return True 
        if l > r: return False 
        if l == r: return 'draw' 
    else:
        # at least one is list, convert the other
        if type(l) == int:
            l = [l]
        if type(r) == int:
            r = [r]
        # run the comparison
        while l and r:
            ret = compare(l.pop(0), r.pop(0))
            if type(ret) == bool: return ret
        # if left and right lists are both empty, it's a draw
        if not l and not r: return 'draw'
        # if left is empty and right is not, return True
        if not l and r: return True
        # if right is empty and left is not, return False
        if not r and l: return False
        

total = 0  
for i, (l,r) in enumerate(pairs, start=1):
    if compare(l,r): total += i
print(total)
