# simulation.py
from game_logic import create_computer_ships, computer_shoot, winning, create_ships_for_simulation


# function that initializes a simulation
def simulate():
    total_shots = 0

    create_computer_ships()
    create_ships_for_simulation()

    while winning() != "You won!" and winning() != "You loose!":
        computer_shoot()

        total_shots += 1

    print(f"{total_shots} total shots")


simulate()
