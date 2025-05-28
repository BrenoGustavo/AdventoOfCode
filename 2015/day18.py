from pathlib import Path
from copy import deepcopy
import time
puzzle_input = Path(__file__).parent / 'inputday18.txt'
with open(puzzle_input, 'r') as archive:
    lights = [[1 if j =='#' else 0 for j in i.strip() ] for i in archive.readlines()]


def part1():
    def animate_ligts(light_grid, n):

        if n <1:
            return light_grid

        new_grid = deepcopy(light_grid)

        neighbours = [
            (-1, -1), 
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for y in range(len(light_grid)):
            for x in range(len(light_grid[y])):
                # print(y, x)
                lights_on = 0

                for coord in neighbours:
                    ny, nx = y + coord[0], x + coord[1]
                    if 0<= ny < len(light_grid) and 0 <= nx < len(light_grid[y]):

                        if light_grid[ny][nx] == 1:
                            lights_on +=1
                # print(f'Number of ligts on: {lights_on}')

                if light_grid[y][x] == 1:
                    if lights_on not in [2, 3]:
                        new_grid[y][x] = 0

                elif light_grid[y][x] == 0 and lights_on == 3:
                    new_grid[y][x] = 1

        return animate_ligts(new_grid, n-1)




    LIGHTS = animate_ligts(lights, 100)
    sum_lights_on = sum(sum(i) for i in LIGHTS)
    print(sum_lights_on)

def part2():
    M = len(lights) - 1
    lights[0][0], lights[0][M], lights[M][0], lights[M][M] = 1, 1, 1, 1

    def animate_ligts(light_grid, n):

        if n <1:
            return light_grid

        new_grid = deepcopy(light_grid)

        neighbours = [
            (-1, -1), 
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for y in range(len(light_grid)):
            for x in range(len(light_grid[y])):
                if (y, x) in [(0, 0), (0, len(lights) - 1), (len(lights) - 1, 0), (len(lights) - 1, len(lights) - 1)]:
                    continue
                lights_on = 0

                for coord in neighbours:
                    ny, nx = y + coord[0], x + coord[1]
                    if 0<= ny < len(light_grid) and 0 <= nx < len(light_grid[y]):

                        if light_grid[ny][nx] == 1:
                            lights_on +=1
                # print(f'Number of ligts on: {lights_on}')

                if light_grid[y][x] == 1:
                    if lights_on not in [2, 3]:
                        new_grid[y][x] = 0

                elif light_grid[y][x] == 0 and lights_on == 3:
                    new_grid[y][x] = 1

        return animate_ligts(new_grid, n-1)
    
    LIGHTS = animate_ligts(lights, 100)
    sum_lights_on = sum(sum(i) for i in LIGHTS)
    print(sum_lights_on)

part2()






