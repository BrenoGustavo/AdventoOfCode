import os

warehouse_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia15.txt')
print(warehouse_txt)
def map_reader(warehouse_txt):
    # c:\Users\bregu\Desktop\Python\Projetos\AOC\inputdia15.txt
    with open(warehouse_txt, 'r') as arquivo:
        linhas = arquivo.readlines()

    mapa = []
    direcoes = ""

    # Processar as linhas
    for linha in linhas:
        # Identifica linhas do mapa (linhas que começam com #)
        if linha.startswith("#"):
            mapa.append(list(linha.strip()))  # Adiciona cada linha do mapa como uma lista de caracteres
        # Caso contrário, são direções
        elif linha.strip():  # Ignora linhas em branco
            direcoes += linha.strip()  # Adiciona direções à string, removendo quebras de linha

    return mapa, direcoes

warehouse, directions = map_reader(warehouse_txt)

def find_initial_pos(mapa):
    for y, linha in enumerate(mapa):

        if "@" in linha:
            x = linha.index('@')
            return (y, x)
    return None, None

robot_y, robot_x = find_initial_pos(warehouse)

print(robot_y, robot_x)





mapa = warehouse
direcao_atual = '^'
pos_atual = (robot_y, robot_x)

print(pos_atual)

if direcao_atual == '^':...





if direcao_atual == '>':...
if direcao_atual == 'v':...
if direcao_atual == '<':...