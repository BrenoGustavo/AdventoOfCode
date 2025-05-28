import pathlib
day = 1
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    puzzle_input = [i.strip() for i in file.readlines()]

def part2():

    word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def find_digits(line):
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(int(line[i]))
                i += 1
                continue

            for word, val in word_to_digit.items():
                if line[i:].startswith(word):
                    digits.append(val)
                    # Avança só 1 caractere para permitir sobreposição
                    break
            i += 1
        return digits

    total = 0
    for line in puzzle_input:
        digits = find_digits(line)
        if digits:
            value = int(str(digits[0]) + str(digits[-1]))
            total += value
    print(f"Part 2 total: {total}")
                
part2()











