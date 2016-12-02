"""
This is a simplest-solution attempt at solving Advent of Code Exercise 1 for December 1, 2016
"""

INPUT = """
R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4,
R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2,
L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5,
R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4,
L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3,
R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3
"""


ORIENTATIONS = [
    [-1, 0],  # North
    [0, 1],  # East
    [1, 0],  # South
    [0, -1],  # West
]

NORTH = 0


def main():
    coordinate_y = 0
    coordinate_x = 0
    orientation = NORTH
    instructions = INPUT.replace('\n', '').replace(' ', '').split(',')
    for instruction in instructions:
        change = 1 if instruction[0] == 'R' else -1
        distance = int(instruction[1:])
        orientation = (orientation + change) % 4
        movement = [o * distance for o in ORIENTATIONS[orientation]]
        coordinate_x += movement[1]
        coordinate_y += movement[0]
    print 'Santa is {} blocks away'.format(abs(coordinate_x) + abs(coordinate_y))

if __name__ == '__main__':
    main()
