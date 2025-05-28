import os
from collections import deque
bytes_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia18.txt')

with open(bytes_txt, 'r') as arquivo:
    allbytes = [list(map(int, line.strip().split(','))) for line in arquivo.readlines()]
    kilobytes = allbytes[:1024]
    # next_bytes = [list(map(int, line.strip().split(','))) for num, line in enumerate(arquivo.readlines()) if num >= 1024]


grid = [['.'] * 71 for i in range(71)]




for num, coord in enumerate(kilobytes):
    cur_x = coord[0]
    cur_y = coord[1]

    grid[cur_y][cur_x] = '#'


for i in grid:
    string = ''.join(i)
    print(string)


from collections import deque

def is_path_possible(grid, start, end):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

def find_blocking_byte(grid_size, bytes_list):
    n = grid_size
    grid = [["." for _ in range(n)] for _ in range(n)]
    start, end = (0, 0), (n-1, n-1)
    
    for step, (x, y) in enumerate(bytes_list):
        grid[y][x] = "#"
        

        if not is_path_possible(grid, start, end):
            return x, y
    
    return None


grid_size = 71


result = find_blocking_byte(grid_size, allbytes)
print("Primeiro byte que corta o caminho:", result)
