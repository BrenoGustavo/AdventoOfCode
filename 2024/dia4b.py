import os
import time

puzzle_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia4.txt')

with open(puzzle_txt, 'r') as arquivo:
    linhas_do_puzzle = [list(linha.strip()) for linha in arquivo.readlines()]



def X_MAS(puzzle):
    contagem = 0
    for i in range(len(puzzle)-2):
        for j in range(len(puzzle)-2):

            linha1 = ''.join([puzzle[i][j], puzzle[i][j+1], puzzle[i][j+2]])
            linha2 = ''.join([puzzle[i+1][j], puzzle[i+1][j+1], puzzle[i+1][j+2]])
            linha3 = ''.join([puzzle[i+2][j], puzzle[i+2][j+1], puzzle[i+2][j+2]])

            linhas_bloco = list((linha1, linha2, linha3))

             
            D_C_B = linhas_bloco[0][0] + linhas_bloco[1][1] + linhas_bloco[2][2]
            D_B_C = linhas_bloco[2][0] + linhas_bloco[1][1] + linhas_bloco[0][2]
            if  D_C_B == 'MAS' or D_C_B == 'SAM':
                if D_B_C == 'MAS' or D_B_C == 'SAM':
                    contagem +=1

        
    return contagem


print(X_MAS(linhas_do_puzzle))

                
            

