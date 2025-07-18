import heapq
import pathlib

"""
--- Dia 16: Reindeer Maze ---
Parte 1: Encontra o menor custo de movimento da entrada 'S' para a saida 'E' em um labirinto,
levando em conta o custo de andar (+1) e rotacionar (+1000).

Parte 2: Conta quantos tiles fazem parte de pelo menos um dos caminhos de menor custo.
"""

day = 16
puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"


def parse_maze(maze_str):
    start = end = None
    grid = []
    for y, line in enumerate(maze_str.strip().split("\n")):
        row = []
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
                row.append(".")
            elif char == "E":
                end = (x, y)
                row.append(".")
            else:
                row.append(char)
        grid.append(row)
    return grid, start, end


def valid_move(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == "."


def part_1(maze_str):
    grid, start, end = parse_maze(maze_str)
    pq = [(0, start, "E")]  # (cost, (x, y), direction)
    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    directions_list = ["N", "E", "S", "W"]
    visited = set()

    while pq:
        cost, (x, y), direction = heapq.heappop(pq)  # type: ignore
        if ((x, y), direction) in visited:
            continue
        visited.add(((x, y), direction))

        if (x, y) == end:
            return cost

        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if valid_move(nx, ny, grid):
            heapq.heappush(pq, (cost + 1, (nx, ny), direction))

        for turn in [-1, 1]:
            new_dir = directions_list[(directions_list.index(direction) + turn) % 4]
            heapq.heappush(pq, (cost + 1000, (x, y), new_dir))

    return -1


def part_2(maze_str):
    grid = maze_str.strip().split("\n")
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    grid[end[0]] = grid[end[0]].replace("E", ".")
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {}
    heap = [(0, 0, *start, {start})]  # (score, direction, i, j, path)
    winning_paths = set()
    lowest_score = None

    def can_visit(d, i, j, score):
        prev_score = visited.get((d, i, j))
        if prev_score is not None and prev_score < score:
            return False
        visited[(d, i, j)] = score
        return True

    while heap:
        score, d, i, j, path = heapq.heappop(heap)

        if lowest_score is not None and score > lowest_score:
            break

        if (i, j) == end:
            lowest_score = score
            winning_paths |= path
            continue

        if not can_visit(d, i, j, score):
            continue

        di, dj = directions[d]
        ni, nj = i + di, j + dj
        if grid[ni][nj] == "." and can_visit(d, ni, nj, score + 1):
            heapq.heappush(heap, (score + 1, d, ni, nj, path | {(ni, nj)}))

        for turn in [-1, 1]:
            nd = (d + turn) % 4
            if can_visit(nd, i, j, score + 1000):
                heapq.heappush(heap, (score + 1000, nd, i, j, path))

    return len(winning_paths)


def main():
    with open(puzzle_path, "r") as file:
        input_data = file.read()

    result_1 = part_1(input_data)
    print("Part 1:", result_1)

    result_2 = part_2(input_data)
    print("Part 2:", result_2)


if __name__ == "__main__":
    main()
