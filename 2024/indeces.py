import numpy as np
def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Converter a matriz em formato NumPy para facilitar manipulação
    matrix = np.array([list(row) for row in grid])

    # Função para verificar se a palavra está em uma direção
    def check_direction(start_row, start_col, delta_row, delta_col):
        for i in range(word_len):
            r, c = start_row + i * delta_row, start_col + i * delta_col
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r, c] != word[i]:
                return False
        return True

    # Explorar todas as direções possíveis
    directions = [
        (0, 1),   # Direita
        (0, -1),  # Esquerda
        (1, 0),   # Para baixo
        (-1, 0),  # Para cima
        (1, 1),   # Diagonal inferior direita
        (1, -1),  # Diagonal inferior esquerda
        (-1, 1),  # Diagonal superior direita
        (-1, -1)  # Diagonal superior esquerda
    ]

    # Iterar por cada posição na matriz
    for row in range(rows):
        for col in range(cols):
            for delta_row, delta_col in directions:
                if check_direction(row, col, delta_row, delta_col):
                    count += 1

    return count

# Caça-palavras
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

# Palavra a ser encontrada
word = "XMAS"

# Contar ocorrências da palavra
result = count_word_occurrences(grid, word)
print(f"A palavra '{word}' aparece {result} vezes no caça-palavras.")
