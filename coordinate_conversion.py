# coordinate_conversion.py
# function that converts coordinates to their corresponding index number
def cords_to_index(cord):
    column = ord(cord[0]) - 65
    row = int(cord[1:]) - 1

    if 0 <= column <= 9 and 0 <= row <= 9:
        index = row * 10 + column
        return int(index)
    else:
        raise IndexError


# function that converts index numbers to their corresponding coordinates
def index_to_cord(index):
    row = index // 10 + 1
    column = index % 10
    cord = chr(column + 65) + str(row)
    return cord
