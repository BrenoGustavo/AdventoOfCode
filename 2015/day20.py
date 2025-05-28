from pathlib import Path
from collections import defaultdict
puzzle_input = Path(__file__).parent / 'inputday20.txt'
with open(puzzle_input, 'r') as archive:
    input_puzzle = archive.read()

    

# 33100000


import math

def encontrar_divisores(X):
    divisores = set()
    for i in range(1, int(math.sqrt(X)) + 1):
        if X % i == 0:
            divisores.add(i)
            divisores.add(X // i)
    return divisores


# l = 360
# print(encontrar_divisores(l))

i = 0
def part1():
    while True:

        divisores = encontrar_divisores(i)
        presentes = sum(10*i for i in divisores)
        if presentes >= int(input_puzzle): # 33100000
            print(f'Casa {i}')
            break

        i+=1

# part1()

def part2():
    def contar_divisores(X, nums):
        divisores = set()
        for i in range(1, int(math.sqrt(X)) + 1):
            results = X % i
            if results == 0:
                div = X // i

                if nums[i] <=50:
                    divisores.add(i)
                    nums[i] +=1

                if nums[div] <=50:
                    divisores.add(div)
                    nums[div] +=1

        return divisores, nums
    
    nums = defaultdict(int)
    i=0
    while True:
        
        divisores, nums = contar_divisores(i, nums)
        presentes = sum(11*i for i in divisores)
        # print(f'Numero: {i} divisores: {divisores}')
        if presentes >= int(input_puzzle) : # 33100000
            print(f'Casa {i}, {presentes}')
            break

        i+=1

part2()



