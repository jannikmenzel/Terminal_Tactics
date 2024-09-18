# project.py
import os
import subprocess

from colorama import Fore
from pyfiglet import Figlet

from board_printer import print_board
from game_logic import create_player_ships, create_computer_ships, player_shoot, computer_shoot, winning, start_game


# function that acts as an initializer
def main():
    setup_game()
    play_game()
    end_game()
    # run_simulation("simulation_log.txt", 100)


# function that initializes all necessary operations before the game start
def setup_game():
    start_game()
    print_board("player_board")
    print(f"Please place your {Fore.LIGHTRED_EX}ships{Fore.RESET}! "
          f"E.g. {Fore.LIGHTBLUE_EX}A1-A5, C4-G4, E8-I8{Fore.RESET}. Note the individual ship lengths!")
    create_player_ships()
    create_computer_ships()
    print_board("game_board")
    print(f"Please enter a {Fore.LIGHTRED_EX}coordinate{Fore.RESET}! "
          f"E.g. {Fore.LIGHTBLUE_EX}A1, D4 or E6{Fore.RESET}")


# function that initializes all necessary operations during the game inside a runtime loop
def play_game():
    while winning() != "You won!" and winning() != "You loose!":
        print(player_shoot())
        print_board("game_board")
        print(computer_shoot())


# function that initializes the end of the game
def end_game():
    f = Figlet(font="doom")
    print(f.renderText(winning()))
    print(f"Press the {Fore.LIGHTRED_EX}ENTER{Fore.RESET} key to exit")
    input()
    exit()


# function that can test the computer algorithm with simulations
def run_simulation(output_file, iterations):
    total_shots = 0

    with open(output_file, 'w') as file:
        for i in range(iterations):
            process = subprocess.Popen(["python", "simulation.py"], stdout=subprocess.PIPE,
                                       text=True, env=os.environ.copy())
            stdout, stderr = process.communicate()
            file.write(f"Iteration {i + 1} \n{stdout}\n")

            lines = stdout.strip().split('\n')
            total_shots += int(lines[0].split()[0])

        file.write(f"\ntotal shot average: {total_shots / iterations}")


if __name__ == "__main__":
    main()
