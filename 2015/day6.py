from pathlib import Path
import numpy as np
from time import sleep, time
puzzle_input = Path(__file__).parent / 'inputday6.txt'

with open(puzzle_input, 'r') as archive:
    instructions = [i.strip() for i in archive.readlines()]

# print(instructions)

def parsing(instructions):
    commands = []
    coords = []
    for i in instructions:
        a, b, c = i.split(',')
        # print(a) #turn off 660
        # print(b) #55 through 986
        # print(c) #197
        coord1 = (int(a.split()[-1]), int(b.split()[0]))
        coord2 = (int(b.split()[-1]), int(c))
        command = ''.join([i for i in a if i.isalpha()])

        commands.append(command)
        coords.append((coord1, coord2))

    return commands, coords


def lights(commands, coords):
    lights = [[False for i in range(1000)] for i in range(1000)]

    for command, (coord1, coord2) in zip(commands, coords):
        print(command, coord1, coord2)
        if command == 'turnon':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    if lights[y][x] == False:
                        lights[y][x] = True

        elif command == 'turnoff':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    if lights[y][x] == True:
                        lights[y][x] = False
        elif command == 'toggle':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    if lights[y][x] == True:
                        lights[y][x] = False
                    else:
                        lights[y][x] = True


    # print(lights[0], lights[-1])
    return sum(sum(row) for row in lights)

        
def part1():
    commands, coords = parsing(instructions)

    resultado = lights(commands, coords)

    print(resultado)

def brightness(commands, coords):
    lights = [[0 for i in range(1000)] for i in range(1000)]

    for command, (coord1, coord2) in zip(commands, coords):
        # print(command, coord1, coord2)

        if command == 'turnon':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    lights[y][x] += 1

        elif command == 'turnoff':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    if lights[y][x] > 0:
                        lights[y][x] -=1

        elif command == 'toggle':

            for y in range(coord1[1], coord2[1]+1):
                for x in range(coord1[0], coord2[0]+1):
                    lights[y][x] +=2

    return sum(sum(row) for row in lights)




commands, coords = parsing(instructions)

total_brightness = brightness(commands, coords)

print(total_brightness)






        