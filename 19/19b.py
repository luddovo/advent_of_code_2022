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

for line in open('input.txt'):
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

STEPS = 32

max_yield = 0

def go(blueprint, robots, materials, step):
    global max_yield
    
    # reached end of branch
    if step > STEPS:
        return

    # update prune bars
    max_yield= max(max_yield, materials['geode'])

    # theoretical yield
    total = materials['geode']
    for i in range(STEPS-step):
        total += robots['geode'] + i

    # prune
    if total < max_yield:
        return

    if step == STEPS - 1:
        work = ['none']
    elif step == STEPS - 2:
        work = ['none', 'geode']
    else:
        work = ['none']
        for w in robots:
            if robots[w] < robot_limits[w]:
                work.append(w) 

    for r in work:
        # check build robot
        #print(f"Step {step} testing {r} materials: {materials} robots {robots}")
        if r != 'none':
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

for blueprint in [1,2,3]:
    print("Blueprint: ", blueprint)
    max_yield = 0
    robot_limits = register.copy()
    for m in robot_limits: robot_limits[m] = max(blueprints[blueprint][r][m] for r in blueprints[blueprint])
    robot_limits['geode'] = STEPS + 1
    print(robot_limits)
    go(blueprint, robots.copy(), materials.copy(),0)
    print(max_yield)
    max_yields[blueprint] = max_yield

print(sum(max_yields[x] * x for x in blueprints))