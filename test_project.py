# test_project.py
import pytest
from coordinate_conversion import *
from game_logic import check_occupied, PlayerShip


# Test for coordinate_conversion
def test_index_to_cord():
    assert index_to_cord(0) == "A1"
    assert index_to_cord(99) == "J10"


def test_cords_to_index():
    assert cords_to_index("A1") == 0
    assert cords_to_index("J10") == 99
    with pytest.raises(IndexError):
        cords_to_index("A11")


# Test for game logic
def test_check_occupied():
    assert check_occupied([1, 2, 3], 3, [[], [], []], False) is True
    assert check_occupied([1, 2, 3], 3, [[1, 2, 3], [], []], False) is False


def test_PlayerShip_fill_missing_horizontal():
    assert PlayerShip.fill_missing_horizontal([1, 3]) == [1, 2, 3]
    assert PlayerShip.fill_missing_horizontal([1, 4]) == [1, 2, 3, 4]
    assert PlayerShip.fill_missing_horizontal([20, 24]) == [20, 21, 22, 23, 24]


def test_PlayerShip_fill_missing_vertical():
    assert PlayerShip.fill_missing_vertical([0, 20]) == [0, 10, 20]
    assert PlayerShip.fill_missing_vertical([0, 30]) == [0, 10, 20, 30]
    assert PlayerShip.fill_missing_vertical([49, 69]) == [49, 59, 69]
