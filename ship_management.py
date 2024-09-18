# ship_management.py
from colorama import Fore

from global_variables import sunken_index


# function that changes hit coordinate in either computer_ships or player_ships to "hit"
def manage_ships(hit_cord, toplist):
    for sublist in toplist:
        for i in range(len(sublist)):
            if sublist[i] == hit_cord:
                sublist[i] = "hit"
                break


# function that shows when every coordinate of a ship was hit
def manage_sinking_ships(toplist):
    for index, sublist in enumerate(toplist):
        if all(element == "hit" for element in sublist):
            # global sunken_index list to check whether a ship has been displayed as sunken before
            if index not in sunken_index:
                sunken_index.append(index)
                return f"{Fore.RED}sunk{Fore.RESET}"
    return ""
