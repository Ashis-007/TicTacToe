import os

line1 = None
line2 = None
line3 = None
line = "     |    |     "
separator = "----------------"

my_list1 = list("     |    |     ")
my_list2 = list("     |    |     ")
my_list3 = list("     |    |     ")

row1 = (7, 8, 9)
row2 = (4, 5, 6)
row3 = (1, 2, 3)

winner = None
is_draw = None


# This will check the game status
# at each iteration
def is_game_over():
    pass


# Game starts here
def start_game():
    while True:
        position_1 = input("Choose your position (1-9): ")
        set_marker(position_1, marker1)

        if is_game_over():
            break

        position_2 = input("Player 2: Choose your position (1,9): ")
        set_marker(position_2, marker2)

        if is_game_over():
            break


print("Welcome to Tic Tac Toe!")

choice = input("Are you ready? ")
if choice == "Yes" or "yes":
    marker1 = input("Player 1: Do you want to be X or O? ")
    if marker1 == "X":
        marker2 = "O"
    else:
        marker2 = "X"

    start_game()
else:
    print("You are expected to be ready! Game is started!")
    # start_game()


# Clear the screen after each iteration
def clear_screen():
    _ = os.system("cls")


def set_marker(pos, marker):
    global my_list1, my_list2, my_list3
    global line1, line2, line3

    if pos in row1:
        pass
    if pos in row2:
        pass
    else:
        pass

    line1 = "".join(my_list1)
    line2 = "".join(my_list2)
    line3 = "".join(my_list3)


# Draws the board
def draw_board():
    print(line)
    print(line1)
    print(separator)
    print(line)
    print(line2)
    print(separator)
    print(line3)
    print(line)

