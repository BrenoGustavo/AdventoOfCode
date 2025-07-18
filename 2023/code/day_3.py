import pathlib

day = 3
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    puzzle_input = [i.strip() for i in file.readlines()]
def part1():
    def is_symbol(c):
        return not c.isdigit() and c != '.'

    def adjacent_coords(i, first_j, last_j):
        coords = [
            (i - 1, first_j - 1),
            (i, first_j - 1),
            (i + 1, first_j - 1),
            (i - 1, last_j + 1),
            (i, last_j + 1),
            (i + 1, last_j + 1),
        ]

        for index in range(first_j, last_j + 1):
            coords.append((i - 1, index))
            coords.append((i + 1, index))

        return coords

    part_numbers = []

    for i in range(len(puzzle_input)):
        line = puzzle_input[i]
        j = 0
        while j < len(line):
            if line[j].isdigit():
                start = j
                while j < len(line) and line[j].isdigit():
                    j += 1
                end = j - 1
                number = int(line[start:j])
                coords = adjacent_coords(i, start, end)

                for y, x in coords:
                    if 0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[0]):
                        if is_symbol(puzzle_input[y][x]):
                            part_numbers.append(number)
                            break
            else:
                j += 1

    print()
    print(sum(part_numbers))

part1()

# other_coords = [
#     (-1, -1),
#     (-1, 0),
#     (-1, +1),
#     (0, +1),
#     (+1, +1),
#     (+1, 0),
#     (+1, -1),
#     (0, -1),
# ]

# for i in range(len(puzzle_input)):
#     for j in range(len(puzzle_input[i])):
#         if puzzle_input[i][j] == '*':
#             adjacent_coords = [(y+i, x+j) for y, x in other_coords]
#             for y, x in adjacent_coords:

#                 if 0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[i]):
#                     ...

def part2():
    import pathlib

    day = 3
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    with open(puzzle_path) as file:
        puzzle_input = [line.strip() for line in file.readlines()]

    digit_to_number = {}
    gear_ratios = []

    # Passo 1: mapear coordenadas de cada dígito ao número completo
    for i, row in enumerate(puzzle_input):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                start = j
                num = 0
                coords = []
                while j < len(row) and row[j].isdigit():
                    num = num * 10 + int(row[j])
                    coords.append((i, j))
                    j += 1
                for coord in coords:
                    digit_to_number[coord] = num
            else:
                j += 1

    # Offsets dos 8 vizinhos
    adj_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    # Passo 2: identificar gears
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if puzzle_input[i][j] == '*':
                found = set()
                for dy, dx in adj_offsets:
                    y, x = i + dy, j + dx
                    if (y, x) in digit_to_number:
                        found.add(digit_to_number[(y, x)])
                if len(found) == 2:
                    a, b = found
                    gear_ratios.append(a * b)

    # Resultado final
    print(sum(gear_ratios))

part2()

