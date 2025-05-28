from pathlib import Path
from itertools import permutations
problem_input = Path(__file__).parent / 'inputday9.txt'
'''
AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
'''
def parse_distances(problem_input):
    distances = {}
    locations = set()
    with open(problem_input, 'r') as archive:
        for linha in archive:
            city1, rest = linha.strip().split(' to ')
            city2, distance = rest.split(' = ')
            distances[(city1, city2)] = int(distance)
            distances[(city2, city1)] = int(distance)
            locations.update({city2, city1})

    return distances, locations
distances, locations = parse_distances(problem_input)

def calculate_route_distance(route, distances):
    return sum(distances[(route[i], route[i + 1])] for i in range(len(route) - 1)) 


def find_shortest_route(data):
    distances, locations = parse_distances(data)
    shortest_distance = float('inf') # -> Reprenta o infinito.

    for route in permutations(locations):
        distance = calculate_route_distance(route, distances)
        shortest_distance = min(shortest_distance, distance)

    return shortest_distance

def find_longest_route(data):
    distances, locations = parse_distances(data)
    longest_distance = 0 # -> Reprenta o infinito.

    for route in permutations(locations):
        distance = calculate_route_distance(route, distances)
        longest_distance = max(longest_distance, distance)

    return longest_distance


shortest = find_shortest_route(problem_input)
print("Shortest distance", shortest)

longest = find_longest_route(problem_input)
print("Longest distance", longest)






 