from pathlib import Path
from itertools import combinations, permutations
puzzle_input = Path(__file__).parent / 'inputday2.txt'

with open(puzzle_input, 'r') as archive:
    presents = [i.strip() for i in archive.readlines()]


def find_area(list_of_boxes_sizes):
    total_paper = 0
    for box in list_of_boxes_sizes:
        dimensions = [int(i) for i in box.split('x')]
        print(dimensions)
        size_areas = [i[0] * i[1] * 2 for i in combinations(dimensions, 2)]
        ribbons = sorted(size_areas)[:2]
        bow = dimensions[0] * dimensions[1] * dimensions[2]
        print(ribbons)
        print(bow)
        smallest = min(size_areas)
        total_paper += sum(size_areas) + int(smallest/2)
        # print(total_paper)
    return total_paper

def ribbons(list_of_boxes_sizes):
    total_ribbon_lenght = 0
    for box in list_of_boxes_sizes:
        dimensions = [int(i) for i in box.split('x')]
        ribbons_size = sum(sorted(dimensions)[:2]) * 2
        bow = dimensions[0] * dimensions[1] * dimensions[2]
        print(ribbons_size + bow)
        total_ribbon_lenght += ribbons_size + bow
        # print(total_paper)
    return total_ribbon_lenght

print(ribbons(presents))




