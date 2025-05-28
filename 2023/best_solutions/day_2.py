import pathlib

def load_puzzle_input(day):
    """Carrega o input do puzzle de forma segura com tratamento de erros."""
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    try:
        with open(puzzle_path) as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo de input não encontrado: {puzzle_path}")

def parse_games(puzzle_input):
    """Parseia os dados do jogo em uma estrutura mais eficiente."""
    games = {}
    for line in puzzle_input:
        game_part, cubes_part = line.split(': ')
        game_id = int(game_part.split()[1])
        
        # Lista de conjuntos de cubos (mais eficiente que dicionário aninhado)
        subsets = []
        for subset in cubes_part.split('; '):
            cubes = {}
            for cube_info in subset.split(', '):
                amount, color = cube_info.split()
                cubes[color] = int(amount)
            subsets.append(cubes)
        
        games[game_id] = subsets
    return games

def is_game_valid(game_subsets, max_cubes):
    """Verifica se um jogo é válido baseado nos cubos máximos permitidos."""
    for subset in game_subsets:
        for color, amount in subset.items():
            if amount > max_cubes.get(color, 0):
                return False
    return True

def solve():
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    puzzle_input = load_puzzle_input(day=2)
    games = parse_games(puzzle_input)
    
    total = sum(
        game_id
        for game_id, subsets in games.items()
        if is_game_valid(subsets, max_cubes)
    )
    
    print(f'A soma dos IDs dos jogos válidos é: {total}')

if __name__ == "__main__":
    solve()