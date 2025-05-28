import numpy as np
import os
puzzle_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia13.txt')

with open(puzzle_txt, 'r') as arquivo:
    CLAWS = [linha for linha in arquivo.readlines()]


def solve_linear_diophantine(ay, by, cy, ax, bx, cx):
    """
    Resolve o sistema linear diophantino:
    c1 = a1*A + b1*B
    c2 = a2*A + b2*B

    Retorna os menores valores de A e B, ou informa que não há solução.
    """
    # Matriz dos coeficientes
    matrix = np.array([[ay, by], [ax, bx]])
    constants = np.array([cy, cx])

    # Determinante da matriz
    det = np.linalg.det(matrix)

    if det == 0:
        print("Sistema não possui solução única (determinante zero).")
        return 0
    # Solução para A e B em números reais
    solution = np.linalg.solve(matrix, constants)

    # Verifica se a solução é inteira (considerando tolerância)
    tolerance = 1e-9
    if not all(abs(val - round(val)) < tolerance for val in solution):
        return "Não há solução inteira para o sistema."

    # Converter para inteiros arredondados
    A, B = map(round, solution)

    # Garantir que os valores sejam não negativos
    if A < 0 or B < 0:
        return "Não há solução não negativa para o sistema."

    return A, B

# # Exemplo de uso



# a1, b1, c1 = 86, 37, 6450
# a2, b2, c2 = 17, 84, 7870

# resultado = solve_linear_diophantine(a1, b1, c1, a2, b2, c2)
# print("Resultado:", resultado)

blocos = []
for c in range(len(CLAWS)):
    if CLAWS[c].startswith('Button A'):
        block = CLAWS[c:c+3]
        blocos.append(block)


# print(blocos)
machines_values = dict()
for machine in range(len(blocos)):
    
    machines_values[f'M{machine}'] = 0

    button_a_line = blocos[machine][0].strip().split(',')
    button_b_line = blocos[machine][1].strip().split(',')
    prize_line = blocos[machine][2].strip().split(',')

    button_A_X = int(button_a_line[0][button_a_line[0].index('+') +1:])
    button_A_Y = int(button_a_line[1][button_a_line[1].index('+') +1:])


    button_B_X = int(button_b_line[0][button_b_line[0].index('+') +1:])
    button_B_Y = int(button_b_line[1][button_b_line[1].index('+') +1:])

    prize_X = int(prize_line[0][prize_line[0].index('=') +1:])
    prize_Y = int(prize_line[1][prize_line[1].index('=') +1:])


    machines_values[f'M{machine}'] = [(button_A_X, button_A_Y), (button_B_X, button_B_Y), (prize_X, prize_Y)]

# print(machines_values)


somatoria = 0
for machine in machines_values.values():

    BA, BB, P = machine[0], machine[1], machine[2]
    ax, ay, bx, by, cx, cy = BA[0], BA[1], BB[0], BB[1], P[0], P[1]

    resultados = solve_linear_diophantine(ay, by, cy, ax, bx, cx)

    if isinstance(resultados, tuple):

        somatoria += 3*resultados[0] + resultados[1]


    print()

print(somatoria)







        





    


