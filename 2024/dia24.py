import os
from collections import deque
caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia24.txt')
def parsing(caminho):
    with open(caminho) as arquivo:
        data_str = ''.join(arquivo.readlines())
        data1, data2 = data_str.split('\n\n')

    wires_dict = dict()

    for line in data1.splitlines():
        wire, value = line[:3], line[-1]
        wires_dict[wire] = int(value)

    system = []
    for linha in data2.splitlines():
        elementos = linha.split()
        input_1, operator, input_2, _, output = elementos
        system.append((input_1, operator, input_2, output))


    return wires_dict, system

def make_connections(wires_dict, system):
    def operate(input_1, operator, input_2):

     if operator == 'AND':
        return 1 if input_1 == input_2 == 1 else 0

     elif operator == 'OR':
        return 1 if input_1 or input_2 else 0
     
     elif operator == 'XOR':
        return 1 if input_1 != input_2 else 0

    fila = deque()
    wires_operated = dict() ##
    for elementos in system:
        input_1, operator, input_2, output = elementos

        if input_1 in wires_dict and input_2 in wires_dict:

            value = operate(wires_dict[input_1], operator, wires_dict[input_2])
            wires_operated[output] = value
        else:
            fila.append(elementos)


    while fila:
        elementos = fila.popleft()
        input_1, operator, input_2, output = elementos

        if input_1 in wires_operated and input_2 in wires_operated:

            value = operate(wires_operated[input_1], operator, wires_operated[input_2])
            wires_operated[output] = value  

        else: 
            fila.append(elementos)

    return wires_operated


def solve_p1(caminho):

    wires_dict, system = parsing(caminho)
    resultado = make_connections(wires_dict, system)

    bits_z = []
    for i,j in resultado.items():
        if i.startswith('z'):
            bits_z.append((i,j))

    print(int(''.join(str(b[1]) for b in sorted(bits_z, reverse=True)), 2))


solve_p1(caminho)