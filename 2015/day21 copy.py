from pathlib import Path
import math
from itertools import combinations
puzzle_input = Path(__file__).parent / 'inputday21.txt'
with open(puzzle_input, 'r') as archive:
    boss_stats = tuple(int(i.strip().split()[-1]) for i in archive.readlines())

# boss_stats = (109, 8, 2)
def fight(player, boss):
    player_hp, player_damage, player_armor = player
    boss_hp, boss_damage, boss_armor = boss
    while True:
        boss_hp -= max(1, player_damage - boss_armor)
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0:
            return False


def win_against_boss(player, boss):
    player_hp, player_damage, player_armor = player
    boss_hp, boss_damage, boss_armor = boss
    effective_player_damage = max(1, player_damage - boss_armor)
    effective_boss_damage = max(1, boss_damage - player_armor)
    boss_turns = math.ceil(player_hp / effective_boss_damage)
    player_turns = math.ceil(boss_hp / effective_player_damage)

    return player_turns <= boss_turns



shop = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3'''

itens = shop.split('\n\n')
weapons = itens[0].split('\n')[1:]
armor = itens[1].split('\n')[1:]
rings = itens[2].split('\n')[1:]

weapons = [i.split() for i in weapons]
armor = [i.split() for i in armor]
rings = [i.split() for i in rings]

weapons_stats = [(int(i[1]), int(i[2]), int(i[3])) for i in weapons]
armor_stats = [(int(i[1]), int(i[2]), int(i[3])) for i in armor]
rings_stats = [(int(i[1]), int(i[2]), int(i[3])) for i in rings]


def get_combinations(weapons=weapons_stats, armors=armor_stats, rings=rings_stats):
    for weapon in weapons:
        for armor in armors:
            for ring in rings:
                for ring2 in rings:
                    if ring == ring2:
                        continue
                    yield [weapon, armor, ring, ring2]


def get_stats(itens):
    cost = sum(i[0] for i in itens)
    damage = sum(i[1] for i in itens)
    armor = sum(i[2] for i in itens)
    return cost, damage, armor


def get_best_combination(boss_stats = boss_stats):
    best_cost = float('inf')
    for combination in get_combinations():
        shop_stats = get_stats(combination)
        player_stats = (100, shop_stats[1], shop_stats[2])

        if win_against_boss(player_stats, boss_stats):
            cost = shop_stats[0]
            if cost < best_cost:
                best_cost = cost
    return best_cost

def part1():
    print(get_best_combination())


def part2():
    best_cost = 0
    for combination in get_combinations():
        shop_stats = get_stats(combination)
        player_stats = (100, shop_stats[1], shop_stats[2])

        if not win_against_boss(player_stats, boss_stats):
            print('player lost')
            print(shop_stats[0])
            cost = shop_stats[0]
            if cost > best_cost:
                best_cost = cost
                best_comb =  combination

    return best_cost, best_comb

# part1()
print(part2())


    