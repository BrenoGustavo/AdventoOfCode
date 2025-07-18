import re

def is_symbol(c):
    return c != '.' and not c.isdigit()

def get_adjacent_positions(row, start_col, end_col):
    positions = []
    for r in range(row - 1, row + 2):
        for c in range(start_col - 1, end_col + 1):
            if (r == row and start_col <= c < end_col):
                continue  # não contar os próprios dígitos do número
            positions.append((r, c))
    return positions

def sum_part_numbers(schematic):
    total = 0
    rows = len(schematic)
    cols = len(schematic[0])

    for row_idx, line in enumerate(schematic):
        for match in re.finditer(r'\d+', line):
            num = int(match.group())
            start_col = match.start()
            end_col = match.end()
            adjacent_positions = get_adjacent_positions(row_idx, start_col, end_col)
            
            for r, c in adjacent_positions:
                if 0 <= r < rows and 0 <= c < cols:
                    if is_symbol(schematic[r][c]):
                        total += num
                        break  # basta um símbolo para contar o número
    return total

# Exemplo de entrada
input_lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Resultado
print(sum_part_numbers(input_lines))  # Saída esperada: 4361
