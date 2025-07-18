import pathlib

def ler_puzzle(file_path):
    with open(file_path, 'r') as arquivo:
        return [list(linha.strip()) for linha in arquivo.readlines()]

def achar_palavras(puzzle):
    contagem = 0
    tamanho = len(puzzle)

    for i in range(tamanho - 3):
        for j in range(tamanho - 3):
            horizontal = ''.join(puzzle[i][j:j + 4])
            vertical = ''.join([puzzle[i + k][j] for k in range(4)])
            diagonal_pbaixo = ''.join([puzzle[i + k][j + k] for k in range(4)])
            diagonal_pcima = ''.join([puzzle[i + k][j + 3 - k] for k in range(4)])

            for w in (horizontal, vertical, diagonal_pbaixo, diagonal_pcima):
                if w == 'XMAS' or w == 'SAMX':
                    contagem += 1

    # Verificações horizontais na parte inferior
    for i in range(tamanho - 1, tamanho - 4, -1):
        for j in range(tamanho - 3):
            horizontal2 = ''.join(puzzle[i][j:j + 4])
            if horizontal2 == 'XMAS' or horizontal2 == 'SAMX':
                contagem += 1

    # Verificações verticais na parte direita
    for i in range(tamanho - 3):
        for j in range(-1, -4, -1):
            try:
                vertical2 = ''.join([puzzle[i + k][j] for k in range(4)])
                if vertical2 == 'XMAS' or vertical2 == 'SAMX':
                    contagem += 1
            except IndexError:
                continue

    return contagem

def X_MAS(puzzle):
    contagem = 0
    for i in range(len(puzzle) - 2):
        for j in range(len(puzzle[0]) - 2):
            linha1 = puzzle[i][j:j + 3]
            linha2 = puzzle[i + 1][j:j + 3]
            linha3 = puzzle[i + 2][j:j + 3]

            D_C_B = linha1[0] + linha2[1] + linha3[2]
            D_B_C = linha3[0] + linha2[1] + linha1[2]

            if (D_C_B in ('MAS', 'SAM')) and (D_B_C in ('MAS', 'SAM')):
                contagem += 1

    return contagem

def part_1(file_path):
    puzzle = ler_puzzle(file_path)
    return achar_palavras(puzzle)

def part_2(file_path):
    puzzle = ler_puzzle(file_path)
    return X_MAS(puzzle)

def main():
    day = 4
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))

if __name__ == "__main__":
    main()
