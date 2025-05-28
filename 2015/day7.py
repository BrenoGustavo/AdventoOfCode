from pathlib import Path
from collections import deque, defaultdict
puzzle_input = Path(__file__).parent / 'inputday7.txt'

def part1():
    def parse_line(line):
        # Separar lado esquerdo e direito da seta
        left, right = line.strip().split(" -> ")
        
        # Transformar lado esquerdo em uma tupla, convertendo números para int
        left_parts = tuple(int(x) if x.isdigit() else x for x in left.split())

        return left_parts, right


    with open(puzzle_input, 'r') as archive:
        instructions = [parse_line(line) for line in archive]



    wqueue = deque(instructions)
    wires_dict = defaultdict()

    while wqueue:
        
        cur_item = wqueue.popleft()
        # print(cur_item)
        i,  j = cur_item
        # if len(i) == 1:
        #     print(cur_item)


        if len(i) == 3:  # Exemplo: x AND y -> z
            w1, operator, w2 = i

            # Substituir valores já conhecidos
            if isinstance(w1, str) and w1 in wires_dict:
                w1 = wires_dict[w1]
            if isinstance(w2, str) and w2 in wires_dict:
                w2 = wires_dict[w2]

            # Apenas processa a operação se ambos os valores forem conhecidos
            if isinstance(w1, int) and isinstance(w2, int):
                if operator == "OR":
                    wires_dict[j] = w1 | w2
                elif operator == "AND":
                    wires_dict[j] = w1 & w2
                elif operator == "RSHIFT":
                    wires_dict[j] = w1 >> w2
                elif operator == "LSHIFT":
                    wires_dict[j] = w1 << w2
            else:
                wqueue.append(cur_item)  # Adiciona de volta se não pode ser resolvido ainda

        elif len(i) == 2:
            operator, w = i
            if w in wires_dict:
                mod = ~ wires_dict[w] & ((1 << 16) - 1) #type: ignore
                wires_dict[j] = mod
            else:
                wqueue.append(cur_item)

        elif len(i) == 1:
            w = i[0]
            if isinstance(w, int):  # Se for número, já pode armazenar
                wires_dict[j] = w
            elif w in wires_dict:  # Se for uma variável já resolvida
                wires_dict[j] = wires_dict[w]
            else:
                wqueue.append(cur_item)  # Adiciona de volta se ainda não tem o valor



    for i, j in wires_dict.items():
        if i =="a":
            print(i, j)

def part2():

    
    """ 
    Overriding wire-b with wire-a's signal
    Wire-a signal from part 1: 956
    """
    def parse_line(line):
        # Separar lado esquerdo e direito da seta
        left, right = line.strip().split(" -> ")
        
        # Transformar lado esquerdo em uma tupla, convertendo números para int
        left_parts = tuple(int(x) if x.isdigit() else x for x in left.split())

        return left_parts, right


    with open(puzzle_input, 'r') as archive:
        instructions = [parse_line(line) for line in archive]



    wqueue = deque(instructions)
    wires_dict = defaultdict()

    while wqueue:
        
        cur_item = wqueue.popleft()
        # print(cur_item)
        i,  j = cur_item
        # if len(i) == 1:
        #     print(cur_item)


        if len(i) == 3:  # Exemplo: x AND y -> z
            w1, operator, w2 = i

            # Substituir valores já conhecidos
            if isinstance(w1, str) and w1 in wires_dict:
                w1 = wires_dict[w1]
            if isinstance(w2, str) and w2 in wires_dict:
                w2 = wires_dict[w2]

            # Apenas processa a operação se ambos os valores forem conhecidos
            if isinstance(w1, int) and isinstance(w2, int):
                if operator == "OR":
                    wires_dict[j] = w1 | w2
                elif operator == "AND":
                    wires_dict[j] = w1 & w2
                elif operator == "RSHIFT":
                    wires_dict[j] = w1 >> w2
                elif operator == "LSHIFT":
                    wires_dict[j] = w1 << w2
            else:
                wqueue.append(cur_item)  # Adiciona de volta se não pode ser resolvido ainda

        elif len(i) == 2:
            operator, w = i
            if w in wires_dict:
                mod = ~ wires_dict[w] & ((1 << 16) - 1) #type: ignore
                wires_dict[j] = mod
            else:
                wqueue.append(cur_item)

        elif len(i) == 1:
            w = i[0]
            if isinstance(w, int):  # Se for número, já pode armazenar
                if j =='b':
                    wires_dict[j] = 956
                else:
                    wires_dict[j] = w
            elif w in wires_dict:  # Se for uma variável já resolvida
                wires_dict[j] = wires_dict[w]
            else:
                wqueue.append(cur_item)  # Adiciona de volta se ainda não tem o valor



    for i, j in wires_dict.items():
        if i =="a":
            print(i, j)

part2()
