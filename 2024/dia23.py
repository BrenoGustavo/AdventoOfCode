import os
conexoes = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia23.txt')


with open(conexoes, 'r') as arquivo:

    conexoes_list = [linha.strip().split('-') for linha in arquivo.readlines()]


triples = []
for dupla in conexoes_list:
    pc1 = dupla[0]
    pc2 = dupla[1]

    for dupla_2 in conexoes_list:
        if set(dupla_2) != set(dupla):

            if pc1 in dupla_2:

                index = dupla_2.index(pc1)
                other_index = abs(index - 1)

                for dupla_3 in conexoes_list:

                    if dupla_2[other_index] in dupla_3 and pc2 in dupla_3:
                        triples.append((pc1, dupla_2[other_index], pc2))

            elif pc2 in dupla_2:
                index = dupla_2.index(pc2)
                other_index = abs(index - 1)

                for dupla_3 in conexoes_list:

                    if dupla_2[other_index] in dupla_3 and pc1 in dupla_3:

                        triples.append((pc1, dupla_2[other_index], pc2))


triples = set(triples)      

# Ordenar elementos de cada tupla e eliminar duplicatas usando um conjunto
unicas = set(tuple(sorted(tupla)) for tupla in triples)

# Converter de volta para lista (se necessário)
tuplas_unicas = list(unicas)

# Exibir o resultado
total = 0
for i in tuplas_unicas:
    for pc in i:
        if pc.startswith('t'):
            total+=1
            break

print(total)
