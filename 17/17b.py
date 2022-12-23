#!/usr/bin/env python3

# load data
push_data = ''.join(open('input.txt')).strip()

# shapes

shapes = {
    'hbar':  [(0,0), (1,0), (2,0), (3,0)],
    'cross': [(1, 0), (0, -1), (1, -1), (2, -1), (1, -2)],
    'lshape':[(2, 0), (2, -1), (2, -2), (1, -2), (0, -2)],
    'vbar':  [(0,0), (0, -1), (0, -2), (0, -3)],
    'box':   [(0, 0), (1, 0), (0, -1), (1, -1)]
}

def collision(board, shape, x, y):
    return any(board[y+j][x+i] for i, j in shapes[shape])

def bprint(board, shape, x, y):
    for i, j in shapes[shape]: board[y+j][x+i] = True

order = ['hbar', 'cross', 'lshape', 'vbar', 'box']

floor = [True for x in range(9)]

board = [floor]


def play(stop):
    global board

    piece_counter = 0

    shift_counter = 0

    tower_height = 0

    board_height = 0

    # play

    while piece_counter < stop:
        #next shape
        shape = order[piece_counter % len(order)]
        x = 3
        # extend board
        l = min(j for i, j in shapes[shape])
        new_y =  tower_height + 4 - l
        for i in range(board_height, new_y):
                board.append([True] + [ False for x in range(7) ] + [True])
        board_height = max(new_y, board_height)
        y = new_y

        while True:
            # push
            newx = x - 1 if push_data[shift_counter % len(push_data)] == '<' else x + 1
            shift_counter += 1
            if not collision(board, shape, newx, y): x = newx

            # drop
            if not collision(board, shape, x, y - 1):
                y = y - 1 
            else:
                # print
                bprint(board, shape, x, y)
                # update height
                tower_height = max(tower_height, y)

                # update counter
                piece_counter += 1            

                if piece_counter == 1370:
                    print(piece_counter, tower_height)

                if tower_height in [588, 3278, 5968, 8658]:
                    print(piece_counter, tower_height)


                #print("shape: ", shape, "th: ", tower_height, "cnt: ", piece_counter, shift_counter)
                #for line in board[::-1]:
                #        for v in line:
                #            print('*' if v else ' ', end='')
                #        print()
                #print()

                break
    return tower_height

stop = 10000

play(stop)

print(len(board))

# find cycle
#for i in range(len(board)):
#    for j in range(i+1, len(board)):
#        if all(board[i+k] == board[j+k] for k in range(20)): print(i,j)

# cycle starts at 587 repeats at 3277
#
#
# 360 + 583090378 cycles of 1715 , rests 1370
#
# 360 = 588
#
# repeat cycle 1715 = 2690
#
# 1370 = 2163