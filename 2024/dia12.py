import os
from collections import Counter, deque
import time
puzzle_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia12.txt')

with open(puzzle_txt, 'r') as arquivo:
    FARM = [list(linha.strip()) for linha in arquivo.readlines()]

def find_region(farm, i, j, region_spots:set[tuple[int, int]]): # RETORNAR A QUANTIDADE DE CASA QUE UMA REGIÃO TEM

    spots_queue = deque()
    region_spots.add((i,j))
    cur_spot = farm[i][j]

    lados = 4

    if j+1 < len(farm[i]) and farm[i][j+1] == cur_spot:
        if (i,j+1) in region_spots:
            lados-=1
        else:
            spots_queue.append((i, j+1))
            region_spots.add((i, j+1))
            lados-=1

    if j - 1 >= 0  and farm[i][j-1] == cur_spot:
        if (i,j-1) in region_spots:
            lados-=1
        else:
            spots_queue.append((i, j-1))
            region_spots.add((i, j-1))
            lados-=1

    if i - 1 >= 0 and farm[i-1][j] == cur_spot:
        if (i-1,j) in region_spots:
            lados-=1
        else:         
            spots_queue.append((i-1, j))
            region_spots.add((i-1, j))
            lados-=1
        
    if i + 1 < len(farm) and farm[i+1][j] == cur_spot:
        if (i+1, j) in region_spots:
            lados-=1
        else:
            spots_queue.append((i+1, j))
            region_spots.add((i+1, j))
            lados-=1

    quantidade = len(region_spots)

    while spots_queue:

        popped = spots_queue.popleft()
        # print('Popped: ', popped)
        i_, j_ = popped[0], popped[1]
        new_spots, perimeter = find_region(farm ,i_, j_, region_spots)
        region_spots.union(new_spots)

        # for square in new_spots:
        #     region_spots.add(square)
        lados += perimeter

    # print(f'O que foi checado: {i,j} ; lados: {lados}')
    return region_spots, lados 

# I_e_J = (6, 0)
# spots = set()
# spots.add(I_e_J)
# regioes, qtds_lados = find_region(FARM, 6, 0, spots)
# print(FARM[6][0])

# print(qtds_lados)
# print(regioes)
# print(len(regioes))

regioes_dict = dict()
contador = Counter()
fences_counter = Counter()


for L in range(len(FARM)):
    for C in range(len(FARM[L])):
        coords = set()
        regiao, lados = find_region(FARM, L, C, coords)



        if FARM[L][C] in regioes_dict:
            if regiao == regioes_dict[FARM[L][C]]:
                continue

            regiao_plantas = [set(r) for r in regioes_dict.values()]
            if regiao in regiao_plantas:
                continue

            if regiao == set(regioes_dict[FARM[L][C]]):
                continue
            else:
                contador[FARM[L][C]] +=1
                ATUAL = FARM[L][C]
                CONTAGEM = contador[FARM[L][C]]
                NEW_REGION = str(ATUAL) + str(CONTAGEM)

                regioes_dict[NEW_REGION] = []
                regioes_dict[NEW_REGION].extend(regiao)
                fences_counter[NEW_REGION] += lados
                # print('Regiao separada')

        else:
            regioes_dict[FARM[L][C]] = []
            # print(f'Região de {FARM[L][C]}: {regiao}')
            regioes_dict[FARM[L][C]].extend(regiao)
            fences_counter[FARM[L][C]] += lados


# for a, b in regioes_dict.items():
#     print(a, b)

        

categoria = 'A'

valores_categoria = []
for chave, valores in regioes_dict.items():
    if chave.startswith(categoria):
        valores_categoria.extend(valores)

# print(fences_counter.keys())
# print(regioes_dict.keys())


somatoria = 0
for KEY in fences_counter.keys():
    partial = 0
    AREA = len(regioes_dict[KEY])
    CERCAS = fences_counter[KEY]
    partial = AREA * CERCAS
    somatoria += partial

print(somatoria)












