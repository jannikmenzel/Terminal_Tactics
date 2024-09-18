# computer_algorithm
from random import randint

from colorama import Fore

from coordinate_conversion import index_to_cord
from global_variables import already_guessed_computer, player_ships
from ship_management import manage_ships


# function that provides randomly generated computer shots
def shoot_randomly():
    while True:
        cord = randint(0, 99)
        # checks if coordinate was already picked before
        if cord not in already_guessed_computer:
            for sublist in player_ships:
                for element in sublist:
                    if element == cord:
                        manage_ships(cord, player_ships)
                        already_guessed_computer.append(cord)
                        return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
            already_guessed_computer.append(cord)
            return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"


# global variables for hunt and target algorithm
current_mode = "hunt"
target_mode = "vertical"
first_hit_position = 0
last_hit_position = 0


# function that provides computer shots based on a hunt and target algorithm
def hunt_and_target():
    global current_mode, target_mode, last_hit_position, first_hit_position

    while True:
        if current_mode == "hunt":
            # Randomly select a position to shoot
            cord = randint(0, 99)

            # Check if the selected position has not been shot before
            if cord not in already_guessed_computer:
                if check_hit_or_miss(cord):
                    last_hit_position = cord
                    first_hit_position = cord
                    current_mode = "target"
                    return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
                else:
                    return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"

        elif current_mode == "target":
            # start with vertical target mode
            if target_mode == "vertical":
                directions_normal_vertical = [-10, 10]

                for direction in directions_normal_vertical:
                    cord = last_hit_position + direction

                    # Check if the new position is within the board boundaries
                    if 0 <= cord <= 99:
                        # Check if the position has not been shot before
                        if cord not in already_guessed_computer:
                            if check_hit_or_miss(cord):
                                last_hit_position = cord
                                return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
                            else:
                                last_hit_position = first_hit_position
                                return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"
                cord = first_hit_position + 10
                if cord not in already_guessed_computer:
                    if check_hit_or_miss(cord):
                        last_hit_position = cord
                        return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
                    else:
                        return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"
                else:
                    target_mode = "horizontal"
                    last_hit_position = first_hit_position

            # continue with horizontal target mode
            if target_mode == "horizontal":
                directions_normal_horizontal = [-1, 1]
                directions_column_a = [1,]
                directions_column_j = [-1]

                if last_hit_position in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
                    directions = directions_column_a
                elif last_hit_position in [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]:
                    directions = directions_column_j
                else:
                    directions = directions_normal_horizontal

                for direction in directions:
                    cord = last_hit_position + direction

                    if 0 <= cord <= 99:
                        # Check if the position has not been shot before
                        if cord not in already_guessed_computer:
                            if check_hit_or_miss(cord):
                                last_hit_position = cord
                                return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
                            else:
                                last_hit_position = first_hit_position
                                return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"
                    cord = first_hit_position + 1
                    if cord not in already_guessed_computer:
                        if check_hit_or_miss(cord):
                            last_hit_position = cord
                            return f"The computer landed a {Fore.RED}Hit{Fore.RESET} on {index_to_cord(cord)}!"
                        else:
                            return f"The computer landed a {Fore.BLUE}Miss{Fore.RESET} on {index_to_cord(cord)}!"

                current_mode = "hunt"
                target_mode = "vertical"


# function that checks whether a cord hit a player ship
def check_hit_or_miss(cord):
    for sublist in player_ships:
        for element in sublist:
            if element == cord:
                manage_ships(cord, player_ships)
                already_guessed_computer.append(cord)
                return True
    already_guessed_computer.append(cord)
    return False
