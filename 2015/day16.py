from pathlib import Path

puzzle_input = Path(__file__).parent / 'inputday16.txt'
with open(puzzle_input, 'r') as archive:
    aunts = [i.strip() for i in archive.readlines()]


sues = dict()
for i, aunt_items in enumerate(aunts, 1):
    sues[i] = {}
    raw_items = aunt_items.split()
    # print(raw_items)

    item1 = raw_items[2][:-1], int(raw_items[3][:-1]) 
    item2 = raw_items[4][:-1], int(raw_items[5][:-1]) 
    item3 = raw_items[6][:-1], int(raw_items[7]) 
    items = [item1, item2, item3]

    for item in items:
        object, amount = item
        sues[i][object] = amount


message = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''.splitlines()

def part1():
    compounds = dict()

    for line in message:
        raw_obj, raw_amnt = line.split(': ')
        object, amount = raw_obj, int(raw_amnt)
        compounds[object] = amount

    for sue, objects in sues.items():
        count = 0 
        for obj, amount in objects.items():
            if amount == compounds[obj]:
                count +=1
        if count == 3:
            print(f'The right aunt Sue is Sue {sue}')
            count = 0

def part2():
    compounds = dict()

    for line in message:
        raw_obj, raw_amnt = line.split(': ')
        object, amount = raw_obj, int(raw_amnt)
        compounds[object] = amount

    for sue, objects in sues.items():
        count = 0 
        for obj, amount in objects.items():

            if obj == "cats" or obj == "trees":
                if amount > compounds[obj]:
                    count +=1
            elif obj == "pomeranians" or obj == "goldfish":
                if amount < compounds[obj]:
                    count +=1

            elif amount == compounds[obj]:
                count +=1
                
        if count == 3:
            print(f'The right aunt Sue is Sue {sue}')
            count = 0


part1()
part2()



