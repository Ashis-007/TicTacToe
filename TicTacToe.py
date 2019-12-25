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
    #horizontal
    horizontal_condition = line1[3] == line1[8] == line1[13] != " " or line2[3] == line2[8] == line2[13] != " " or line3[3] == line3[8] == line3[13] != " " 

    #vertical
    vertical_condition = line1[3] == line2[3] == line3[3] != " " or line1[8] == line2[8] == line3[8] != " " or line1[13] == line2[13] == line3[13] != " "

    #diagonal
    diagonal_condition = line1[3] == line2[8] == line3[13] != " " or line3[3] == line2[8] == line1[13] != " "

    return horizontal_condition or vertical_condition or diagonal_condition


def set_marker(pos, marker):
    global my_list1, my_list2, my_list3
    global line1, line2, line3

    if pos in row1:
        if pos == 7:
            my_list1[3] = marker
        elif pos == 8:
            my_list1[8] = marker
        else:
            my_list1[13] = marker
    elif pos in row2:
        if pos == 4:
            my_list2[3] = marker
        elif pos == 5:
            my_list2[8] = marker
        else:
            my_list2[13] = marker
    elif pos in row3:
        if pos == 1:
            my_list3[3] = marker
        elif pos == 2:
            my_list3[8] = marker
        else:
            my_list3[13] = marker
    else:
        print("Wrong Input")

    line1 = "".join(my_list1)
    line2 = "".join(my_list2)
    line3 = "".join(my_list3)

    draw_board()


# Draws the board
def draw_board():
    global my_list1, my_list2, my_list3
    global line1, line2, line3

    print(line)
    print(line1)
    print(separator)
    print(line)
    print(line2)
    print(separator)
    print(line3)
    print(line)



# Game starts here
def start_game():
    count = 0
    global winner
    while count <= 9:
        position_1 = int(input("Choose your position (1-9): "))
        set_marker(position_1, marker1)

        if is_game_over():
            winner = "Player 1"
            break
        count += 1

        if count == 9:
            is_draw = True
            break
    
        position_2 = int(input("Player 2: Choose your position (1,9): "))
        set_marker(position_2, marker2)

        if is_game_over():
            winner = "Player 2"
            break
        count += 1

        if count == 9:
            is_draw = True
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

if is_draw:
    print("It is a draw!")
else:
    print(f"{winner} wins!")



# Clear the screen after each iteration
def clear_screen():
    _ = os.system("cls")

