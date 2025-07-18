"""
Solução do desafio Day 7 - Advent of Code 2023: Bridge Repair.

O objetivo é verificar, para cada linha de entrada, se existe uma combinação de operadores
(+ , *, e na parte 2 também ||) entre os números fornecidos que gere o valor alvo especificado
no início da linha. A avaliação deve ser feita da esquerda para a direita (sem precedência).

A parte 1 considera apenas os operadores + e *.
A parte 2 considera também a concatenação || (transforma dois números em um só, ex: 12 || 3 = 123).
"""

import pathlib
from itertools import product
from time import time


def gerar_arranjos(n, incluir_concat=False):
    operadores = ["*", "+"]
    if incluir_concat:
        operadores.append("||")
    return [list(arranjo) for arranjo in product(operadores, repeat=n)]


def testar_operadores(equacao: str, incluir_concat=False) -> int:
    resultado_esperado_str, elementos_str = equacao.split(":")
    resultado_esperado = int(resultado_esperado_str)
    elementos = [int(x) for x in elementos_str.strip().split()]

    arranjos_operadores = gerar_arranjos(
        len(elementos) - 1, incluir_concat=incluir_concat
    )

    for operadores in arranjos_operadores:
        total_parcial = elementos[0]

        for i in range(len(operadores)):
            oper = operadores[i]
            valor = elementos[i + 1]

            if oper == "+":
                total_parcial += valor
            elif oper == "*":
                total_parcial *= valor
            elif oper == "||":
                total_parcial = int(str(total_parcial) + str(valor))

        if total_parcial == resultado_esperado:
            return resultado_esperado

    return 0  # Caso nenhuma combinação atinja o valor esperado


def soma_expressoes_validas(expressions_raw, incluir_concat=False) -> int:
    return sum(testar_operadores(expr, incluir_concat) for expr in expressions_raw)


def main():
    day = 7
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    with open(puzzle_path, "r") as file:
        expressions_raw = file.readlines()

    inicio = time()

    print("Part 1:", soma_expressoes_validas(expressions_raw, incluir_concat=False))
    print("Part 2:", soma_expressoes_validas(expressions_raw, incluir_concat=True))

    fim = time()
    print(f"Tempo de execução: {fim - inicio:.2f} segundos")


if __name__ == "__main__":
    main()
