from pathlib import Path 
import re

puzzle_input = Path(__file__).parent / 'inputday8.txt' 

def calculate_lengths(s):
    """
    Calculate the code length and in-memory length for a given string literal.
    """
    # Code length is the length of the string as it appears in the file
    code_length = len(s)

    # In-memory length is the length of the string after processing escape sequences
    # Remove the surrounding quotes
    in_memory_string = s[1:-1]

    # Replace escape sequences with their corresponding characters
    # Handle \\, \", and \xXX
    in_memory_string = re.sub(r'\\x[0-9a-fA-F]{2}', 'X', in_memory_string)  # Replace \xXX with a single character
    in_memory_string = in_memory_string.replace('\\"', '"')  # Replace \" with "
    in_memory_string = in_memory_string.replace('\\\\', '\\')  # Replace \\ with \

    in_memory_length = len(in_memory_string)

    return code_length, in_memory_length

def solve_advent_of_code(file_path):
    """
    Solve the Advent of Code problem for the given input file.
    """
    total_code_length = 0
    total_in_memory_length = 0

    with open(puzzle_input, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:
                code_length, in_memory_length = calculate_lengths(line)
                total_code_length += code_length
                total_in_memory_length += in_memory_length

    # Calculate the difference
    difference = total_code_length - total_in_memory_length
    return difference

# Example usage
def part1():
    result = solve_advent_of_code(puzzle_input)
    print(f"The difference is: {result}")

# part1()


def part2():

    def encode_string(s):
        encoded = '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
        return encoded
    total_raw = 0
    total_encoded = 0
    with open(puzzle_input, 'r') as file:
            for line in file:
                line = line.strip()
                total_raw += len(line)
                encoded = encode_string(line)
                total_encoded += len(encoded)
                print(f"Original: {line} -> Encoded: {encoded}, Length: {len(encoded)}")

    print(f'Total_raw: {total_raw}')
    print(f'Total_encoded: {total_encoded}')
    print(total_encoded - total_raw)


part2()