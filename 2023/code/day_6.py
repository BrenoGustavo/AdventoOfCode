import pathlib

day = 6
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
print(puzzle_path)


'''
Time:      7  15   30
Distance:  9  40  200'''

with open(puzzle_path) as file:


    puzzle_input = file.readlines()
    stripped = [i.strip() for i in puzzle_input[0].split(':')[1].split(' ') if i]
    stripped_2 = [i.strip() for i in puzzle_input[1].split(':')[1].split(' ') if i]
    times = list(map(int, stripped))
    distances = list(map(int, stripped_2))

    races_info = list(zip(times, distances))

def beat_records(races_info):
    final_mult = 1

    for info in races_info:
        time, distance_record = info

        new_ways_to_beat = 0

        for btn_prs_time in range(1, time+1):
            remaining = time - btn_prs_time

            new_distance = btn_prs_time * remaining
            if new_distance > distance_record:
                new_ways_to_beat += 1

        final_mult *= new_ways_to_beat if new_ways_to_beat else 1

    return final_mult

def part1():
    result = beat_records(races_info)

    print(result)

def part2():
    no_kerning_time = int(''.join([i.strip() for i in puzzle_input[0].split(':')[1].split(' ') if i]))
    no_kerning_distance = int(''.join([i.strip() for i in puzzle_input[1].split(':')[1].split(' ') if i]))
    part_2_info = [(no_kerning_time, no_kerning_distance)]

    result = beat_records(part_2_info)
    print(result)
   
part2()
