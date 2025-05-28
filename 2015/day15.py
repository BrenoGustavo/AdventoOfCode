from pathlib import Path
puzzle_input = Path(__file__).parent / 'inputday15.txt'
with open(puzzle_input, 'r') as archive:
    ingredientes = [line.strip() for line in archive.readlines()]

ingredients = dict()

for i in ingredientes:
    j = i.split()
    ingredients[j[0][:-1]] = [int(j[2][:-1]), int(j[4][:-1]), int(j[6][:-1]), int(j[8][:-1]), int(j[10])]


def score_combination_without_calories(amounts):
    """ Calcula a pontuação da combinação de ingredientes """
    # Inicializa os atributos em 0
    total = [0, 0, 0, 0]  # capacity, durability, flavor, texture
    
    # Percorre cada ingrediente e soma suas contribuições
    for i, (ingredient, props) in enumerate(ingredients.items()):
        for j in range(4):  # Ignorando calorias (posição 4)
            total[j] += amounts[i] * props[j]

    # Se algum valor for negativo, ele deve ser tratado como 0
    total = [max(0, x) for x in total]

    # Calcula o score final (multiplicação dos atributos)
    return total[0] * total[1] * total[2] * total[3]

def score_combination_with_calories(amounts):
    """ Calcula a pontuação da combinação de ingredientes """
    # Inicializa os atributos em 0
    total = [0, 0, 0, 0]  # capacity, durability, flavor, texture
    total_calories = 0
    # Percorre cada ingrediente e soma suas contribuições
    for i, (ingredient, props) in enumerate(ingredients.items()):
        for j in range(4):  # Ignorando calorias (posição 4)
            total[j] += amounts[i] * props[j]
        total_calories += amounts[i] * props[4]

    if total_calories != 500:  
        return 0  
    # Se algum valor for negativo, ele deve ser tratado como 0
    total = [max(0, x) for x in total]

    # Calcula o score final (multiplicação dos atributos)
    return total[0] * total[1] * total[2] * total[3]

def part1():
    def find_best_cookie():
        best_score = 0
        
        # Gerar todas as combinações possíveis que somam 100
        for a in range(101):
            for b in range(101 - a):
                for c in range(101 - a - b):
                    d = 100 - a - b - c  # O último ingrediente completa a soma
                    amounts = [a, b, c, d]
                    
                    # Calcula a pontuação dessa distribuição
                    score = score_combination_without_calories(amounts)
                    best_score = max(best_score, score)
        
        return best_score

    # Executa a busca pelo melhor cookie
    print(find_best_cookie())

def part2():
    def find_best_cookie():
        best_score = 0
        
        # Gerar todas as combinações possíveis que somam 100
        for a in range(101):
            for b in range(101 - a):
                for c in range(101 - a - b):
                    d = 100 - a - b - c  # O último ingrediente completa a soma
                    amounts = [a, b, c, d]
                    
                    # Calcula a pontuação dessa distribuição
                    score = score_combination_with_calories(amounts)
                    best_score = max(best_score, score)
        
        return best_score

    # Executa a busca pelo melhor cookie
    print(find_best_cookie())

part2()
