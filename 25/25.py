#!/usr/bin/env python3

import re

BASE = 5

snafu_numerals = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

dec_numerals = {0: '=', 1: '-', 2: '0', 3: '1', 4: '2'}

def base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def s2d(s):
    m = 1
    n = 0
    while s:
        n += snafu_numerals[s[-1]] * m
        m *= BASE
        s = s[:-1]
    return n

def d2s(d):

    v = d + int("222222222222222222222222", 5)

    r = base(v, 5)

    for i, c in enumerate(r):
        r[i] = dec_numerals[c]

    m = re.match(r"0+(.+)", ''.join(r))

    return m.groups(1)      
                  

sum = sum(s2d(s.strip()) for s in open('input.txt'))

print(sum, d2s(sum))
