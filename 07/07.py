#!/usr/bin/env python3

# node class
class DirNode:
    def __init__(self, parent, name, type, size = 0):
        self.parent = parent
        self.name = name
        self.type = type
        self.size = size
        self.children = []

root = current_node = DirNode(None, '/', 'd')

# traverse input file and create tree
for line in open("input.txt", "r"):
    ws = line.split()
    if ws[0] == '$':
        if ws[1] == "ls":
            # process files at current level
            pass
        elif ws[1] == "cd":
            # go up or down
            if ws[2] == '..':
                current_node = current_node.parent
            else:
                for n in current_node.children:
                    if n.name == ws[2]:
                        current_node = n
                        break                    
            pass
    elif ws[0].isdigit():
            # create file if not exist
            if not any( node.name == ws[1] for node in current_node.children):
                current_node.children.append(DirNode(current_node, ws[1],'f',int(ws[0])))
    elif ws[0] == 'dir':
            # create dir if not exist
            if not any( node.name == ws[1] for node in current_node.children):
                current_node.children.append(DirNode(current_node, ws[1],'d'))
 
# traverse tree, calculate sizes, and pretty print the tree
def calc_size(node, indent = ''):

    indent += '  '

    if node.type == 'f':
        return node.size
    else:
        size = 0
        for c in node.children:
            size += calc_size(c, indent)
        node.size = size
        
    print(indent, node.name, node.type, node.size)

    return node.size

calc_size(root)
    

# traverse tree and get sizes

LIMIT = 100000

def sum_sizes(node, sum = 0):
    
    if node.type == 'f': return 0

    sum = 0

    # loop through all children to add themselves
    for n in node.children: sum += sum_sizes(n, sum)

    # if current dir under limit, add to the count
    if node.size <= LIMIT: sum += node.size

    # return sum
    return sum

print("Uloha 1: ", sum_sizes(root))

total_size = 70000000

free_space = total_size - root.size

space_needed = 30000000

current_pick = total_size

# traverse the tree and get smallest directory that needs to be deleted to get free_space over space_needed

def dir_to_delete(node, current_pick = total_size):

    v = free_space + node.size
    if v > space_needed and node.size < current_pick:
        current_pick = node.size

    for n in node.children: current_pick = dir_to_delete(n, current_pick)

    return current_pick

print("Uloha 2: ", dir_to_delete(root))
