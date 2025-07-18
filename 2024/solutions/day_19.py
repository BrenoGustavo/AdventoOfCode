"""
Verifica como formar padrões de toalhas com uma lista de padrões disponíveis.
Parte 1: Conta quantos designs são possíveis de formar com os padrões disponíveis.
Parte 2: Conta todas as diferentes formas de montar cada design com os padrões disponíveis.
"""

import pathlib


def load_data(file_path):
    with open(file_path, "r") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
        padrões = linhas[0].split(", ")
        designs = linhas[1:]
    return padrões, designs


def is_possible(design, padrões, memo):
    if design in memo:
        return memo[design]

    if not design:
        return True

    for padrão in padrões:
        if design.startswith(padrão):
            if is_possible(design[len(padrão) :], padrões, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def count_possible_designs(padrões, designs):
    count = 0
    for design in designs:
        if is_possible(design, padrões, {}):
            count += 1
    return count


def count_all_arrangements(padrões, designs):
    padrões_set = set(padrões)

    def count_ways(design, memo):
        if design in memo:
            return memo[design]
        if design == "":
            return 1

        total = 0
        for padrao in padrões_set:
            if design.startswith(padrao):
                total += count_ways(design[len(padrao) :], memo)

        memo[design] = total
        return total

    total_count = 0
    for design in designs:
        total_count += count_ways(design, {})

    return total_count


def part_1(file_path):
    padrões, designs = load_data(file_path)
    return count_possible_designs(padrões, designs)


def part_2(file_path):
    padrões, designs = load_data(file_path)
    return count_all_arrangements(padrões, designs)


def main():
    day = 19
    file_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(file_path))  # Resultado esperado: 304
    print("Part 2:", part_2(file_path))  # Resultado esperado: número total de arranjos


if __name__ == "__main__":
    main()
