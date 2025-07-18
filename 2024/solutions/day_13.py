"""
Dia 13 - Claw Contraption 🎯

Este desafio envolve resolver um sistema de equações diofantinas lineares para descobrir
quantas vezes devemos pressionar os botões A e B (com custos diferentes) para alcançar
a posição exata do prêmio em uma garra.

- Parte 1: Calcula o menor custo (em tokens) necessário para alcançar o prêmio com movimentos pequenos.
- Parte 2: Adiciona um deslocamento de 10^13 nas posições dos prêmios, exigindo soluções com grandes números.

O problema essencial é resolver:

    a1*A + b1*B = prize_y
    a2*A + b2*B = prize_x

Buscando soluções inteiras e não-negativas para A e B.
"""

import pathlib
import numpy as np
from sympy import Matrix


def parse_input(file_path: pathlib.Path, add_offset=False):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    blocks = [
        lines[i : i + 3] for i in range(0, len(lines), 3) if len(lines[i : i + 3]) == 3
    ]

    machines = []
    for block in blocks:
        try:
            a_x = int(block[0].split(",")[0].split("+")[1])
            a_y = int(block[0].split(",")[1].split("+")[1])
            b_x = int(block[1].split(",")[0].split("+")[1])
            b_y = int(block[1].split(",")[1].split("+")[1])
            p_x = int(block[2].split(",")[0].split("=")[1])
            p_y = int(block[2].split(",")[1].split("=")[1])
        except (IndexError, ValueError) as e:
            print(f"Erro ao processar bloco:\n{block}\nErro: {e}")
            continue  # pula blocos mal formatados

        if add_offset:
            p_x += 10**13
            p_y += 10**13

        machines.append(((a_x, a_y), (b_x, b_y), (p_x, p_y)))

    return machines


def solve_diophantine_numpy(a1, b1, c1, a2, b2, c2):
    matrix = np.array([[a1, b1], [a2, b2]])
    constants = np.array([c1, c2])

    if np.linalg.det(matrix) == 0:
        return None

    solution = np.linalg.solve(matrix, constants)
    tolerance = 1e-9

    if not all(abs(val - round(val)) < tolerance for val in solution):
        return None

    A, B = map(round, solution)
    if A < 0 or B < 0:
        return None

    return A, B


def solve_diophantine_sympy(a1, b1, c1, a2, b2, c2):
    matrix = Matrix([[a1, b1], [a2, b2]])
    constants = Matrix([c1, c2])

    try:
        solution = matrix.LUsolve(constants)
    except ValueError:
        return None

    if not all(x.is_integer for x in solution):
        return None

    A, B = map(int, solution)
    if A < 0 or B < 0:
        return None

    return A, B


def part_1(file_path):
    machines = parse_input(file_path, add_offset=False)
    total_tokens = 0

    for (a_x, a_y), (b_x, b_y), (p_x, p_y) in machines:
        result = solve_diophantine_numpy(a_y, b_y, p_y, a_x, b_x, p_x)
        if result:
            A, B = result
            total_tokens += A * 3 + B

    return total_tokens


def part_2(file_path):
    machines = parse_input(file_path, add_offset=True)
    total_tokens = 0

    for (a_x, a_y), (b_x, b_y), (p_x, p_y) in machines:
        result = solve_diophantine_sympy(a_y, b_y, p_y, a_x, b_x, p_x)
        if result:
            A, B = result
            total_tokens += A * 3 + B

    return total_tokens


def main():
    day = 13
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))


if __name__ == "__main__":
    main()
