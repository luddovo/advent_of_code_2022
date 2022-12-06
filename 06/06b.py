#!/usr/bin/env python3


# read input into string

with open("input.txt", "r") as f:
    s = f.read();


# start loop

b = []
cnt = 0

for c in s:
    b.append(c)
    cnt += 1

    if len(b) > 14:
        b.pop(0)

        #check for 14 diff characters

        duplicates = False

        for c1 in b:
            if b.count(c1) > 1:
                duplicates = True
                break

        if not duplicates:
            print(cnt)
            break
        
