"""
Dia 10 - Lava Production Facility

Este script resolve as Partes 1 e 2 do desafio do Advent of Code 2023 - Dia 10.

- A entrada é uma matriz topográfica de alturas (0-9).
- Parte 1 calcula o número de posições com altura 9 alcançáveis a partir de cada ponto com altura 0, seguindo um caminho estritamente crescente (de +1 em +1).
- Parte 2 calcula o número de trilhas distintas possíveis a partir de cada ponto com altura 0 até chegar em algum ponto de altura 9, seguindo as mesmas regras.

A estratégia utilizada é busca em profundidade (DFS), sendo otimizada por memoização na Parte 2.
"""

import pathlib
from functools import cache


# Leitura do mapa
def read_map(file_path):
    map_data = []
    with open(file_path, "r") as file:
        for line in file:
            map_data.append([int(char) for char in line.strip()])
    return map_data


# Parte 1 - contar quantos 9s são alcançáveis a partir de cada 0
def part_1(height_map):
    def walk_trail(x: int, y: int, visited_9s: set[tuple[int, int]]):
        height = height_map[y][x]
        if height == 9:
            visited_9s.add((x, y))
            return

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(height_map[0]) and 0 <= ny < len(height_map):
                if height_map[ny][nx] == height + 1:
                    walk_trail(nx, ny, visited_9s)

    total_score = 0
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if height_map[y][x] == 0:
                end_positions = set()
                walk_trail(x, y, end_positions)
                total_score += len(end_positions)

    return total_score


# Parte 2 - contar quantos caminhos distintos existem a partir de cada 0 até algum 9
def part_2(height_map):
    @cache
    def walk_trail(x: int, y: int) -> int:
        height = height_map[y][x]
        if height == 9:
            return 1

        total_paths = 0
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(height_map[0]) and 0 <= ny < len(height_map):
                if height_map[ny][nx] == height + 1:
                    total_paths += walk_trail(nx, ny)
        return total_paths

    total_rating = 0
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if height_map[y][x] == 0:
                total_rating += walk_trail(x, y)

    return total_rating


def main():
    day = 10
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    height_map = read_map(puzzle_path)

    print("Part 1:", part_1(height_map))
    print("Part 2:", part_2(height_map))


if __name__ == "__main__":
    main()
