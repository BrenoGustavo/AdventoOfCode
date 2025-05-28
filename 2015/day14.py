from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday14.txt'
with open(puzzle_input, 'r') as archive:
    reindeers = [line.strip() for line in archive.readlines()]

def time_flies(reindeers_info, cur_time):

    fly_speed, time, rest = reindeers_info
    ntimes_flown = cur_time // (time + rest)
    final = cur_time % (time + rest)
    
    if final >= time:
        ntimes_flown +=1
        distance_raced = ntimes_flown*(fly_speed*time)
    else:
        mid_flight = final
        distance_raced = ntimes_flown*(fly_speed*time) + mid_flight*fly_speed

    return distance_raced

def part1(cur_time):
    info = []
    for line in reindeers:


        r =  line.split()
        name, *reindeer_info = r[0], int(r[3]), int(r[6]), int(r[13])

        raced = time_flies(reindeer_info, cur_time)
        info.append((name, raced))
        # print(f'{name} raced {raced} km')


    result = max(info, key=lambda x: x[1])
    print(result)
    return result

# part1(1000)

def part2(time):
    reindeers_stats = []
    reindeers_scores = dict()
    for line in reindeers:
            r =  line.split()
            name, *reindeer_info = r[0], int(r[3]), int(r[6]), int(r[13])
            reindeers_scores[name] = 0
            reindeers_stats.append((name, *reindeer_info))

    # print(reindeers_stats)


    for i in range(1, time+1):
        longest = 0
        cur_stats = []
        for r in reindeers_stats:
            name, *reindeer_info = r
            cur_dist = time_flies(reindeer_info, i)
            # print(cur_dist)
            cur_stats.append((name, cur_dist))

            longest = cur_dist if cur_dist > longest else longest

        winners = [i for i in cur_stats if i[1] == longest]
        
        for w in winners:
            name, cur_dist = w
            reindeers_scores[name] +=1

    for i, j in reindeers_scores.items():
        print(i, j)
    print(max(reindeers_scores.values()))
    return max(reindeers_scores.values())

part2(2503)
part1(2503)


    

        
         





    
