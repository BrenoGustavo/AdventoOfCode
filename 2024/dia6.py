import os
import time
input_puzzle = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia6.txt')
with open(input_puzzle, 'r') as arquivo:

    laboratorio = [list(linha.strip()) for linha in arquivo.readlines()]

def encontrar_posição(laboratorio):
    for i in range(len(laboratorio)):
        for j in range(len(laboratorio[i])):
            if laboratorio[i][j] =='^':
                return (i, j)

def girar_matriz(matriz):
    # Transpor a matriz
    transposta = [list(linha) for linha in zip(*matriz)]
    # Inverter cada linha para girar 90 graus
    matriz_girada = [linha for linha in transposta]
    return matriz_girada[::-1]

posicao_inicial = encontrar_posição(laboratorio)
i, j = posicao_inicial[0], posicao_inicial[1]  # type: ignore

print(i) #6
print(j) #4

def guard_patrol(laboratorio:list, i:int, j:int, fun=1) -> int: #type: ignore
    
    # print(f'índice atual: {i}, {j}')

    ''' I and J stands for the guar's initial position, I for row and J for column'''
    # is_path = True
    contagem = 0
    caminho_a_frente_invertido = [laboratorio[hor][j] for hor in range(len(laboratorio)) if hor < i]
    caminho_a_frente = caminho_a_frente_invertido[::-1]


    # time.sleep(0.5)
    print(caminho_a_frente)

    # time.sleep(0.5)
    contagem_indice = 0
    for t in range(len(caminho_a_frente)):
        # for linha in laboratorio:
        #     print(linha)    

        if  caminho_a_frente[t] != 'X' and caminho_a_frente[t] !='#' :

            contagem += 1    
            contagem_indice +=1
            diferenca = len(laboratorio[0]) - len(caminho_a_frente)
            laboratorio[len(laboratorio) - diferenca - (t+1)][j] = 'X' # Muda elemento para

            # print(f'Substituindo agora {caminho_a_frente[t]} por "X"')
            # time.sleep(0.5)

            # time.sleep(0.5)

        elif caminho_a_frente[t] == '#':

            # print('Girou!: ')
            laboratorio_girado = girar_matriz(laboratorio)
            diferenca = len(laboratorio) - len(caminho_a_frente)
            novo_indice_i = 9 - j
            novo_indice_j = len(caminho_a_frente) - (t) 

            return contagem + guard_patrol(laboratorio_girado, novo_indice_i, novo_indice_j, fun+1)
            
    else:
        return len(caminho_a_frente)


contagem = 0
for linha in laboratorio:
    print(linha)
    contagem +=1

print(contagem)
 
print(guard_patrol(laboratorio, 53, 89))
# print(guard_patrol(laboratorio, 6, 4))






















    
