from functools import cache

# Caminho para o arquivo de entrada

import pathlib

day = 21
caminho_arquivo = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"


def calcular_caminho(par):
    """
    Calcula o caminho entre duas teclas em um teclado numérico.

    :param par: Uma tupla contendo dois caracteres representando as teclas.
    :return: Uma string com as instruções de movimento.
    """
    (y1, x1), (y2, x2) = [divmod("789456123_0A<v>".find(tecla), 3) for tecla in par]
    caminho = ">" * (x2 - x1) + "v" * (y2 - y1) + "0" * (y1 - y2) + "<" * (x1 - x2)
    # print(caminho)
    return caminho if (3, 0) in [(y1, x2), (y2, x1)] else caminho[::-1]


@cache
def calcular_comprimento(sequencia, profundidade):
    """
    Calcula o comprimento total de uma sequência de movimentos.

    :param sequencia: Uma string representando a sequência de movimentos.
    :param profundidade: O nível de profundidade da recursão.
    :return: O comprimento total calculado.
    """
    if profundidade < 0:
        # print(len(sequencia))
        return len(sequencia) + 1
    return sum(
        calcular_comprimento(calcular_caminho(par), profundidade - 1)
        for par in zip("A" + sequencia, sequencia + "A")
    )


def calcular_resultado(profundidade):
    """
    Calcula o resultado somando os valores obtidos a partir do arquivo de entrada.

    :param profundidade: O nível de profundidade da recursão.
    :return: A soma dos resultados calculados.
    """
    with open(caminho_arquivo) as arquivo:
        return sum(
            int(sequencia[:3]) * calcular_comprimento(sequencia[:3], profundidade)
            for sequencia in arquivo
        )


if __name__ == "__main__":

    resultado = calcular_resultado(2)
    print("Parte 1: ", resultado)
    resultado = calcular_resultado(25)
    print("Parte 2: ", resultado)
