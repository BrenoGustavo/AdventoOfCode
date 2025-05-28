import pathlib
day = 1
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    puzzle_input = [i.strip() for i in file.readlines()]

def part1():

    def first_and_last_numbers(list_of_lines):
        sum_nums = 0
        for line in list_of_lines:
            numbers = [i for i in line if i.isdigit()]
            first_last_num = int(numbers[0] + numbers[-1])
            sum_nums += first_last_num

        return sum_nums 

    print(f'The sum of the first and last digits of each line is {first_and_last_numbers(puzzle_input)}')

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

    def find_digits(puzzle_input):

        total = 0
        for line in puzzle_input:
            i = 0
            digits = []
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

            if digits:
                value = int(str(digits[0]) + str(digits[-1]))
                total += value

        return total
    
    resultado = find_digits(puzzle_input)
    print('AAAAA',resultado)


part2()







