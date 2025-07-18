import pathlib
from collections import defaultdict, deque


def parse_input(file_path):
    with open(file_path, "r") as file:
        raw = file.read().strip()
    rules_raw, updates_raw = raw.split("\n\n")

    rules = [
        tuple(map(int, line.split("|"))) for line in rules_raw.strip().splitlines()
    ]
    updates = [
        list(map(int, line.split(","))) for line in updates_raw.strip().splitlines()
    ]

    return rules, updates


def validate_update(update, rules):
    """Verifica se uma atualização está em ordem de acordo com as regras."""
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True


def reorder_update(update, rules):
    """Reordena uma atualização inválida usando ordenação topológica."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set(update)

    # Construir grafo apenas com as regras que envolvem páginas da atualização
    for x, y in rules:
        if x in nodes and y in nodes:
            graph[x].append(y)
            in_degree[y] += 1

    for node in nodes:
        if node not in in_degree:
            in_degree[node] = 0

    # Ordenação topológica (Kahn's algorithm)
    queue = deque(sorted([node for node in nodes if in_degree[node] == 0]))
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in sorted(graph[current]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


def part_1(rules, updates):
    total = 0
    for update in updates:
        if validate_update(update, rules):
            meio = update[len(update) // 2]
            total += meio
    return total


def part_2(rules, updates):
    total = 0
    for update in updates:
        if not validate_update(update, rules):
            corrigida = reorder_update(update, rules)
            meio = corrigida[len(corrigida) // 2]
            total += meio
    return total


def main():
    day = 5
    input_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    rules, updates = parse_input(input_path)

    print("Part 1:", part_1(rules, updates))
    print("Part 2:", part_2(rules, updates))


if __name__ == "__main__":
    main()
