#!/usr/bin/env python3

# initial state

signal = [1]

# read input

for line in open("input.txt"):
    
    cmd = line.split()

    if cmd[0] == "noop":
        signal.append(signal[-1])
    else:
        signal.append(signal[-1])
        signal.append(signal[-1] + int(cmd[1]))

# calculate

print( sum(signal[x-1] * x for x in[20, 60, 100, 140, 180, 220]) )

print(signal)

for r in range(6):
    for c in range(40):
        if signal[r * 40  + c] in (c - 1, c, c + 1):
            print("#", end='')
        else:
            print(".", end='')
    print()