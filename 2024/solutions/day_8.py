"""
Solução do desafio Day 8 - Advent of Code 2023: Resonant Collinearity.

O problema envolve identificar "antinodes", que são pontos alinhados com duas antenas
da mesma frequência, com duas regras diferentes:

- Parte 1: Um antinode ocorre quando está perfeitamente em linha com duas antenas,
  e **uma está o dobro da distância da outra**.
- Parte 2: Qualquer ponto alinhado com **pelo menos duas antenas** da mesma frequência
  já é considerado um antinode, independente da distância.

O código identifica todas as antenas, agrupa suas coordenadas por frequência e calcula
os antinodes gerados conforme as regras acima.
"""

import pathlib
from itertools import combinations


def carregar_matriz_input(dia: int):
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{dia}.txt"
    with open(puzzle_path, "r") as file:
        linhas = file.readlines()
    return [list(linha.strip()) for linha in linhas]


def mapear_antenas(matriz):
    antenas = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor != ".":
                antenas.setdefault(valor, []).append((i, j))
    return antenas


def antinodes_parte_1(combinacoes, limite):
    nodes = set()
    for a, b in combinacoes:
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay

        try:
            tg = dy / dx
        except ZeroDivisionError:
            tg = None

        # Antinode 1: em linha após B, a mesma distância
        c1 = (bx + dx, by + dy) if tg is not None else (bx + dx, by + dy)
        # Antinode 2: em linha antes de A, a mesma distância
        c2 = (ax - dx, ay - dy) if tg is not None else (ax - dx, ay - dy)

        for cx, cy in (c1, c2):
            if 0 <= cx < limite and 0 <= cy < limite:
                nodes.add((cx, cy))

    return nodes


def antinodes_parte_2(combinacoes, tamanho):
    nodes = set()

    for a, b in combinacoes:
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay

        try:
            tg = dy / dx
            b_coef = ay - tg * ax
        except ZeroDivisionError:
            tg = None
            b_coef = None

        def ponto_em_linha(k):
            return (
                (round(ax + dx * k), round(ay + dy * k))
                if tg is not None
                else (ax, ay + dy * k)
            )

        k = -1
        while True:
            x, y = ponto_em_linha(k)
            if not (0 <= x < tamanho and 0 <= y < tamanho):
                break
            nodes.add((x, y))
            k -= 1

        k = 1
        while True:
            x, y = ponto_em_linha(k)
            if not (0 <= x < tamanho and 0 <= y < tamanho):
                break
            nodes.add((x, y))
            k += 1

        # Também adiciona as próprias antenas como antinodes
        nodes.add(a)
        nodes.add(b)

    return nodes


def encontrar_antinodes(matriz, parte_2=False):
    coordenadas_antenas = mapear_antenas(matriz)
    tamanho = len(matriz)
    todos_antinodes = set()

    for coordenadas in coordenadas_antenas.values():
        if len(coordenadas) < 2:
            continue
        combinacoes = list(combinations(coordenadas, 2))
        if parte_2:
            novos = antinodes_parte_2(combinacoes, tamanho)
        else:
            novos = antinodes_parte_1(combinacoes, tamanho)
        todos_antinodes |= novos

    return todos_antinodes


def main():
    dia = 8
    matriz = carregar_matriz_input(dia)

    parte1 = encontrar_antinodes(matriz, parte_2=False)
    print("Part 1:", len(parte1))

    parte2 = encontrar_antinodes(matriz, parte_2=True)
    print("Part 2:", len(parte2))


if __name__ == "__main__":
    main()
