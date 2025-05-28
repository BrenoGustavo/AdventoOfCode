from collections import deque, defaultdict

# Mapeamento do teclado numérico e controles
NUMERIC_KEYPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

DIRECTIONAL_KEYPAD = {
    '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1),
    'A': (0, 0)
}

# Função para calcular vizinhos válidos no teclado
def get_neighbors(position, keypad):
    x, y = position
    neighbors = []
    for dx, dy in DIRECTIONAL_KEYPAD.values():
        nx, ny = x + dx, y + dy
        if (nx, ny) in keypad.values():
            neighbors.append((nx, ny))
    return neighbors

# BFS para encontrar o menor caminho
def bfs(start, target, keypad):
    queue = deque([(start, 0)])  # (posição atual, passos)
    visited = set()
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, keypad):
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))
    return float('inf')

# Calcular complexidade total
def calculate_complexity(codes, numeric_keypad):
    total_complexity = 0
    for code in codes:
        numeric_part = int(code[:-1])
        total_steps = 0
        current_position = numeric_keypad['A']
        
        for char in code:
            target_position = numeric_keypad[char]
            steps = bfs(current_position, target_position, numeric_keypad)
            total_steps += steps
            current_position = target_position
        
        complexity = total_steps * numeric_part
        total_complexity += complexity
    
    return total_complexity

# Lista de códigos fornecida no exemplo
CODES = ["029A", "980A", "179A", "456A", "379A"]

# Calcular o resultado
result = calculate_complexity(CODES, NUMERIC_KEYPAD)
print("Complexidade total:", result)
