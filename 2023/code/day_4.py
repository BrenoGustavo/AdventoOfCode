import pathlib
from collections import defaultdict

day = 4
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    puzzle_input = [i.strip() for i in file.readlines()]

def part1():

    # def check_winning_nums(line):
    total = 0
    for line in puzzle_input:
        _, numbers = line.split(':')

        winners_list, wagerlist = numbers.split("|")

        winners= [int(i.strip()) for i in winners_list.split() if i]
        wagers = [int(i.strip()) for i in wagerlist.split() if i]

        winners_won = set(winners) & set(wagers)
        worth = 2**(len(winners_won)-1) if winners_won else 0
        total +=worth


    print(total)

# part1()

def part2():
    scratchcards_count =  defaultdict(lambda: 1)
    for i in range(1, len(puzzle_input)+1):
        
        
        line = puzzle_input[i-1]
        # print(line)

        _, numbers = line.split(':')

        winners_list, wagerlist = numbers.split("|")

        winners= [int(i.strip()) for i in winners_list.split() if i]
        wagers = [int(i.strip()) for i in wagerlist.split() if i]

        winners_won = set(winners) & set(wagers)
        # print(winners_won)
        next_copies = len(winners_won)

        for mult in range(scratchcards_count[i]):
            # print(f"\t{mult}")
            for j in range(1, next_copies+1):
            
                scratchcards_count[i+j] +=1

    # for k, l in scratchcards_count.items():
    #     print(k, l)
    
    total = sum(v for v in scratchcards_count.values())
    print(f'The total of scratchcards own is: ', total)



part2()