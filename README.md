# Terminal Tactics: Battleship

## Video Demo

[Link to Video Demo](<https://youtu.be/TrsPZBQHl6k>)

## Description

>"Terminal Tactics: Battleship" is a console-based implementation of the classic game Battleship. Wherein you are able
to set up your own fleet and play against the computer. The provided code also comes with the option to run simulated
games in which the computers' overall performance can be statistically analyzed and displayed.

### Project Structure

The project consists of a main file as well as several modules:

>- **`project.py`:** This file contains most of the key elements needed to set up, play, and end the game. It not only
  manages the runtime loop but also implements the option to run simulations.


>- **`board_printer.py`:** The board_printer module is responsible for displaying the game board with all of its
  components during the setup and play phases.


>- **`simulation.py`:** The simulation module is responsible for handling the game simulation to test the
  computer shooting algorithms performance. It is executed via the `project.py` file and thereby creates a text file
  containing the collected data.


>- **`game_logic.py`:** The game logic module defines the "PlayerShip" class as well as the "ComputerShip" class. It
  also contains the functions necessary to set up and play the game.


>- **`ship_management.py`:** The ship management module is an extension of the `game_logic.py` file and manages the
  updating of ship status during the game


>- **`coordinate_conversion.py`:** The coordinate conversion module handles the conversion of coordinates in the format
  [A1] - [J10] to their corresponding index number [0] - [99]


>- **`computer_algorithm.py`:** The computer algorithm module contains the code behind the computer the player plays
  against. The algorithm is called "Hunt and Target".


>- **`test_project.py`:** The test project module implements a number of tests for several modules and ensures the
  functionality of the game.

### Design Choices

#### Object-Oriented Approach

>This project adopts an object-oriented approach to maintain a certain flexibility within the games' logic.
Therefor, two classes named `PlayerShip` and `ComputerShip` implement all ships as objects with a length of min 2 and
max 5 as well as their corresponding coordinates. With the help of classes the five different ship types: carrier,
battleship, cruiser, submarine, and destroyer can easily be created and modified.

#### Use of Libraries

>The project also utilizes external libraries such as the `colorama` library for colorful text output or the
`pyfiglet` library for ASCII art rendering. This overall provides a user-friendly game interface. Especially in the
context of the project being a console-based game, the prioritization of simplicity and functionality over graphical
complexity makes it fun to play.

#### Modular Structure

>The separation of functions into individual modules ensures that the code is clear to understand. Without this
measure, the project would hold around 650 individual lines of code. The modular structure also maintains a logical
separation of the codes' functionality into different fields.

#### Simulations

>Another feature of my program is the ability to run simulations to measure the computers' efficiency. The build in
algorithm works according to the "Hunt and Target" principle which mirrors the human way of playing the game. With an
average of 65 shots until winning, the computer comes close to the human average of 60–70 shots.

### Requirements

>- Check any required dependencies: `requirements.txt`

