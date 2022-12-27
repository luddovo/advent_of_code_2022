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

def go(blueprint, robots, materials, step):
    global max_yield
    
    # update prune bars
    max_yield= max(max_yield, materials['geode'])

    # reached end of branch
    if step > STEPS:
        return

    # theoretical yield
    total = materials['geode']
    for i in range(STEPS-step+1):
        total += robots['geode'] + i

    # prune
    if total < max_yield:
        return

    # see which robots makes sense making
    if step == STEPS:
        work = ['none']
    elif step == STEPS - 1:
        work = ['none','geode']
    else:
        work = ['none']
        for w in robots:
            if robots[w] < robot_limits[w]:
                work.append(w) 

    for r in work:

        # print(f"Step {step} testing {r} materials: {materials} robots {robots}")
        
        if r != 'none':
            # check if I have robots that build materials to build selected robot
            cannot_build = False
            for m in materials:
                if blueprints[blueprint][r][m] > 0:
                    if robots[m] == 0:
                        cannot_build = True
                        break
            
            if cannot_build: continue

        # fork state
        new_materials = materials.copy()
        new_robots = robots.copy()
        new_step = step

        if r!= 'none':
            # mine till we get all the materials to build the selected robot
            while True:
                if all(new_materials[m] >= blueprints[blueprint][r][m] for m in materials) or new_step >= STEPS:
                    break
                # mine materials
                for mr in robots:
                    new_materials[mr] += robots[mr]
                new_step += 1

            # build the robot
            if new_step < STEPS:    
                for m in blueprints[blueprint][r]:
                    new_materials[m] -= blueprints[blueprint][r][m]
                new_robots[r] += 1

        else:
            # mine till the one before end
            while new_step < STEPS:
                for mr in robots:
                    new_materials[mr] += robots[mr]
                new_step += 1

        # mine for the step
        for mr in robots:
            new_materials[mr] += robots[mr]
        new_step += 1

        # print(f"Step {new_step} built {r} materials: {new_materials} robots {new_robots}")

        go(blueprint, new_robots, new_materials, new_step)

for blueprint in blueprints:
    print("Blueprint: ", blueprint)
    max_yield = 0
    robot_limits = register.copy()
    for m in robot_limits: robot_limits[m] = max(blueprints[blueprint][r][m] for r in blueprints[blueprint])
    robot_limits['geode'] = STEPS + 1
    print(robot_limits)
    go(blueprint, robots.copy(), materials.copy(),1)
    print(max_yield)
    max_yields[blueprint] = max_yield

print(sum(max_yields[x] * x for x in blueprints))