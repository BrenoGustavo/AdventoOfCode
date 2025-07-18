"""
Simula a geração de números secretos de compradores no mercado de macacos.
Na Parte 1, soma os 2000º números secretos de cada comprador após aplicar a transformação.
Na Parte 2, busca a melhor sequência de 4 variações de preço para maximizar a venda de esconderijos,
identificando quando vender com base nas variações entre os últimos dígitos dos números secretos.
"""

import pathlib
import math


def make_secret_number(secret):
    result1 = (secret * 64) ^ secret
    result1 %= 16777216

    result2 = (result1 // 32) ^ result1
    result2 %= 16777216

    result3 = (result2 * 2048) ^ result2
    result3 %= 16777216

    return result3


def part_1(file_path):
    with open(file_path, "r") as file:
        secrets = [int(line.strip()) for line in file.readlines()]

    total = 0
    for secret in secrets:
        for _ in range(2000):
            secret = make_secret_number(secret)
        total += secret

    return total


def part_2(file_path):
    with open(file_path, "r") as file:
        secrets = [int(line.strip()) for line in file.readlines()]

    REPETITIONS = 2000
    sequences = []
    changes = []

    for num in secrets:
        sequence = [num % 10]
        change = []

        for _ in range(REPETITIONS):
            prev = num
            num = make_secret_number(num)
            sequence.append(num % 10)
            change.append((num % 10) - (prev % 10))

        sequences.append(sequence)
        changes.append(change)

    # Armazena todas as possíveis sequências de 4 variações e seus resultados
    quadruples = []
    for buyer_index in range(len(sequences)):
        quad_map = {}
        for i in range(3, REPETITIONS):
            key = (
                f"{changes[buyer_index][i - 3]:+}"
                f"{changes[buyer_index][i - 2]:+}"
                f"{changes[buyer_index][i - 1]:+}"
                f"{changes[buyer_index][i]:+}"
            )
            if key not in quad_map:
                quad_map[key] = sequences[buyer_index][i + 1]
        quadruples.append(quad_map)

    # Soma os valores de venda para cada sequência única
    totals = {}
    for quad_map in quadruples:
        for key, value in quad_map.items():
            totals[key] = totals.get(key, 0) + value

    return max(totals.values())


def main():
    day = 22
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))


if __name__ == "__main__":
    main()
