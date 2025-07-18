"""
Dia 11 - Pedra Piscante

Este script simula a transformação de uma lista de pedras inteiras de acordo com três regras específicas, durante um número determinado de "piscadas".

Regras:
- Se a pedra for 0, ela vira 1.
- Se o número de dígitos da pedra for par, ela se divide em dois números.
- Se for ímpar, a pedra é multiplicada por 2024.

Parte 1: Calcula o total de pedras após 25 piscadas.
Parte 2: Calcula o total de pedras após 75 piscadas.

Para eficiência, utiliza um `Counter` para rastrear quantidades de pedras por valor ao longo das transformações.
"""

import pathlib
from collections import Counter


def carregar_pedras(file_path):
    with open(file_path) as file:
        return [int(i) for i in file.read().split()]


def calcular_pedras(pedras_iniciais, piscadas):
    contagem = Counter(pedras_iniciais)

    for _ in range(piscadas):
        nova_contagem = Counter()
        for pedra, quantidade in contagem.items():
            if pedra == 0:
                nova_contagem[1] += quantidade  # Regra 1
            elif len(str(pedra)) % 2 == 0:
                # Regra 2: divisão em dois números
                meio = len(str(pedra)) // 2
                esquerdo = int(str(pedra)[:meio])
                direito = int(str(pedra)[meio:])
                nova_contagem[esquerdo] += quantidade
                nova_contagem[direito] += quantidade
            else:
                # Regra 3: multiplicação
                nova_contagem[pedra * 2024] += quantidade
        contagem = nova_contagem

    return contagem.total()


def part_1(pedras):
    return calcular_pedras(pedras, piscadas=25)


def part_2(pedras):
    return calcular_pedras(pedras, piscadas=75)


def main():
    day = 11
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    pedras = carregar_pedras(puzzle_path)

    print("Part 1:", part_1(pedras))
    print("Part 2:", part_2(pedras))


if __name__ == "__main__":
    main()
