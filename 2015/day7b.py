from pathlib import Path

def parse_line(line):
    """Lê uma linha e transforma em uma instrução armazenável em um dicionário."""
    left, right = line.strip().split(" -> ")
    parts = tuple(int(x) if x.isdigit() else x for x in left.split())
    return right, parts  # Retorna {destino: expressão}

# Carregar as instruções do arquivo
puzzle_input = Path(__file__).parent / 'inputday7.txt'
with open(puzzle_input, "r") as archive:
    instructions = dict(parse_line(line) for line in archive)

# Cache para armazenar valores resolvidos
wires_dict = {}

def evaluate(wire):
    """Resolve o valor do fio 'wire' recursivamente com memoization."""
    if wire.isdigit():  
        return int(wire)  # Retorna diretamente se for número
    if wire in wires_dict:
        return wires_dict[wire]  # Retorna se já foi calculado

    operation = instructions[wire]

    if len(operation) == 1:  # Exemplo: 123 -> x ou y -> x
        result = evaluate(operation[0])

    elif len(operation) == 2:  # Exemplo: NOT x -> h
        _, w = operation
        result = ~evaluate(w) & 0xFFFF  # Limitar a 16 bits

    else:  # Operações binárias como AND, OR, LSHIFT, RSHIFT
        w1, op, w2 = operation
        w1, w2 = evaluate(w1), evaluate(w2)

        if op == "AND":
            result = w1 & w2
        elif op == "OR":
            result = w1 | w2
        elif op == "LSHIFT":
            result = w1 << w2
        elif op == "RSHIFT":
            result = w1 >> w2

    wires_dict[wire] = result  # Armazena o resultado no cache
    return result

# Obter o sinal final em 'a'
print("O valor do sinal em 'a' é:", evaluate("a"))

