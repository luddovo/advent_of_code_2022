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

    #check for 4 diff characters
    if len(b) > 3:
        if b[cnt-4] == b[cnt-3]:
            pass
        elif b[cnt-4] == b[cnt-2]:
            pass
        elif b[cnt-4] == b[cnt-1]:
            pass
        elif b[cnt-3] == b[cnt-2]:
            pass
        elif b[cnt-3] == b[cnt-1]:
            pass
        elif b[cnt-2] == b[cnt-1]:
            pass
        else:
            print(cnt)
            break
