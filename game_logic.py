# game_logic.py
from random import randint

from colorama import Fore
from pyfiglet import Figlet

from board_printer import print_board
from computer_algorithm import hunt_and_target
from coordinate_conversion import cords_to_index
from global_variables import player_ships, computer_ships, already_guessed_player, hit, miss
from ship_management import manage_ships, manage_sinking_ships


# class managing the creation of player ship objects
class PlayerShip:
    # init method containing variables for the ship's coordinates and length
    def __init__(self, cords, length):
        self.cords = cords
        self.length = length

    # method to check if the length of the given coordinates match the length of the ship
    def check_length(self):
        if len(self.cords) == self.length and self.cords[0] != self.cords[1]:
            return True
        else:
            return False

    # function to autofill the coordinates in horizontal direction
    @staticmethod
    def fill_missing_horizontal(cords):
        result = []
        for i in range(len(cords) - 1):
            result.append(cords[i])
            if cords[i] + 1 != cords[i + 1]:
                result.extend(range(cords[i] + 1, cords[i + 1]))

        result.append(cords[-1])

        return result

    # function to autofill the coordinates in vertical direction
    @staticmethod
    def fill_missing_vertical(cords):
        result = []
        for i in range(len(cords) - 1):
            result.append(cords[i])
            if cords[i] + 10 != cords[i + 1]:
                result.extend(range(cords[i] + 10, cords[i + 1], 10))

        result.append(cords[-1])

        return result

    # cords getter
    @property
    def cords(self):
        return self._cords

    # cords setter
    @cords.setter
    def cords(self, cords: list):
        try:
            if [*cords[0]][1] == [*cords[1]][1]:
                for i in range(2):
                    cords[i] = cords_to_index(cords[i])
                cords = sorted(cords)
                cords = self.fill_missing_horizontal(cords)
                self._cords = cords
            elif [*cords[0]][0] == [*cords[1]][0]:
                for i in range(2):
                    cords[i] = cords_to_index(cords[i])
                cords = sorted(cords)
                cords = self.fill_missing_vertical(cords)
                self._cords = cords
            else:
                self._cords = None
        except (ValueError, IndexError, KeyError):
            self._cords = None


# class managing the creation of Computer ship objects
class ComputerShip:
    # init method containing variables for the ship's coordinates and length
    def __init__(self, length):
        self.length = length
        self.cords = None

    # method to generate random coordinates matching the given restrictions
    def generate_cords(self, toplist):
        while True:
            cords = []
            orientation = self.random_orientation()
            # generate random coordinates for horizontal orientation
            if orientation == "horizontal":
                row = randint(1, 10)
                column = randint(1, self.length)
                start = self.digits_to_index(row, column)

                for i in range(self.length):
                    cords.append(start)
                    start += 1
            # generate random coordinates for vertical orientation
            if orientation == "vertical":
                row = randint(1, self.length)
                column = randint(1, 10)
                start = self.digits_to_index(row, column)

                for i in range(self.length):
                    cords.append(start)
                    start += 10

            # append coordinates to global computer_ships list
            if check_occupied(cords, self.length, toplist, False):
                toplist.append(cords)
                self.cords = cords
                return cords

    # cords getter
    @property
    def cords(self):
        return self._cords

    # cords setter
    @cords.setter
    def cords(self, new_cords):
        self._cords = new_cords

    # function to generate a random orientation
    @staticmethod
    def random_orientation():
        hor_or_ver = randint(0, 1)
        match hor_or_ver:
            case 0:
                return "horizontal"
            case 1:
                return "vertical"

    # function to convert the given coordinates(in numeric form) to an index number
    @staticmethod
    def digits_to_index(row, column):
        return (row - 1) * 10 + (column - 1)


# function which creates the player ship objects with corresponding variable inputs
def create_player_ships():
    create_ship("carrier", 5, Fore.LIGHTRED_EX)
    create_ship("battleship", 4, Fore.LIGHTBLUE_EX)
    create_ship("cruiser", 3, Fore.LIGHTGREEN_EX)
    create_ship("submarine", 3, Fore.LIGHTMAGENTA_EX)
    create_ship("destroyer", 2, Fore.LIGHTYELLOW_EX)


