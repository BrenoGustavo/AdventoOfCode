import time
import os
tempoa = time.time()
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia9.txt')

def compactar_disco(input_puzzle):
    # Constrói a lista de blocos a partir do input
    blocks = []
    file_id = 0

    for i, char in enumerate(input_puzzle):
        count = int(char)
        if i % 2 == 0:  # Arquivo
            blocks.extend([file_id] * count)
            file_id += 1
        else:  # Espaço vazio
            blocks.extend(['.'] * count)
    # print(f'blocos: {blocks}')
    return blocks


def somar(blocks):
    indice_max = 0
    i = len(blocks) - 1  # Começa do final
    while i >= 0:
        if blocks[i] != '.':  # Bloco de arquivo encontrado

            max_loop= 0
            for j in range(len(blocks)):
                if j > i:
                    break
                max_loop = j if j >= max_loop else max_loop


                if blocks[j] == '.':
                    blocks[j] = blocks[i]
                    blocks[i] = '.'
                    break
            indice_max = max_loop if max_loop > indice_max else indice_max
                
        i -= 1  # Passa para o próximo bloco
    checksum = sum(idx * block for idx, block in enumerate(blocks) if block != '.')
    return checksum

print()

with open(caminho_arquivo) as f:
    input_puzzle_grande = f.read().strip()

blocos = compactar_disco(input_puzzle_grande)
tempoA = time.time()
print('Começando a executar o código...')
print(somar(blocos))
tempoB = time.time()
print(f'{tempoB - tempoA} segundos')



