"""
Simula o caminho de patrulha de um guarda em um laboratório baseado em regras fixas de movimentação.
Parte 1 calcula quantas posições distintas são visitadas até sair do mapa.
Parte 2 determina quantas posições podem receber um obstáculo de forma que o guarda fique preso em um loop.
"""

import pathlib
from collections import defaultdict
import time

# Direções: cima, direita, baixo, esquerda
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part_1(file_path):
    def encontrar_posicao(lab):
        for i in range(len(lab)):
            for j in range(len(lab[i])):
                if lab[i][j] == "^":
                    return i, j

    def girar_matriz(matriz):
        transposta = [list(linha) for linha in zip(*matriz)]
        return transposta[::-1]

    def patrulha(lab, i, j):
        contagem = 0
        caminho_a_frente = [lab[linha][j] for linha in range(i - 1, -1, -1)]

        for t, valor in enumerate(caminho_a_frente):
            if valor not in ("X", "#"):
                contagem += 1
                lab[i - (t + 1)][j] = "X"
            elif valor == "#":
                lab_girado = girar_matriz(lab)
                novo_i = len(lab) - 1 - j
                novo_j = len(caminho_a_frente) - t
                return contagem + patrulha(lab_girado, novo_i, novo_j)
        return contagem + 1

    with open(file_path, "r") as arquivo:
        lab = [list(linha.strip()) for linha in arquivo.readlines()]

    i, j = encontrar_posicao(lab)  # type: ignore
    return patrulha(lab, i, j)


def part_2(file_path):
    start_time = time.time()

    with open(file_path, "r") as f:
        linhas = f.read().splitlines()

    campo = []
    pos = (-1, -1)
    for y, linha in enumerate(linhas):
        campo.append([c for c in linha])
        if pos[0] == -1:
            x = linha.find("^")
            if x != -1:
                pos = (x, y)

    def girar_direita(d):
        return (d + 1) % 4

    def proxima(pos, dir):
        dx, dy = DIRECTIONS[dir]
        return (pos[0] + dx, pos[1] + dy)

    def fora_dos_limites(p):
        return p[0] < 0 or p[0] >= len(campo[0]) or p[1] < 0 or p[1] >= len(campo)

    def eh_obstaculo(p):
        return campo[p[1]][p[0]] == "#"

    def eh_inicio(p):
        return campo[p[1]][p[0]] == "^"

    def verifica_loop(pos, dir, obstaculo):
        rastros = defaultdict(list)
        while True:
            prox = proxima(pos, dir)
            if fora_dos_limites(prox):
                return False
            if eh_obstaculo(prox) or prox == obstaculo:
                dir = girar_direita(dir)
                continue
            if dir in rastros[prox]:
                return True
            rastros[prox].append(dir)
            pos = prox

    dir_inicial = 0
    resultado = set()
    visitados = set()
    while True:
        prox = proxima(pos, dir_inicial)
        if fora_dos_limites(prox):
            break
        if eh_obstaculo(prox):
            dir_inicial = girar_direita(dir_inicial)
            continue
        if prox not in resultado and not eh_inicio(prox) and prox not in visitados:
            if verifica_loop(pos, girar_direita(dir_inicial), prox):
                resultado.add(prox)
        pos = prox
        visitados.add(pos)

    return len(resultado)


def main():
    day = 6
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))


if __name__ == "__main__":
    main()
