import random, time, sys
import os
import copy

HEIGHT = 15
WIDTH = 100
SHAPES = (' ', '#')
SQUARES = []
TIME_SLEEP = 0.02

# randomly populate at the begininng
def populate_board():
    for h in range(HEIGHT):
        new_column = []
        for w in range(WIDTH):
            new_column.append(random.choice(SHAPES))
        SQUARES.append(new_column)

def live_or_die(w, h):
    # calculate neibour cells
    live_neighbour = 0
    left = (w - 1) % WIDTH
    right = (w + 1) % WIDTH
    up = (h - 1) % HEIGHT
    down = (h + 1) % HEIGHT

    if (SQUARES[up][w] == SHAPES[1]): # upper neighbour
        live_neighbour += 1
    if (SQUARES[up][right] == SHAPES[1]): # upper right neighbour
        live_neighbour += 1
    if (SQUARES[up][left] == SHAPES[1]): # upper left neighbour
        live_neighbour += 1
    if (SQUARES[down][w] == SHAPES[1]): # lower neighbour
        live_neighbour += 1
    if (SQUARES[down][right] == SHAPES[1]): # lower right neighbour
        live_neighbour += 1
    if (SQUARES[down][left] == SHAPES[1]): # lower left neighbour
        live_neighbour += 1
    if (SQUARES[h][right] == SHAPES[1]): # right neighbour
        live_neighbour += 1
    if (SQUARES[h][left] == SHAPES[1]): # left neighbour
        live_neighbour += 1

    # check current state of the cell
    if (SQUARES[h][w] == SHAPES[1]): # if cell is alive
        if (live_neighbour < 2):
            return False
        elif (live_neighbour == 2 or live_neighbour == 3):
            return True
        elif (live_neighbour > 3):
            return False
    else:
        if (live_neighbour == 3):
            return True


populate_board()

while True:
    os.system('clear')
    try:
        new_squares = copy.deepcopy(SQUARES)
        for h in range(HEIGHT):
            for w in range(WIDTH):
                if (live_or_die(w, h)):
                    new_squares[h][w] = SHAPES[1]
                else:
                    new_squares[h][w] = SHAPES[0]

        SQUARES = new_squares

        for h in range(HEIGHT):
            for w in range(WIDTH):
                print(SQUARES[h][w], end='')
            print()
        time.sleep(TIME_SLEEP)
    except KeyboardInterrupt:
        sys.exit()