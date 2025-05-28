from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday1.txt'

with open(puzzle_input, 'r') as archive:
    instructions = archive.read()

def part1():
    floor = instructions.count('(') - instructions.count(')')
    print(floor)


def part2():
    total = 0
    for i in range(len(instructions)):
        if instructions[i] == '(':
            total +=1
        elif instructions[i] == ')':
            total -=1
        print(total)
        if total < 0:
            print(i+1)
            return
        
part1()
part2()
