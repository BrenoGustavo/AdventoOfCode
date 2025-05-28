from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday3.txt'

with open(puzzle_input, 'r') as archive:
    directions = archive.read()


def count_houses(directions):
    x, y  = 0, 0
    already_visited = set()
    already_visited.add((0,0))
    print(len(directions))
    for dir in directions:
        print(f'Cur coord: {x, y}')
        if dir == '^':
            nx, ny = x, y + 1
            new_cord = nx, ny
            already_visited.add(new_cord)
            x, y = nx, ny

        elif dir == 'v':
            nx, ny = x, y -1
            new_cord = nx, ny
            already_visited.add(new_cord)
            x, y = nx, ny

        elif dir == '>':
            nx, ny = x + 1, y
            new_cord = nx, ny
            already_visited.add(new_cord)
            x, y = nx, ny
        elif dir == '<':
            nx, ny = x - 1, y 
            new_cord = nx, ny
            already_visited.add(new_cord)
            x, y = nx, ny

    return len(already_visited)
    
def part1():
    print(count_houses(directions))

def part2():
    santa_1_dirs = [directions[i] for i in range(len(directions)) if i % 2 == 0]
    santa_2_dirs = [directions[i] for i in range(len(directions)) if i % 2 == 1]

    def count_houses_2_santas(directions):

        x, y  = 0, 0
        already_visited = set()
        already_visited.add((0,0))
        for dir in directions:


            if dir == '^':
                nx, ny = x, y + 1
                new_cord = nx, ny
                already_visited.add(new_cord)
                x, y = nx, ny

            elif dir == 'v':
                nx, ny = x, y -1
                new_cord = nx, ny
                already_visited.add(new_cord)
                x, y = nx, ny

            elif dir == '>':
                nx, ny = x + 1, y
                new_cord = nx, ny
                already_visited.add(new_cord)
                x, y = nx, ny
            elif dir == '<':
                nx, ny = x - 1, y 
                new_cord = nx, ny
                already_visited.add(new_cord)
                x, y = nx, ny

        return already_visited

    santa1_houses = count_houses_2_santas(santa_1_dirs)
    santa2_houses = count_houses_2_santas(santa_2_dirs)
    all_houses = santa1_houses.union(santa2_houses)
    print(len(all_houses))

part2()