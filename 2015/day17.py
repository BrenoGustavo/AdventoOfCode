from pathlib import Path
from itertools import combinations

puzzle_input = Path(__file__).parent / 'inputday17.txt'
with open(puzzle_input, 'r') as archive:
    containers = [int(i.strip()) for i in archive.readlines()]


print(containers)

def eggnog_containers_sum(containers, target):
    count = 0
    for i in range(1, len(containers)+1):

        for combo in combinations(containers, i):
            if sum(combo) == target:
                count += 1

    return count

def part1():

    liters = 150
    result = eggnog_containers_sum(containers, liters)

    print(result)


# def max_containers(containers, target):
#     num_of_containters = {}
#     for i in range(1, len(containers)+1):

#         for combo in combinations(containers, i):
#             if len(combo) not in num_of_containters:
#                 num_of_containters[len(combo)] = 0


#             if sum(combo) == target:
#                 num_of_containters[len(combo)] +=1  

#     return max([x for x in num_of_containters.items()], key=lambda x: x[1])

# liters = 150
# result = max_containers(containers, liters)
# print(result)

def max_containers(containers, target):
    count = 0
    max_len = float('inf')
    for i in range(1, len(containers)+1):
        for combo in combinations(containers, i):
            num_of_containers = len(combo)
            if sum(combo) == target:
                if num_of_containers <  max_len:
                    max_len = num_of_containers
                    count = 0
                if num_of_containers == max_len:
                    count +=1

                

    return count

liters = 150
result = max_containers(containers, liters)
print(result)

        

        
