# board_printer.py
from colorama import Fore

from global_variables import player_ships, hit, miss


# function that takes either "game_board" or "player_board" as input argument
def print_board(usage):
    # headline of the board
    print("--------------------------------")
    print("⚓  A  B  C  D  E  F  G  H  I  J")

    # colors for corresponding ships
    colors = [Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX]

    # outer loop for rows
    for x in range(10):
        print(str(x + 1).zfill(2), "", end="")

        # inner loop for columns
        for y in range(10):
            index = x * 10 + y  # Correct index calculation
            # displays game board for ship creation
            if usage == "game_board":
                if index in hit:
                    print(f" {Fore.RED}x{Fore.RESET} ", end="")
                elif index in miss:
                    print(f" {Fore.BLUE}O{Fore.RESET} ", end="")
                else:
                    print(" _ ", end="")

            # displays game board during the shooting phase
            elif usage == "player_board":
                ship_color = None
                for i, sublist in enumerate(player_ships):
                    if index in sublist:
                        ship_color = colors[i]
                        break
                if ship_color:
                    print(f" {ship_color}I{Fore.RESET} ", end="")
                else:
                    print(" _ ", end="")

        # prints new line after every column
        print("")
