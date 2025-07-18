import pathlib


def parse(data):

    locks_and_keys = [list(map(list, i.split())) for i in data.split("\n\n")]
    locks = []
    keys = []

    for i in locks_and_keys:
        firstrow = i[0]
        if "#" in firstrow[0]:
            locks.append(i)
        else:
            keys.append(i)

    return locks, keys


def count_height_lock(eschematic):

    lenght = len(eschematic[0])
    heights = []
    for i in range(lenght):
        cur = []
        for j in eschematic:
            cur.append(j[i])

        counts_dot = cur.count(".")

        heights.append(counts_dot)
    return heights


def count_height_key(eschematic):

    lenght = len(eschematic[0])
    heights = []
    for i in range(lenght):
        cur = []
        for j in eschematic:
            cur.append(j[i])

        counts_dot = cur.count("#")

        heights.append(counts_dot)
    return heights


def check_height(lock, key):

    for el1, el2 in zip(lock, key):
        if el1 < el2:
            return False

    return True


def main():
    day = 25
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    with open(puzzle_path) as file:
        input_puzzle = file.read()

    locks, keys = parse(input_puzzle)

    count_height_lock(locks[0])
    count_height_key(keys[0])

    total = 0
    for lock in locks:
        lheight = count_height_lock(lock)

        for key in keys:
            kheight = count_height_key(key)

            if check_height(lheight, kheight):
                total += 1

    print("Parte 1:", total)


if __name__ == "__main__":
    main()
