from pathlib import Path
boss_stats_txt = Path(__file__).parent / 'inputday22.txt'

with open(boss_stats_txt, 'r') as archive:
    stats = [i.strip() for i in archive.readlines()]
    boss = [i.split(': ') for i in stats]
    boss_stats = dict()
    for i in boss:
        boss_stats[i[0]] = int(i[1])
        


spells = {
    # Spell:    Mana   Damage  HealsLife   HealsMana   Turns Shield 
    'Magic Missle': (53, 4, 0, 0, 0, 0),
    'Drain': (73, 2, 2, 0, 0, 0),
    'Shield': (113, 0, 0, 0, 6, 7),
    'Poison ': (173, 3, 0, 0, 6, 0),
    'Drain': (229, 0, 0, 101, 5, 0),
}