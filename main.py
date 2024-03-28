import numpy as np

to_continue = True
position = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
n = 0
mark = ""
column = 0
row = 0


def print_map(map_position):
    print("Player 1: X       Player 2: O")
    print("             COLUMNS:")
    print("            1   2   3")
    print("          --v---v---v--")
    print(f"      1 > | {map_position[0][0]} | {map_position[0][1]} | {map_position[0][2]} |")
    print(f"ROWS: 2 > | {map_position[1][0]} | {map_position[1][1]} | {map_position[1][2]} |")
    print(f"      3 > | {map_position[2][0]} | {map_position[2][1]} | {map_position[2][2]} |")
    print("          -------------")


def is_winner(map_position, player_mark):
    # map_position[row][column]
    for _ in range(3):
        if map_position[_][0] == player_mark and map_position[_][1] == player_mark and map_position[_][2] == player_mark:
            return True
        elif map_position[0][_] == player_mark and map_position[1][_] == player_mark and map_position[2][_] == player_mark:
            return True
    if map_position[0][2] == player_mark and map_position[1][1] == player_mark and map_position[2][0] == player_mark:
        return True
    elif map_position[0][0] == player_mark and map_position[1][1] == player_mark and map_position[2][2] == player_mark:
        return True


print_map(position)
while to_continue:
    valid = False
    # Check which player has to go now
    n = n + 1
    if n % 2 == 0:
        player = 2
        mark = "O"
    else:
        player = 1
        mark = "X"
    print("______________________________________________________________")
    # Ask for the player's input
    while not valid:
        valid_choice = False
        # Make sure the player makes a valid choice
        while not valid_choice:
            try:
                column = int(input(f"PLAYER {player}, CHOOSE A COLUMN: "))
                row = int(input(f"PLAYER {player}, CHOOSE A ROW: "))
            except ValueError:
                print("PLEASE ENTER A VALID NUMBER.")
            else:
                if (column < 0) or (column > 3) or (row < 0) or (row > 3):
                    print("PLEASE ENTER A NUMBER FROM 1 TO 3.")
                else:
                    valid_choice = True
        # Make sure the choice he made is available
        if position[row - 1][column - 1] == " ":
            valid = True
        else:
            print("THE SPOT IS ALREADY TAKEN, PLEASE MAKE ANOTHER CHOICE")
    # Edit the map
    position[row - 1][column - 1] = mark

    # Draw the map with new values
    print_map(position)

    # Check for a winner
    if is_winner(position, mark):
        print(f"PLAYER {player} WON!")
        to_continue = False
