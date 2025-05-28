from pathlib import Path
from itertools import permutations
puzzle_input = Path(__file__).parent / 'inputday13.txt'
with open(puzzle_input, 'r') as archive:
    information = [line.strip() for line in archive.readlines()]

def names_and_happiness(information):

    happiness = dict()
    people = set()
    for line in information:

        info = line[:-1].split()
        name1, operation, value, name2 = info[0], info[2], int(info[3]), info[-1]
        if operation =='lose':
            value = - value
        
        people.add(name1)

        happiness[(name1, name2)] = value

    return happiness, people
 
def sum_happines(data: dict, people: set):
    pairs = [list(p) for p in permutations(people)]
    total = 0
    for p in pairs:
        p.append(p[0])
        # print(p)
        result = 0
        for i in range(len(p)-1):
            p1, p2 = p[i], p[i+1]
            value1 = data[(p1, p2)]
            value2 = data[(p2, p1)]
            result += value1 + value2
            
        if result > total:
            total = result
    return total

def part1():
    data, people = names_and_happiness(information)

    resultado = sum_happines(data, people)

    print(resultado)

part1()


def part2():
    data, people = names_and_happiness(information)


    for p in people:

        data[(p, 'me')] = 0
        data[('me', p)] = 0

    people.add('me')

    resultado = sum_happines(data, people)
    print(resultado)




# part2()




