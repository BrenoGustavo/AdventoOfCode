import os
import time

puzzle_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia4.txt')

with open(puzzle_txt, 'r') as arquivo:
    linhas_do_puzzle = [list(linha.strip()) for linha in arquivo.readlines()]



def achar_palavras(puzzle):
    contagem = 0

    for i in range(len(puzzle)-3):
        for j in range(len(puzzle)-3):
            
            horizontal = ''.join(puzzle[i][j:j+4])
            vertical = ''.join([puzzle[i][j], puzzle[i+1][j], puzzle[i+2][j], puzzle[i+3][j]])
            diagonal_pbaixo = ''.join([puzzle[i][j], puzzle[i+1][j+1], puzzle[i+2][j+2], puzzle[i+3][j+3]])
            diagonal_pcima = ''.join([puzzle[i][j+3], puzzle[i+1][j+2], puzzle[i+2][j+1], puzzle[i+3][j]])

            words = list((horizontal, vertical, diagonal_pbaixo, diagonal_pcima))

            for w in words:
                if w == 'XMAS' or w =='SAMX':
                    contagem += 1
    for i in range(len(puzzle)-3):
        for j in range(-1, -4, -1):

            vertical2 = ''.join([puzzle[i][j], puzzle[i+1][j], puzzle[i+2][j], puzzle[i+3][j]])
            
            if vertical2 == 'XMAS' or vertical2 =='SAMX':
                contagem+=1

    for i in range(len(puzzle)-1, len(puzzle) -4, -1):
        for j in range(len(puzzle)-3):

            horizontal2 = ''.join(puzzle[i][j:j+4])

            if horizontal2 == 'XMAS' or horizontal2 =='SAMX':

                contagem+=1
    
    return contagem



timea = time.time()
print(achar_palavras(linhas_do_puzzle))
timeb = time.time()
print(f'Tempo: {timeb - timea}')