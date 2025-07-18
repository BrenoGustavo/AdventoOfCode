import pathlib
from collections import Counter

def part_1(file_path):

    with open(file_path, 'r') as file:
        left = []
        right = []
        
        for line in file:
          left_num, right_num = line.split()
          left.append(int(left_num))
          right.append(int(right_num))


        # left, right = zip(*(map(int, line.split()) for line in file))

        
        left_sorted = sorted(left)
        right_sorted = sorted(right)
        total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))
        
        return total_distance

def prat_2(file_path):

    with open(file_path, 'r') as file:

        left, right = zip(*(map(int, line.split()) for line in file))
        right_counts = Counter(right)
        similarity_score = sum(num * right_counts.get(num, 0) for num in left)

        return similarity_score

def main():
    day = 1
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1: ", part_1(puzzle_path))
    print("Part 2: ", prat_2(puzzle_path))

if __name__ == "__main__":
    main()