# function that manages the input loop and error handling
def create_ship(ship_name, length, color):
    while True:
        try:
            user_input = input(f"Place your {color}{ship_name}{Fore.RESET} ({length}): ").strip().upper().split("-")
            ship = PlayerShip(user_input, length)
            if ship.cords is not None and ship.check_length() and check_occupied(ship.cords, length, player_ships,
                                                                                 True):
                player_ships.append(ship.cords)
                print_board("player_board")
                break
            else:
                print("Invalid Input")
        except TypeError:
            pass
            print("Invalid Input")


# function that creates the computer ship objects
def create_computer_ships():
    computer_carrier = ComputerShip(5)
    computer_carrier.generate_cords(computer_ships)

    computer_battleship = ComputerShip(4)
    computer_battleship.generate_cords(computer_ships)

    computer_cruiser = ComputerShip(3)
    computer_cruiser.generate_cords(computer_ships)

    computer_submarine = ComputerShip(3)
    computer_submarine.generate_cords(computer_ships)

    computer_destroyer = ComputerShip(2)
    computer_destroyer.generate_cords(computer_ships)


# function that creates the player ship objects randomly
def create_ships_for_simulation():
    simulation_carrier = ComputerShip(5)
    simulation_carrier.generate_cords(player_ships)

    simulation_battleship = ComputerShip(4)
    simulation_battleship.generate_cords(player_ships)

    simulation_cruiser = ComputerShip(3)
    simulation_cruiser.generate_cords(player_ships)

    simulation_submarine = ComputerShip(3)
    simulation_submarine.generate_cords(player_ships)

    simulation_destroyer = ComputerShip(2)
    simulation_destroyer.generate_cords(player_ships)


# method to check if a ship can be placed on given coordinates
def check_occupied(cords, length, toplist, printing):
    for i in range(length):
        # check if any other ships interfere with the given coordinates
        if any(cords[i] in sublist for sublist in toplist):
            if printing:
                print("You've already placed a ship on one of the squares!")
            return False
        else:
            if cords[i] in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
                for offset in [1, 10, -10]:
                    neighbor_square = cords[i] + offset
                    if any(neighbor_square in sublist for sublist in toplist):
                        if printing:
                            print("Ships must have at least one square space between them!")
                        return False
            elif cords[i] in [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]:
                for offset in [-1, 10, -10]:
                    neighbor_square = cords[i] + offset
                    if any(neighbor_square in sublist for sublist in toplist):
                        if printing:
                            print("Ships must have at least one square space between them!")
                        return False
            else:
                for offset in [-1, 1, -10, 10]:
                    neighbor_square = cords[i] + offset
                    if any(neighbor_square in sublist for sublist in toplist):
                        if printing:
                            print("Ships must have at least one square space between them!")
                        return False
    return True


# function that asks the player for an input coordinate to shoot
def player_shoot():
    while True:
        try:
            raw_cord = input("Input: ").strip().upper()
            cord = cords_to_index(raw_cord)
            # checks if coordinate was already picked before
            if cord not in already_guessed_player:
                already_guessed_player.append(cord)
                for sublist in computer_ships:
                    for element in sublist:
                        if not element == cord:
                            continue
                        else:
                            manage_ships(cord, computer_ships)
                            # if the given coordinate was a hit, it is appended to the hit list
                            # in order to be displayed on the board
                            hit.append(cord)
                            return f"{Fore.RED}Hit{Fore.RESET} {manage_sinking_ships(computer_ships)}!"
                miss.append(cord)
                return f"{Fore.BLUE}Miss{Fore.RESET}!"
            # error handling
            else:
                print("You've already guessed that!")
        except (ValueError, IndexError):
            pass
            print("Not a valid coordinate!")


# function that randomly generates a coordinate to shoot for the computer
def computer_shoot():
    return hunt_and_target()


# function that ends the runtime loop and displays the winner
def winning():
    if all(all(element == "hit" for element in sublist) for sublist in computer_ships):
        return "You won!"
    elif all(all(element == "hit" for element in sublist) for sublist in player_ships):
        return "You loose!"


# function that implements the title screen
def start_game():
    f = Figlet(font="doom")
    print(f.renderText("Battleship"))
    print(f"Press {Fore.LIGHTRED_EX}ENTER{Fore.RESET} to continue")
    input()
    print("\n\n")
