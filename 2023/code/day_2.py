import pathlib
day = 2
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)

with open(puzzle_path) as file:
    puzzle_input = [i.strip().split(': ') for i in file.readlines()]
    game_dict = dict()
    for game_num, sets_cubes in puzzle_input:
        # cur_game = int(game_num[-1])
        cur_game = int(game_num.split(' ')[-1])
        game_dict[cur_game] = {}

        cubes_sets = sets_cubes.split("; ")
        
        cur_set = 1

        for handful_of_cubes in cubes_sets:
            game_dict[cur_game][cur_set] = {}

            for cubes in handful_of_cubes.split(', '):
                amount, color = cubes.split(' ')
                game_dict[cur_game][cur_set][color] = int(amount)
            
            cur_set +=1

# for i, j in game_dict.items():
#     print('Game: ', i)
#     for k, l in j.items():
#         print(f'\t{k}, {l}')

def part1():
    red, green, blue  = 12, 13, 15
    colors = {
        'red': 12,
        'green': 13, 
        'blue': 14
    }
    total = 0
    for game, sets in game_dict.items():
        # print('Game: ', game)
        for cur_set, handful_of_cubes in sets.items():
            valid = True

            for color, amount in colors.items():
                if color in handful_of_cubes:
                    if handful_of_cubes[color] > colors[color]:
                        valid = False
                        break
            if not valid:
                break
        else:
            total += game

    print(f' O total é {total}')

# part1()
total = 0
for game, sets_of_handful_of_cubes in game_dict.items():
    rgb = {'red': 0, 'green': 0, 'blue': 0 }
    for set_num, handful_cubes in sets_of_handful_of_cubes.items():
        for color, count in rgb.items():
            if color in handful_cubes:
                rgb[color] = max(rgb[color], handful_cubes[color])

    result = 1
    for count in rgb.values():
        result *= count
    
    total += result

print(total)