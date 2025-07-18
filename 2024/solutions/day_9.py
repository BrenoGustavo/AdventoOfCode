"""
Solução do desafio Day 9 - Advent of Code 2023: Disk Fragmenter.

A entrada é uma string numérica que alterna entre o tamanho de arquivos e espaços livres,
ex: "12345" → arquivo de 1 bloco, 2 espaços livres, arquivo de 3 blocos, etc.

✔️ Parte 1: mover blocos individuais para preencher o espaço mais à esquerda.
✔️ Parte 2: mover arquivos inteiros para a esquerda, se houver espaço contínuo.

Ambas as partes terminam com o cálculo de um checksum: soma de (índice * ID do arquivo) para cada bloco.
"""

import pathlib


def carregar_entrada(dia: int) -> str:
    path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{dia}.txt"
    with open(path) as f:
        return f.read().strip()


def gerar_disco(input_str: str) -> list[str]:
    """Gera o disco expandido a partir da string compacta."""
    disco = []
    file_id = 0
    for i, c in enumerate(input_str):
        n = int(c)
        if i % 2 == 0:
            disco.extend([str(file_id)] * n)
            file_id += 1
        else:
            disco.extend(["."] * n)
    return disco


def mover_blocos_individuais(disco: list[str]) -> list[str]:
    """Move blocos um por um da direita para a esquerda."""
    i = len(disco) - 1
    while i >= 0:
        if disco[i] != ".":
            for j in range(i):
                if disco[j] == ".":
                    disco[j], disco[i] = disco[i], "."
                    break
        i -= 1
    return disco


def compact_files(disk):
    # print("".join(disk))

    """Compacta os arquivos conforme as regras da Parte 2."""
    max_id = max(int(ch) for ch in disk if ch != ".")
    for file_id in range(max_id, -1, -1):
        file_id = str(file_id)

        file_start = disk.index(file_id)
        file_end = len(disk) - 1 - disk[::-1].index(file_id)
        file_length = file_end - file_start + 1

        best_start = None
        for i in range(file_start):
            if all(
                c == "." for c in disk[i : i + file_length]
            ):  # Genial !!!!!! Revisar depois esse algoritmo
                best_start = i
                break

        if best_start is not None:

            for i in range(file_start, file_end + 1):
                disk[i] = "."

            for i in range(best_start, best_start + file_length):
                disk[i] = file_id

    # print("".join(disk))
    return disk


def calcular_checksum(disco: list[str]) -> int:
    # print("".join(disco))
    return sum(i * int(c) for i, c in enumerate(disco) if c != ".")


def main():
    dia = 9
    entrada = carregar_entrada(dia)

    # Parte 1: mover blocos individualmente
    disco1 = gerar_disco(entrada)
    mover_blocos_individuais(disco1)
    print("Parte 1:", calcular_checksum(disco1))

    # Parte 2: mover arquivos inteiros
    disco2 = gerar_disco(entrada)
    compact_files(disco2)
    print("Parte 2:", calcular_checksum(disco2))


if __name__ == "__main__":
    main()
