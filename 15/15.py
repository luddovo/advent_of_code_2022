#!/usr/bin/env python3

import re

LINE = 2000000


# read data

sensors = []

for line in open('input.txt'):
    d = re.findall(r'-*\d+', line)
    s = {}
    for i, k in enumerate(['sx','sy','bx','by']):
        s[k] = int(d[i])
    s['dist'] = abs(s['bx'] - s['sx']) + abs(s['by'] - s['sy'])

    sensors.append(s)
    print(s)

# create beacons set for later

beacons = set([])

for s in sensors:
    beacons.add( (s['bx'], s['by']) )

# find intervals of coverage on the line for all beacons

intervals = []

for s in sensors:
    dfl = abs(s['sy'] - LINE)
    # see if sensor can reach the line
    if dfl <= s['dist']:
        reachx = s['dist'] - dfl
        interval = { 'b': s['sx'] - reachx, 'e': s['sx'] + reachx }
        intervals.append(interval)
        print(interval)

# merge intervals

merged = []

# sort all points

points = []

for i in intervals:
    points.append( { 'x': i['b'], 'type': 'b'} )
    points.append( { 'x': i['e'], 'type': 'e'} )

points.sort(key=lambda i: i['x'])
print(points)

# do the merging

b_counter = 0

merged = []

for p in points:
    if p['type'] == 'b':
        if b_counter == 0:
            interval_start = p['x']
        b_counter += 1
    else:
        b_counter -= 1
        if b_counter == 0:
            merged.append( (interval_start, p['x']) )

print(merged)

# count total coverage

total = 0

for b, e in merged:
    total += e - b + 1

print(total)

# exclude beacon locations

for bx, by in beacons:
    if by == LINE:
        # go through intervals
        for ib, ie in merged:
            if ib <= bx <= ie:
                total -= 1

print(total)