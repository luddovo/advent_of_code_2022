#!/usr/bin/env python3

import re

monkeys = {}

modulo = 1

# read input

for m in ''.join(open('input.txt')).split('\n\n'):
    
    ma = m.split('\n')
    ma = [s.strip() for s in ma]

    n = int( re.split(" |:", ma[0])[1] )

    monkeys[n] = {}

    monkeys[n]['count'] = 0

    # starting items
    monkeys[n]['items'] = [int(x) for x in re.search("Starting items: (.*)", ma[1]).group(1).split(",")]

    # build the supermodulo
    for x in monkeys[n]['items']: modulo *= x

    # operation
    monkeys[n]['operation'] = re.search("Operation: new = (.*)", ma[2]).group(1)

    # test
    monkeys[n]['test'] = int( re.search("Test: divisible by (.*)", ma[3]).group(1) )

    # true
    monkeys[n]['true'] = int( re.search("If true: throw to monkey (.*)", ma[4]).group(1) )

    # false
    monkeys[n]['false'] = int( re.search("If false: throw to monkey (.*)", ma[5]).group(1) )

# throw items

ROUNDS = 10000

for i in range(ROUNDS):
    print(i)
    for n, monkey in monkeys.items():
        while monkey['items']:
            # inspect
            monkey['count'] += 1
            old = monkey['items'].pop(0)
            new = eval(monkey['operation']) % modulo
            #throw
            monkeys[ monkey['true'] if new % monkey['test'] == 0 else monkey['false'] ]['items'].append(new)
# find the two most active monkeys

l = []

for n, monkey in monkeys.items():
    l.append(monkey['count'])

l.sort(reverse=True)

print(l[0] * l[1])
