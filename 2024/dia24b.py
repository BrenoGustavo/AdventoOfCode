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
    print(f'Quantidade de Z"s: {len(bits_z)}')

    # for z in sorted(bits_z):
    #     print(z)
    return int(''.join(str(b[1]) for b in sorted(bits_z, reverse=True)), 2)

wires_dict, system = parsing(caminho)


binary_x = []
binary_y = []
for i, j in wires_dict.items():
    if i.startswith('x'):
        binary_x.append(str(j))
    elif i.startswith('y'):
        binary_y.append(str(j))

binary_x, binary_y = ''.join(binary_x), ''.join(binary_y)
int_binx = int(binary_x, 2)
int_biny = int(binary_y, 2)
int_binz = int_binx + int_biny
binary_z = bin(int_binz)

print(f'Binário de X: {binary_x}')
print(f'Binário de Y: {binary_y}')
print('-'*65)
print(f'Binário de Z: {binary_z[2:]}\n')


print(f'Decimal X: {int_binx}')
print(f'Decimal Y: {int_biny}')
print('-'*65)
print(f'Decimal Z: {int_binz}\n')

resultado = solve_p1(caminho)
binary_resultado = bin(resultado)

print(binary_resultado[2:])
print(binary_z[2:])

print(int(binary_resultado[2:], 2))
print(int(binary_z[2:], 2))
