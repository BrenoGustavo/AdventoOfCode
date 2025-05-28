from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday4.txt'

with open(puzzle_input, 'r') as archive:
    puzzle_input = archive.read()


import hashlib

def find_lowest_number(secret_key):
    number = 1
    while True:
        input_string = secret_key + str(number)
        hash_md5 = hashlib.md5(input_string.encode()).hexdigest()
        if hash_md5.startswith('000000'):
            return number
        number += 1

secret_key = "yzbqklnj"
answer = find_lowest_number(secret_key)
print(f"The lowest number is: {answer}")