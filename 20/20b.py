#!/usr/bin/env python3

numbers = []

# read input data

for i, line in enumerate(open('input.txt')):
    numbers.append({"value": 811589153 * int(line.strip()), "order": i})

print(numbers, len(numbers))

# mix

for cnt in range(10):

    for i in range(len(numbers)):
        index = [x['order'] for x in numbers].index(i)

        # zero does not move
        if numbers[index]['value'] == 0: continue

        #print(list(x['value'] for x in numbers))

        # remove the item
        item = numbers.pop(index)

        new_index = ( index + item['value'] ) % len(numbers)

        # move right
        if item['value'] > 0:
            # insert after
            if new_index == len(numbers): new_index = 0

            numbers.insert(new_index, item)
        # move left
        else:
            # insert before

            if new_index > 0:
                numbers.insert(new_index, item)
            else:
                numbers.append(item)

        #print(list(x['value'] for x in numbers))

# find 0
index = [x['value'] for x in numbers].index(0)
print(f"Index of 0 is {index}")

print([numbers[(index + i) % len(numbers)]['value'] for i in [1000,2000,3000]])
print(sum(numbers[(index + i) % len(numbers)]['value'] for i in [1000,2000,3000]))
