#!/usr/bin/env python3

# create point table

p = dict()

p["A X"] = 4

p["A Y"] = 8

p["A Z"] = 3

p["B X"] = 1

p["B Y"] = 5

p["B Z"] = 9

p["C X"] = 7

p["C Y"] = 2

p["C Z"] = 6

# map guide to point table

points = 0

for line in open("input.txt", "r"):
    try:
        points += p[line.strip()]
    except KeyError:
        pass

print(points)