def parse_disk(disk_map):
    """Transforma a string do disco em uma lista de blocos."""
    ''' Transforma a string em uma lista de elementos'''
    blocks = []
    index = 0
    while index < len(disk_map):
        size = int(disk_map[index])
        blocks.append(size)
        index += 1
    return blocks

def generate_disk(blocks):
    """Gera a representação detalhada do disco com IDs e espaços livres."""
    disk = []
    current_id = 0
    for i, block_size in enumerate(blocks):
        if i % 2 == 0:  # Arquivo
            disk.extend([str(current_id)] * block_size)
            current_id += 1
        else:  # Espaço livre
            disk.extend(['.'] * block_size)
    return disk

def compact_files(disk):
    """Compacta os arquivos conforme as regras da Parte 2."""
    max_id = max(int(ch) for ch in disk if ch != '.')
    for file_id in range(max_id, -1, -1):
        file_id = str(file_id)
        # Localizar o arquivo no disco
        file_start = disk.index(file_id)
        file_end = len(disk) - 1 - disk[::-1].index(file_id)
        file_length = file_end - file_start + 1
        
        # Encontrar espaço livre suficiente à esquerda
        best_start = None
        for i in range(file_start):
            if all(c == '.' for c in disk[i:i + file_length]):    #Genial !!!!!! Revisar depois esse algoritmo
                best_start = i
                break
        
        if best_start is not None:
            # Remover o arquivo de sua posição atual
            for i in range(file_start, file_end + 1):
                disk[i] = '.'
            # Inserir o arquivo no espaço encontrado
            for i in range(best_start, best_start + file_length):
                disk[i] = file_id
    return disk

def calculate_checksum(disk):
    """Calcula o checksum do disco."""
    checksum = 0
    for idx, block in enumerate(disk):
        if block != '.':
            checksum += idx * int(block)
    return checksum

# Entrada do problema

import time
import os
tempoa = time.time()
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia9.txt')
print(caminho_arquivo)

with open(caminho_arquivo) as f:
    input_puzzle_grande = f.read().strip()


# Parsear e gerar o disco inicial
blocks = parse_disk(input_puzzle_grande)

disk = generate_disk(blocks)

# Compactar os arquivos
compacted_disk = compact_files(disk)

# Calcular o checksum
checksum = calculate_checksum(compacted_disk)

print("Checksum:", checksum)
