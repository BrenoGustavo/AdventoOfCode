import os
from collections import deque
bytes_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia18.txt')

with open(bytes_txt, 'r') as arquivo:

    kilobytes = [list(map(int, line.strip().split(','))) for num, line in enumerate(arquivo.readlines()) if num < 1024]
    # next_bytes = [list(map(int, line.strip().split(','))) for num, line in enumerate(arquivo.readlines()) if num >= 1024]


grid = [['.'] * 71 for i in range(71)]




for num, coord in enumerate(kilobytes):
    cur_x = coord[0]
    cur_y = coord[1]

    grid[cur_y][cur_x] = '#'


for i in grid:
    string = ''.join(i)
    print(string)



def shortes_path(maze):

    n = len(maze)

    start = (0,0)
    end = (n-1, n-1)

    queue = deque([(0,0,0)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add(start)

    while queue:

        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:

            nx, ny = x + dx, y  + dy

            if 0 <= nx < n  and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1


resultado = shortes_path(grid)

print(resultado)







