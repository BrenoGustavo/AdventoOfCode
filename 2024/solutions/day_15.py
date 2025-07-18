"""
Simulação de movimentação em um grid com obstáculos, caixas e instruções de movimento.
A Parte 1 executa os passos simples em um grid básico.
A Parte 2 envolve empurrar caixas (representadas por colchetes) que se comportam de forma especial,
incluindo movimentações em cadeia e empurrões verticais e horizontais.
"""

import argparse
import pathlib

DIRECTION_MAP = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def read_input(filename):
    with open(filename, "r") as file:
        grid = []
        steps = []
        for line in file:
            if len(line.strip()) == 0:
                break
            grid.append(line.strip())
        for line in file:
            steps.append(line.strip())
    return grid, "".join(steps)


def analyze_grid_str(grid_str):
    start_pos = None
    for r, row in enumerate(grid_str):
        c = row.find("@")
        if c != -1:
            start_pos = (r, c)
            break
    return [list(row) for row in grid_str], start_pos


def expand_grid_str(grid_str):
    new_grid = []
    for row in grid_str:
        line = (
            row.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        )
        new_grid.append(line)
    return new_grid


def calculate_gps_sum(grid):
    total = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "O" or cell == "[":
                total += (100 * r) + c
    return total


def part_1(grid_str, steps):
    grid, (r, c) = analyze_grid_str(grid_str)  # type: ignore
    for step in steps:
        dr, dc = DIRECTION_MAP[step]
        nr, nc = r + dr, c + dc

        if grid[nr][nc] == "#":
            continue
        if grid[nr][nc] == ".":
            grid[r][c] = "."
            grid[nr][nc] = "@"
            r, c = nr, nc
            continue

        peek_r, peek_c = nr + dr, nc + dc
        while grid[peek_r][peek_c] not in {".", "#"}:
            peek_r += dr
            peek_c += dc

        if grid[peek_r][peek_c] == ".":
            grid[peek_r][peek_c] = "O"
            grid[r][c] = "."
            grid[nr][nc] = "@"
            r, c = nr, nc

    return calculate_gps_sum(grid)


def part_2(grid_str, steps):
    expanded_grid_str = expand_grid_str(grid_str)
    grid, (r, c) = analyze_grid_str(expanded_grid_str)  # type: ignore

    for step in steps:
        dr, dc = DIRECTION_MAP[step]
        nr, nc = r + dr, c + dc

        if grid[nr][nc] == "#":
            continue
        if grid[nr][nc] == ".":
            grid[r][c] = "."
            grid[nr][nc] = "@"
            r, c = nr, nc
            continue

        if dc != 0:  # Horizontal push
            peek_c = nc
            while grid[r][peek_c] not in {".", "#"}:
                peek_c += dc
            if grid[r][peek_c] == "#":
                continue
            shift_c = peek_c
            while shift_c != c - dc:
                grid[r][shift_c] = grid[r][shift_c - dc]
                shift_c -= dc
            grid[r][c] = "."
            c = nc

        else:  # Vertical push

            def get_shift_chain():
                queue = [(r, c)]
                visited = {(nr, nc): grid[nr][nc]}
                while queue:
                    cur_r, cur_c = queue.pop(0)
                    peek_r, peek_c = cur_r + dr, cur_c + dc

                    if grid[peek_r][peek_c] == "#":
                        return None
                    if grid[peek_r][peek_c] == ".":
                        continue

                    visited[(peek_r, peek_c)] = grid[peek_r][peek_c]
                    if grid[peek_r][peek_c] == "[":
                        visited[(peek_r, peek_c + 1)] = grid[peek_r][peek_c + 1]
                        queue.append((peek_r, peek_c))
                        queue.append((peek_r, peek_c + 1))
                    elif grid[peek_r][peek_c] == "]":
                        visited[(peek_r, peek_c - 1)] = grid[peek_r][peek_c - 1]
                        queue.append((peek_r, peek_c))
                        queue.append((peek_r, peek_c - 1))

                return visited

            pieces_to_shift = get_shift_chain()
            if pieces_to_shift:
                for pr, pc in pieces_to_shift:
                    grid[pr][pc] = "."
                for (pr, pc), val in pieces_to_shift.items():
                    grid[pr + dr][pc + dc] = val

                grid[r][c] = "."
                grid[nr][c] = "@"
                r, c = nr, nc

    return calculate_gps_sum(grid)


def main():
    day = 15
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    grid_str, steps = read_input(puzzle_path)

    result_1 = part_1(grid_str, steps)
    print("Part 1:", result_1)

    result_2 = part_2(grid_str, steps)
    print("Part 2:", result_2)


if __name__ == "__main__":
    main()
