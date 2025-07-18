"""
Day 20: Race Condition Solution

This solution calculates the number of possible "cheats" in a racetrack that can save
at least 100 picoseconds. Part 1 allows 2-picosecond cheats, while Part 2 extends
this to 20-picosecond cheats.
"""

import time
from collections import deque, defaultdict
import pathlib


def read_from_file(day):
    file_name = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    with open(file_name, "r") as file:
        return [list(line.strip()) for line in file]


def find_start_and_end(_map):
    start, end = (None, None), (None, None)
    for i in range(len(_map)):
        for j in range(len(_map[i])):
            if _map[i][j] == "S":
                start = (i, j)
            if _map[i][j] == "E":
                end = (i, j)
    return start, end


def bfs(_map, start):
    queue = deque()
    _map[start[0]][start[1]] = 0
    queue.append((start[0], start[1], 0))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y, cur_score = queue.popleft()
        for direction in directions:
            new_x, new_y = cur_x + direction[0], cur_y + direction[1]
            new_score = cur_score + 1

            if _map[new_x][new_y] == "#":
                continue
            if _map[new_x][new_y] in [".", "E"]:
                _map[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_score))
            if isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] > new_score:
                _map[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_score))


def part_1():
    def find_cheats(_map, cur_x, cur_y, cur_score, result):
        possible_dir_for_cheats = [
            [-2, 0],
            [0, -2],
            [2, 0],
            [0, 2],
            [-1, 1],
            [1, -1],
            [-1, -1],
            [1, 1],
        ]
        for dir in possible_dir_for_cheats:
            new_x, new_y = cur_x + dir[0], cur_y + dir[1]
            if (
                0 <= new_x < len(_map)
                and 0 <= new_y < len(_map[0])
                and isinstance(_map[new_x][new_y], int)
                and _map[new_x][new_y] + 2 < cur_score
            ):
                new_score = _map[new_x][new_y]
                result[cur_score - new_score - 2] += 1

    def backwards_bfs(_map, end):
        queue = deque()
        result = defaultdict(int)
        queue.append((end[0], end[1], _map[end[0]][end[1]]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            cur_x, cur_y, cur_score = queue.popleft()
            find_cheats(_map, cur_x, cur_y, cur_score, result)
            for direction in directions:
                new_x, new_y = cur_x + direction[0], cur_y + direction[1]
                new_score = cur_score - 1
                if (
                    isinstance(_map[new_x][new_y], int)
                    and _map[new_x][new_y] == new_score
                ):
                    queue.append((new_x, new_y, new_score))
        return result

    my_map = read_from_file(20)
    start, end = find_start_and_end(my_map)
    bfs(my_map, start)
    result = backwards_bfs(my_map, end)
    return sum(count for saved_seconds, count in result.items() if saved_seconds >= 100)


def part_2():
    def generate_possible_dir_for_cheats(min_sum, max_sum):
        pairs = []
        for x in range(-max_sum, max_sum + 1):
            for y in range(-max_sum, max_sum + 1):
                if min_sum <= abs(x) + abs(y) <= max_sum:
                    pairs.append((x, y))
        return pairs

    def find_cheats(_map, cur_x, cur_y, cur_score, _result, possible_dir_for_cheats):
        for dir in possible_dir_for_cheats:
            new_x, new_y = cur_x + dir[0], cur_y + dir[1]
            if (
                0 <= new_x < len(_map)
                and 0 <= new_y < len(_map[0])
                and isinstance(_map[new_x][new_y], int)
                and _map[new_x][new_y] + abs(dir[0]) + abs(dir[1]) < cur_score
            ):

                new_score = _map[new_x][new_y]
                _result[cur_score - new_score - (abs(dir[0]) + abs(dir[1]))] += 1

    def backwards_bfs(_map, end):
        queue = deque()
        _result = defaultdict(int)
        queue.append((end[0], end[1], _map[end[0]][end[1]]))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        possible_dir_for_cheats = generate_possible_dir_for_cheats(2, 20)

        while queue:
            cur_x, cur_y, cur_score = queue.popleft()
            find_cheats(_map, cur_x, cur_y, cur_score, _result, possible_dir_for_cheats)
            for direction in directions:
                new_x, new_y = cur_x + direction[0], cur_y + direction[1]
                new_score = cur_score - 1
                if (
                    isinstance(_map[new_x][new_y], int)
                    and _map[new_x][new_y] == new_score
                ):
                    queue.append((new_x, new_y, new_score))
        return _result

    my_map = read_from_file(20)
    start, end = find_start_and_end(my_map)
    bfs(my_map, start)
    result = backwards_bfs(my_map, end)
    return sum(count for saved_seconds, count in result.items() if saved_seconds >= 100)


def main():
    start_time = time.time()
    print("Part 1:", part_1())
    print("Part 2:", part_2())
    print(f"Time elapsed: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
