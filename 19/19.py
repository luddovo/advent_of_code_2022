#!/usr/bin/env python3

# have one ore robot
# have 24 minutes for each blueprint
# ore, clay, obsidian, geode
# substract and build at the beginning of minute
# produce during the minute
# can produce, or build
# maximize geode production

# read input

import parse

register = {
    'ore': 0,
    'clay': 0,
    'obsidian': 0,
    'geode': 0
}

blueprints = {}

for line in open('test_input.txt'):
    print(line)
    d = parse.parse("Blueprint {blueprint}: Each ore robot costs {ore_ore} ore. Each clay robot costs {clay_ore} ore. Each obsidian robot costs {obsidian_ore} ore and {obsidian_clay} clay. Each geode robot costs {geode_ore} ore and {geode_obsidian} obsidian.", line.strip())
    
    r = register.copy()
    
    # empty robot
    c = register.copy()
    r['none'] = c

    c = register.copy()
    c['ore'] = int(d['ore_ore'])
    r['ore'] = c

    c = register.copy()
    c['ore'] = int(d['clay_ore'])
    r['clay'] = c

    c = register.copy()
    c['ore'] = int(d['obsidian_ore'])
    c['clay'] = int(d['obsidian_clay'])
    r['obsidian'] = c

    c = register.copy()
    c['ore'] = int(d['geode_ore'])
    c['obsidian'] = int(d['geode_obsidian'])
    r['geode'] = c

    blueprints[int(d['blueprint'])] = r

robots = register.copy()
robots['ore'] = 1

materials = register.copy()

print(blueprints)
print(robots)
print(materials)

max_yields = {}

STEPS = 24

max_yield = 0

prune_bars = register.copy()

def go(blueprint, robots, materials, step):
    global max_yield, prune_bars
    
    # update prune bars
    for b in prune_bars:
        if materials[b] > 0 and step < prune_bars[b]:
            prune_bars[b] = step
            print(f"First {b} reached in {step} steps.")

    # prune
    for b in prune_bars:
        if materials[b] == 0 and step > prune_bars[b]:
            return

    # reached end of branch
    if step == STEPS:
        max_yield= max(max_yield, materials['geode'])
        return

    for r in ['none', 'geode', 'obsidian', 'clay', 'ore']:
        # check build robot
        #print(f"Step {step} testing {r} materials: {materials} robots {robots}")
        cannot_build = any(materials[m] < blueprints[blueprint][r][m] for m in blueprints[blueprint][r])
        if cannot_build: continue

        # fork state
        new_materials = materials.copy()
        new_robots = robots.copy()

        # mine materials
        for mr in robots:
            new_materials[mr] += robots[mr]

        # build robot
        if r != 'none':
            for m in blueprints[blueprint][r]:
                new_materials[m] -= blueprints[blueprint][r][m]
            new_robots[r] += 1

        #print(f"Step {step} built {r} materials: {materials} robots {robots}")

        go(blueprint, new_robots, new_materials, step + 1)

for blueprint in blueprints:
    print("Blueprint: ", blueprint)
    max_yield = 0
    # reset prune bars
    for b in prune_bars: prune_bars[b] = STEPS + 1
    # prune_bars = {'ore': 2, 'clay': 4, 'obsidian': 11, 'geode': STEPS + 1}
    go(blueprint, robots.copy(), materials.copy(),0)
    print(max_yield)
    max_yields[blueprint] = max_yield

print(sum(max_yields[x] * x for x in blueprints))