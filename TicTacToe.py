import os

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
    start_game()

line1 = None
line2 = None
line3 = None
my_list = list("     |    |     ")

row3 = (7, 8, 9)
row2 = (4, 5, 6)
row1 = (1, 2, 3)

winner = None
is_draw = None


# Draws the board
def draw_board():
    for i in range(1, 9):
        if i % 3 == 0:
            print("----------------")
            continue
        else:
            print("     |    |     ")


# Clear the screen after each iteration
def clear_screen():
    _ = os.system("cls")


# Game starts here
def start_game():
    while True:
        position_1 = input("Choose your position (1-9): ")
        player1()

        if is_game_over():
            break

        position_2 = input("Player 2: Choose your position (1,9): ")
        player2()

        if is_game_over():
            break


def player1():
    pass


def player2():
    pass


# This will check the game status
# at each iteration
def is_game_over():
    pass

