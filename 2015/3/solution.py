"""--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and
so his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the
east.
^>v< delivers presents to 4 houses in a square, including twice to the house at
his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2
houses.
Your puzzle answer was 2081.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the
elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa
goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back
where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction
and Robo-Santa going the other.
Your puzzle answer was 2341.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os


def count_houses(data):
    x, y = 0, 0
    houses = dict()
    for instruction in data:
        house = (x, y)
        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1

        if instruction == "^":
            y += 1
        elif instruction == "v":
            y -= 1
        elif instruction == ">":
            x += 1
        elif instruction == "<":
            x -= 1

    return len(houses)


def count_houses_with_robosanta(data):
    santas = ([0, 0], [0, 0])
    houses = dict()
    for i, instruction in enumerate(data):
        santa = i % 2
        house = tuple(santas[santa])
        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1

        if instruction == "^":
            santas[santa][1] += 1
        elif instruction == "v":
            santas[santa][1] -= 1
        elif instruction == ">":
            santas[santa][0] += 1
        elif instruction == "<":
            santas[santa][0] -= 1

    return len(houses)


# Extra method - counts houses depending on amount of santas
def count_houses_dep_on_santas(data, santas_amount):
    santas = list()
    houses = dict()
    for j in range(santas_amount):
        santas.append([0, 0])
    for i, instruction in enumerate(data):
        santa = i % len(santas)
        house = tuple(santas[santa])
        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1

        if instruction == "^":
            santas[santa][1] += 1
        elif instruction == "v":
            santas[santa][1] -= 1
        elif instruction == ">":
            santas[santa][0] += 1
        elif instruction == "<":
            santas[santa][0] -= 1

    return len(houses)


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "input")
    with open(input_path, "r") as input_file:
        instructions = input_file.read()

    print(count_houses(data=instructions))
    print(count_houses_with_robosanta(data=instructions))
    print(count_houses_dep_on_santas(data=instructions, santas_amount=1))
    print(count_houses_dep_on_santas(data=instructions, santas_amount=2))
