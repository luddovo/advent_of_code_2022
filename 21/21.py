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
            op2[m.group(1)] = m.group(4)

print(numbers, op1, op, op2)




def go(monkey):
    if monkey in numbers:
        return numbers[monkey]
    return eval('go(op1[monkey]) ' +  op[monkey] + ' go(op2[monkey])')


print(go('root'))