"""
Simula bytes corrompendo posições em uma memória 2D (71x71).
Parte 1: Após os primeiros 1024 bytes caírem, calcula o menor caminho do canto superior esquerdo ao inferior direito evitando posições corrompidas.
Parte 2: Descobre qual é o primeiro byte que, ao cair, bloqueia completamente o caminho da origem ao destino.
"""

import pathlib
from collections import deque


def load_bytes(file_path, limit=None):
    with open(file_path, "r") as f:
        lines = f.readlines()
        coords = [list(map(int, line.strip().split(","))) for line in lines]
        return coords[:limit] if limit else coords


def create_grid(size, blocked_coords):
    grid = [["."] * size for _ in range(size)]
    for x, y in blocked_coords:
        grid[y][x] = "#"
    return grid


def shortest_path(grid):
    n = len(grid)
    start = (0, 0)
    end = (n - 1, n - 1)
    queue = deque([(0, 0, 0)])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n
                and 0 <= ny < n
                and grid[nx][ny] == "."
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))  # type: ignore
                queue.append((nx, ny, steps + 1))

    return -1


def is_path_possible(grid, start, end):
    n = len(grid)
    queue = deque([start])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n
                and 0 <= ny < n
                and grid[nx][ny] == "."
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False


def find_blocking_byte(grid_size, bytes_list):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    start, end = (0, 0), (grid_size - 1, grid_size - 1)

    for x, y in bytes_list:
        grid[y][x] = "#"
        if not is_path_possible(grid, start, end):
            return f"{x},{y}"

    return None


def part_1(file_path):
    first_1024_bytes = load_bytes(file_path, limit=1024)
    grid = create_grid(71, first_1024_bytes)
    return shortest_path(grid)


def part_2(file_path):
    all_bytes = load_bytes(file_path)
    return find_blocking_byte(71, all_bytes)


def main():
    day = 18
    input_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(input_path))  # 318
    print("Part 2:", part_2(input_path))  # ex: "6,1"


if __name__ == "__main__":
    main()
