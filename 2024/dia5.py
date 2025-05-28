import os 
import time
import pprint
caminho_input_regras = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia5.txt')
caminho_input_paginas = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia5b.txt')

with open(caminho_input_regras, 'r') as arquivo:

    ordering_rules = [list(map(int, linhas.replace('|', '\n').split())) for linhas in arquivo.readlines()]


with open(caminho_input_paginas, 'r') as arquivo:

    printing_pages = [list(map(int, linhas.replace(',', '\n').split())) for linhas in arquivo.readlines()]

regras = dict()


# print(ordering_rules)
# time.sleep(1)
# print(printing_pages)


for pprev, pnext in ordering_rules: 

    if pprev not in regras:
        regras[pprev] = []
    if pnext not in regras[pprev]:
        regras[pprev].append(pnext)


soma_dos_meios = 0

indice = 0
for p_updates in printing_pages:
    
    ordered = True

    for pagina in range(len(p_updates)-1):
        cur_page = p_updates[pagina]

        if cur_page not in regras:
            ordered = False
            break

        pages_in_front = p_updates[pagina+1:]

        for next_page in pages_in_front:
            if next_page in regras[cur_page]:
                # A sequencia segue a regra
                break
            else:
                ordered = False
            
    if ordered:
        meio = p_updates[len(p_updates)//2] 
        soma_dos_meios+=meio

    # else:
    #     print(f'Linha não ordenada.\n\tÍndice: ', indice)
    indice+=1

        

print(soma_dos_meios)

