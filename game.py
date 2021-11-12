# importing the logic.py file
# where we have written all the functions for the game
import logic

# First create the 4-by-4 gameboard
mat = logic.start_game()

# print the 4-by-4 gameboard
for row in mat:
    print(row)

while True:
    # taking the user input
    # for next step (NOTE: the upper() function transforms the user's input to uppercase)
    inp = input("Enter a command. \n (W = up, A = left, S = down, D = right): ").upper()

    # create a list of the user's valid inputs
    validInputs = ["W", "A", "S", "D"]

    # keeps prompting the user to enter a command until it is valid (IF it is invalid)
    while inp not in validInputs:
        print("Invalid command entered.")
        inp = input("Enter a command. \n (W = up, A = left, S = down, D = right): ").upper()

    # first compress the matrix
    mat, flag1 = logic.compress(mat, inp)

    # then merge the cells
    mat, flag2 = logic.merge(mat, inp)

    # check if the grid is changed in any way
    flag = flag1 or flag2

    # compress the cells again (NOTE: var is useless)
    mat, var = logic.compress(mat, inp)

    # get the current state and print it
    status = logic.game_state(mat)
    print("\n\n")
    print(status)

    # if game not over then continue
    # and add a new two
    if status == "KEEP GOING!":
        logic.add_new_2(mat)
    # otherwise break the loop
    else:
        break

    # print the matrix after each
    # move.
    print("\n\n")
    for row in mat:
        print(row)


maxVal = 0

# Your score is the highest number you got on your grid
for r in range(4):
    for c in range(4):
        if mat[r][c] > maxVal:
            maxVal = mat[r][c]

print("Your final score was:", maxVal)

