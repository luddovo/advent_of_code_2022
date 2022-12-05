#!/usr/bin/env python3

# create point table

#r 1
#p 2
#s 3

p = dict()

p["A X"] = 3    # l 0 rs 3      

p["A Y"] = 4    # d 3 rr 1

p["A Z"] = 8    # w 6 rp 2

p["B X"] = 1    # l 0 pr 1

p["B Y"] = 5    # d 3 pp 2

p["B Z"] = 9    # w 6 ps 3

p["C X"] = 2    # l 0 sp 2

p["C Y"] = 6    # d 3 ss 3

p["C Z"] = 7    # w 6 sr 1

# map guide to point table

points = 0

for line in open("input.txt", "r"):
    try:
        points += p[line.strip()]
    except KeyError:
        pass

print(points)