from pathlib import Path
from itertools import combinations
from math import prod


def carregar_entrada(caminho: Path) -> list[int]:
    with caminho.open() as arquivo:
        return [int(linha) for linha in arquivo.read().splitlines()]


def pode_dividir_em_dois_grupos(resto: list[int], peso_alvo: int) -> bool:
    # Tenta encontrar pelo menos uma combinação de subconjunto que soma peso_alvo
    for tam in range(1, len(resto)):
        for grupo in combinations(resto, tam):
            if sum(grupo) == peso_alvo:
                return True
    return False


def encontrar_menor_qe(pacotes: list[int], grupos: int = 3) -> int:
    peso_total = sum(pacotes)
    peso_alvo = peso_total // grupos

    for tamanho in range(1, len(pacotes)):
        candidatos_validos = []
        for grupo in combinations(pacotes, tamanho):
            if sum(grupo) != peso_alvo:
                continue

            resto = pacotes.copy()
            for item in grupo:
                resto.remove(item)

            if pode_dividir_em_dois_grupos(resto, peso_alvo):
                candidatos_validos.append(prod(grupo))

        if candidatos_validos:
            return min(candidatos_validos)

    raise ValueError("Nenhuma combinação válida encontrada.")


def solve_part1(entrada: list[int]) -> int:
    return encontrar_menor_qe(entrada, grupos=3)


def solve_part2(entrada: list[int]) -> int:
    return encontrar_menor_qe(entrada, grupos=4)


def main():
    day = 24
    caminho_entrada = Path(__file__).parent / "inputday24.txt"
    entrada = carregar_entrada(caminho_entrada)
    print("Parte 1:", solve_part1(entrada))
    print("Parte 2:", solve_part2(entrada))


if __name__ == "__main__":
    main()
