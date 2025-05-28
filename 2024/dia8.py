PUZZLE_INPUT = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''



'''
dict contendo chaves de linhas
cada chave linha contem outro dict contendo as colunas para cada valor de linha
True se existir antena, else False


se indice linha ou coluna exceder 50/12 (tamanho do input), pular;
se estiver dentro do limite, criar no dict um hash ligando a coordenada

aplicar for checando cada antena com frequencia diferentes;
ao achar uma nova, incluir coordenada no dict continuar o for para achar outra antena igual
e ao encontrar, pegar a coordenada e substituir


'''
from inputdia8 import ANTENAS
from itertools import combinations
ANTENAS_TESTE = [list(linha.strip()) for linha in PUZZLE_INPUT.splitlines()]
ANTENAS_PUZZLE = [list(linha.strip()) for linha in ANTENAS.splitlines()]




def mapear_antenas(antenas): # Retorna um dict com as coordenadas de cada tipo de antena

    def encontrar_indices(lista, valor): # Retorna uma lista com as coordenadas da antena X
        indices = []
        for i, linha in enumerate(lista):
            for j, elemento in enumerate(linha):
                if elemento == valor:
                    indices.append((i, j))  # Adiciona a posição (linha, coluna)
        return indices
    
    encontradas = []
    coordenadas_antenas = dict()
    for i in range(len(antenas)):
        for j in range(len(antenas[i])):
            cur_local = antenas[i][j]
            if cur_local != '.':
                if cur_local not in encontradas:
                    encontradas.append(cur_local)
                    coordenadas_antenas[cur_local] = encontrar_indices(antenas, cur_local)

    return coordenadas_antenas


def antinodes(combinacao_antenas, tamanho: int): # Retorna um set com as coordenadas dos antinodes de um tipo de antena
    
    nodes = set()
    for dupla in combinacao_antenas:
        coord1 = dupla[0]
        coord2 = dupla[1]

        coord1_x = coord1[0]
        coord1_y = coord1[1]
        coord2_x = coord2[0]
        coord2_y = coord2[1]

        try:
            tg = (coord2_y - coord1_y ) / (coord2_x - coord1_x)
            print(f'Pontos `{coord1} e {coord2}')
            print(f'Tangente: {tg}')
        except ZeroDivisionError:
            tg = False

        diff_x = abs(coord2_x - coord1_x)
        diff_y = abs(coord2_y - coord1_y)

        if tg >= 0:
            new_node_1 = (max(coord1_x, coord2_x) + diff_x, max(coord1_y, coord2_y) + diff_y)
            new_node_2 = (min(coord1_x, coord2_x) - diff_x, min(coord1_y, coord2_y) - diff_y)

        elif tg < 0:
            new_node_1 = (max(coord1_x, coord2_x) + diff_x, min(coord1_y, coord2_y) - diff_y)
            new_node_2 = (min(coord1_x, coord2_x) - diff_x, max(coord1_y, coord2_y) + diff_y)

        elif tg == False:
            new_node_1 = (coord1_x, min(coord1_y, coord2_y) - diff_y)
            new_node_2 = (coord1_x, max(coord1_y, coord2_y) + diff_y)
        else:
            print('wtff?')

        if all(0 <= valor < tamanho for valor in new_node_1):
            nodes.add(new_node_1)
        if all(0 <= valor < tamanho for valor in new_node_2):
            nodes.add(new_node_2)

        print(f'\tNew nodes: {new_node_1} e {new_node_2}')
        
    return nodes



def encontrar_coordenadas_antinodes(coordenadas_antenas:dict): # teste: dicionario 
    # print(' EXECUTANDO encontrar_coordenadas_antinodes')
    coordenadas_antinodes = set()
    for tipo_antena, coordenadas in coordenadas_antenas.items():

        print(tipo_antena, coordenadas)
        duplas = list(combinations(coordenadas, 2))
        # print(f'Duplas: {duplas}\t\n')
        # novas_coordenadas = antinodes(duplas, 50)
        novas_coordenadas = antinodes(duplas, 50)
        # print(f"Novas coordenadas: {novas_coordenadas}")
        print(f'\t {novas_coordenadas}')
        coordenadas_antinodes = coordenadas_antinodes | novas_coordenadas
    print()
    return coordenadas_antinodes


for l in ANTENAS_PUZZLE:
    print(''.join(l))

print('-'*50)
for linha in ANTENAS_TESTE:
    print(linha)
antenas_e_coordenadas = mapear_antenas(ANTENAS_PUZZLE)
ANTINODES_COORDINATES = encontrar_coordenadas_antinodes(antenas_e_coordenadas)

print(len(ANTINODES_COORDINATES))





