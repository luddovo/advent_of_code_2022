#!/usr/bin/env python3

import re

LINE_MIN = 0
LINE_MAX = 4000000

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

# find and intervals of coverage on a line for all beacons

def intervals_in_line(line):

    intervals = []

    for s in sensors:
        dfl = abs(s['sy'] - line)
        # see if sensor can reach the line
        if dfl <= s['dist']:
            reachx = s['dist'] - dfl
            interval = { 'b': s['sx'] - reachx, 'e': s['sx'] + reachx }
            intervals.append(interval)

    # merge intervals

    merged = []

    # sort all points

    points = []

    for i in intervals:
        points.append( { 'x': i['b'], 'type': 'b'} )
        points.append( { 'x': i['e'], 'type': 'e'} )

    points.sort(key=lambda i: (i['x'], i['type']))

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

    return merged

# go though all the lines in range, if there's a gap in the coverage, print it

for l in range(LINE_MIN, LINE_MAX + 1):
    i = intervals_in_line(l)
    if (len(i) > 1):
        b, e = i[0]
        answer = (e + 1) * 4000000 + l
        print(l, i, answer)