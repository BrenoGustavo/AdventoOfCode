import pathlib
from collections import defaultdict

day = 5
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    # puzzle_input = [i.strip() for i in file.readlines()]
    puzzle_input = file.read()

def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    seeds = list(map(int, sections[0].split(":")[1].split()))

    maps = []
    for section in sections[1:]:
        lines = section.strip().split("\n")[1:]  # skip the title line
        rules = []
        for line in lines:
            dst, src, length = map(int, line.strip().split())
            rules.append((src, dst, length))
        maps.append(rules)
    
    return seeds, maps

def convert(value, rules):
    for src, dst, length in rules:
        if src <= value < src + length:
            return dst + (value - src)
    return value  # unmapped values stay the same

def process_seed(seed, maps):
    value = seed
    for rules in maps:
        value = convert(value, rules)
    return value

def find_lowest_location(input_text):
    seeds, maps = parse_input(input_text)
    return min(process_seed(seed, maps) for seed in seeds)

print(find_lowest_location(puzzle_input))  # Output: 35
