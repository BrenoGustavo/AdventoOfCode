INPUT_PUZZLE = '1950139 0 3 837 6116 18472 228700 45'


PEDRAS = [int(i) for i in INPUT_PUZZLE.split()]

'''Metodo 1'''
# def blink(pedras, blinks: int):
#     if blinks == 0:
#         return pedras
#     # print('\t', pedras)
    
#     i = 0
#     while i < len(pedras):
#         if pedras[i] == 0:
#             pedras[i] = 1
#             i +=1
    
#         elif len(str(pedras[i])) % 2 == 0:
#             idx_ = int(len(str(pedras[i])) / 2)
#             pedras[i:i+1] = [int(str(pedras[i])[:idx_]), int(str(pedras[i])[idx_:])]

#             i +=2

#         else:
#             pedras[i] = pedras[i] * 2024

#             i +=1
#     # print('\t\t', pedras)
#     return blink(pedras, blinks-1)



# pedras_piscadas = blink(PEDRAS, 25)
# print(len(pedras_piscadas))

# from collections import deque
'''Metodo 2'''
# def simular_pedras(pedras_iniciais, piscadas):
#     fila = deque(pedras_iniciais)
#     for _ in range(piscadas):
#         for _ in range(len(fila)):
#             pedra = fila.popleft()
#             # Processa a pedra de acordo com as regras
#             if pedra == 0:
#                 fila.append(1)
#             elif len(str(pedra)) % 2 == 0:
#                 meio = len(str(pedra)) // 2
#                 esquerdo = int(str(pedra)[:meio])
#                 direito = int(str(pedra)[meio:])
#                 fila.append(esquerdo)
#                 fila.append(direito)
#             else:
#                 fila.append(pedra * 2024)
#     return len(fila)


# print(simular_pedras(PEDRAS, 75))


'''Metodo 3'''

from collections import Counter

def calcular_pedras_otimizado(pedras_iniciais, piscadas):
    # Contagem inicial das pedras
    contagem = Counter()
    for pedra in pedras_iniciais:
        contagem[pedra] += 1

    for _ in range(piscadas):
        nova_contagem = Counter()

        for pedra, quantidade in contagem.items():
            if pedra == 0:
                nova_contagem[1] += quantidade  # Regra 1
            elif len(str(pedra)) % 2 == 0:
                # Regra 2: Divisão
                meio = len(str(pedra)) // 2
                esquerdo = int(str(pedra)[:meio])
                direito = int(str(pedra)[meio:])
                nova_contagem[esquerdo] += quantidade
                nova_contagem[direito] += quantidade
            else:
                # Regra 3: Multiplicação
                nova_contagem[pedra * 2024] += quantidade

        contagem = nova_contagem

    # Soma o número total de pedras
    # return sum(contagem.values())
    return contagem.total()

# Exemplo de uso
pedras_iniciais = PEDRAS
piscadas = 75

resultado = calcular_pedras_otimizado(pedras_iniciais, piscadas)
print("Número total de pedras após 75 piscadas:", resultado)

