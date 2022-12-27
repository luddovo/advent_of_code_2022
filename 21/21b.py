#!/usr/bin/env python3

import re

numbers = {}
op1 = {}
op = {}
op2 = {}

for line in open('input.txt'):
    m = re.match(r'(....): (\d+)', line.strip())
    if m:
        numbers[m.group(1)] = int(m.group(2))
    else:
        m = re.match(r'(\w+): (\w+) (.) (\w+)', line.strip())
        if m:
            op1[m.group(1)] = m.group(2)
            op[m.group(1)] = m.group(3)
            #if m.group(3) == '/':
            #    op[m.group(1)] = '//'
            op2[m.group(1)] = m.group(4)

print(numbers, op1, op, op2)


def go(monkey):
    if monkey in numbers:
        return numbers[monkey]
    return eval('go(op1[monkey]) ' +  op[monkey] + ' go(op2[monkey])')

#upper bound

cnt = 1

print("Upper bound")

while True:
    numbers['humn'] = cnt
    print(cnt, go(op1['root']), go(op2['root']))
    if go(op1['root']) < go(op2['root']):
        print(cnt)
        break
    cnt *= 2

print("Interval halving")

# interval halving
max = cnt
min = cnt // 2
while True:
    print(min, max)
    numbers['humn'] = min
    a = abs(go(op1['root']) - go(op2['root']))
    numbers['humn'] = max
    b = abs(go(op1['root']) - go(op2['root']))
    if a < b:
        max = min + (max - min) // 2
    elif a > b:
        min = min + (max - min) // 2
    else:
        print(go(op1['root']), go(op2['root']), min,max)
        break

# search
print("Search")

for i in range(min, max+1):
    numbers['humn'] = i
    if go(op1['root']) == go(op2['root']):
        print(i, go(op1['root']), go(op2['root']))