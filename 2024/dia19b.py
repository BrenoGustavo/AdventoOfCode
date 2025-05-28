import os
import time
toalhas_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia19.txt')

with open(toalhas_txt, 'r') as arquivo:

    linhas = arquivo.readlines()
    available_towels = linhas[0].strip().split(', ')
    sequences = [linha.strip() for linha in linhas[1:] if linha.strip()]



tamanho_design = 0

def count_arrangements(patterns, designs):
    # Transformar a lista de padrões em um conjunto para acesso rápido
    patterns_set = set(patterns)
    
    # Função recursiva com memoização
    def count_ways(design, memo):
        if design in memo:
            return memo[design]
        
        if design == "":
            return 1  # Uma maneira de formar uma string vazia (não usar nada)
        
        ways = 0
        # Tentar cada padrão como prefixo
        for pattern in patterns_set:
            if design.startswith(pattern):
                # Recursão para o restante do design
                ways += count_ways(design[len(pattern):], memo)
        
        memo[design] = ways
        return ways

    total_count = 0
    memo = {}
    # Para cada design, contar as maneiras e somar
    for design in designs:
        total_count += count_ways(design, memo)
    
    return total_count

# Entrada de exemplo

# Resolver o problema
result = count_arrangements(available_towels, sequences)
print("Total de maneiras:", result)
