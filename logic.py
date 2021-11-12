import random


def add_new_2(mat):
    """Function to add a new 2 to the grid in a random cell

    :param mat: 2D list that represents our 4-by-4 gameboard
    """

    # choosing a random index for
    # row and column.
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # while loop will break once the
    # random cell chosen is empty (contains 0)
    while (mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # we will place a 2 at that empty
    # random cell.
    mat[r][c] = 2

def start_game():
    """Function to start the game by creating the gameboard and adding the first 2

    :return: mat: a 2D list that represents our 4-by-4 gameboard
    """

    # the starting board
    mat = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

    # print controls for user
    print("\n\n")
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    print("\n\n")

    # calling the function to add
    # a new 2 in grid after every step
    add_new_2(mat)

    return mat


def game_state(mat):
    """Function to determine if the user has WON, LOST, or NEITHER

    :param mat: a 2D list representing our 4-by-4 gameboard
    :return: a String that tells the user if they won, lost, or if they can keep playing
    """

    # traverse matrix in ROW-COLUMN order
    for r in range(4):
        for c in range(4):
            # if matrix contains 2048, the user has won
            if mat[r][c] == 2048:
                return "VICTORY!"
            # if there is still a location for a 2 to be inserted, the game is not over yet
            elif mat[r][c] == 0:
                return "KEEP GOING!"

    # traverse matrix in ROW-COLUMN order
    for r in range(3):
        for c in range(3):
            # if there are cells that can be merged together, the game is not over yet
            if mat[r][c] == mat[r + 1][c] or mat[r][c] == mat[r][c + 1]:
                return "KEEP GOING!"

    # traverses elements not traversed in loop ABOVE
    for x in range(3):
        # if there are cells that can be merged together, the game is not over yet
        if mat[x][3] == mat[x + 1][3]:
            return "KEEP GOING!"
        elif mat[3][x] == mat[3][x + 1]:
            return "KEEP GOING!"

    # if the function has not returned a value yet, we know the game is over
    return "GAME OVER!"


def compress(mat, letter):
    """Function to compress the grid BEFORE merging cells.

    By compress, we mean shifting all of the entries over WITHOUT combining them.

    :param mat: a 2D list representing our 4-by-4 gameboard
    :param letter: a single-character string that represents the direction that the user has chosen to move in
    :return: the compressed gameboard and a variable "changed" that indicates whether the gameboard
    was altered in any way
    """

    # bool variable to determine if any change happened or not
    changed = False

    # here we will determine which way to shift entries (left, up, right, or down)
    if letter.upper() == "A":
        for r in range(4):

            # traverse columns leftwards and shifts entries rightwards
            for c in range(3, 0, -1):

                if mat[r][c - 1] == 0 and mat[r][c] != 0:
                    mat[r][c - 1] = mat[r][c]
                    mat[r][c] = 0
                    changed = True

            # traverse columns rightwards and shifts entries leftwards
            for c in range(0, 3):

                if mat[r][c] == 0 and mat[r][c + 1] != 0:
                    mat[r][c] = mat[r][c + 1]
                    mat[r][c + 1] = 0
                    changed = True
    elif letter.upper() == "W":
        for c in range(4):

            # traverse rows upwards and shifts entries upwards
            for r in range(3, 0, -1):

                if mat[r - 1][c] == 0 and mat[r][c] != 0:
                    mat[r - 1][c] = mat[r][c]
                    mat[r][c] = 0
                    changed = True

            # traverse rows downwards and shifts entries upwards
            for r in range(0, 3):

                if mat[r][c] == 0 and mat[r + 1][c] != 0:
                    mat[r][c] = mat[r + 1][c]
                    mat[r + 1][c] = 0
                    changed = True
    elif letter.upper() == "D":
        for r in range(4):

            # traverse columns rightwards and shifts entries rightwards
            for c in range(0, 3):

                if mat[r][c + 1] == 0 and mat[r][c] != 0:
                    mat[r][c + 1] = mat[r][c]
                    mat[r][c] = 0
                    changed = True

            # traverse columns leftwards and shifts entries rightwards
            for c in range(3, 0, -1):

                if mat[r][c] == 0 and mat[r][c - 1] != 0:
                    mat[r][c] = mat[r][c - 1]
                    mat[r][c - 1] = 0
                    changed = True
    elif letter.upper() == "S":
        for c in range(4):

            # traverses rows downwards and shifts entries downwards
            for r in range(0, 3):

                if mat[r + 1][c] == 0 and mat[r][c] != 0:
                    mat[r + 1][c] = mat[r][c]
                    mat[r][c] = 0
                    changed = True

            # traverses rows upwards and shifts entries downwards
            for r in range(3, 0, -1):

                if mat[r - 1][c] != 0 and mat[r][c] == 0:
                    mat[r][c] = mat[r - 1][c]
                    mat[r - 1][c] = 0
                    changed = True

    return mat, changed


def merge(mat, letter):
    """Function to merge the cells in the gameboard AFTER compressing

    :param mat: a 2D list representing our 4-by-4 gameboard
    :param letter: a single-character string that indicates the direction that the user has chosen to move in
    :return: the merged gameboard and a variable "changed" that indicates whether the gameboard
    was altered in any way
    """
    changed = False

    # here we determine which way to merge entries (left/right OR up/down)
    if letter.upper() == "A":
        for r in range(4):
            for c in range(0, 3):

                # if current cell has same value as
                # next cell in the row and they
                # are not empty
                if mat[r][c] == mat[r][c + 1] and mat[r][c] != 0:

                    # double current cell value and
                    # empty the next cell
                    mat[r][c] = mat[r][c] + mat[r][c + 1]
                    mat[r][c + 1] = 0
                    changed = True
    elif letter.upper() == "W":
        for c in range(4):
            for r in range(0, 3):

                if mat[r][c] == mat[r + 1][c] and mat[r][c] != 0:

                    mat[r][c] = mat[r][c] + mat[r + 1][c]
                    mat[r][c + 1] = 0
                    changed = True
    elif letter.upper() == "D":
        for r in range(4):
            for c in range(3, 0, -1):

                if mat[r][c] == mat[r][c - 1] and mat[r][c] != 0:

                    mat[r][c] = mat[r][c] + mat[r][c - 1]
                    mat[r][c - 1] = 0
                    changed = True
    elif letter.upper() == "S":

        for c in range(4):
            for r in range(3, 0, -1):

                if mat[r][c] == mat[r - 1][c] and mat[r][c] != 0:

                    mat[r][c] = mat[r][c] + mat[r - 1][c]
                    mat[r - 1][c] = 0
                    changed = True

    return mat, changed


