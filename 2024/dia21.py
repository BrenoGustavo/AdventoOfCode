codes = '''029A
980A
179A
456A
379A
'''


lista_de_codes = []

for code in codes.splitlines():

    lista_de_codes.append([int(i) if i.isnumeric() else i for i in code])


robot_pad = [
    [None, '^', 'A'],
     ['<', 'v', '>']
      ]

num_pad = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, 'A']
]

def encontrar_coordenadas(painel, valor):
    for i, linha in enumerate(painel):
        if valor in linha:
            return (i, linha.index(valor))
    return None

def menor_caminho_com_movimentos(painel, sequencia):
    movimentos_totais = 0
    movimentos = []
    direcoes = {
        (-1, 0): "^",
        (1, 0): "v",
        (0, -1): "<",
        (0, 1): ">"
    }

    posicao_atual = encontrar_coordenadas(painel, 'A')

    for proximo in sequencia:
        proxima_posicao = encontrar_coordenadas(painel, proximo)
        if posicao_atual and proxima_posicao:
            # Calcula o deslocamento
            deslocamento_linha = proxima_posicao[0] - posicao_atual[0]
            deslocamento_coluna = proxima_posicao[1] - posicao_atual[1]

            # Movimentos verticais
            for _ in range(abs(deslocamento_linha)):
                movimentos.append(direcoes[(1 if deslocamento_linha > 0 else -1, 0)])

            # Movimentos horizontais
            for _ in range(abs(deslocamento_coluna)):
                movimentos.append(direcoes[(0, 1 if deslocamento_coluna > 0 else -1)])
            
            # Adicionar "A" para apertar o botão


            # Soma os movimentos
            movimentos_totais += abs(deslocamento_linha) + abs(deslocamento_coluna)
            movimentos.append('A')
            posicao_atual = proxima_posicao

    return movimentos_totais, movimentos

def encontrar_caminho(numpad, sequencia):

    _, caminho = menor_caminho_com_movimentos(num_pad, sequencia)
    print(''.join(caminho))
    _, caminho2 = menor_caminho_com_movimentos(robot_pad, caminho)
    print(''.join(caminho2))

    _, caminho3 = menor_caminho_com_movimentos(robot_pad, caminho2)
    print(''.join(caminho3))
    print(len(caminho3))
    return len(caminho3)


total = 0

for codigo in lista_de_codes:
    print(codigo)
    numeric = int(''.join([str(i) for i in codigo[:-1]]))
    tamanho_caminho = encontrar_caminho(num_pad, codigo)

    # print(f'Tamanho do caminho: {tamanho_caminho}')
    # print(f'Parte numerica: {numeric}')
    mutipricacao = numeric * tamanho_caminho
    total += mutipricacao

print(total)



