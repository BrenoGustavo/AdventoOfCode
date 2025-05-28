import os
import time
toalhas_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia19.txt')

with open(toalhas_txt, 'r') as arquivo:

    linhas = arquivo.readlines()
    available_towels = linhas[0].strip().split(', ')
    sequences = [linha.strip() for linha in linhas[1:] if linha.strip()]



tamanho_design = 0

def is_possible(design: str, padrões, tamanho_design, ja_foram):
    # if len(design) <=  tamanho_design:
    #     return False
    # if len(design) >  tamanho_design:
    #     tamanho_design = len(design)

    if design in ja_foram:
        return False
    
    ja_foram.add(design)
    
    # print('AQUI COMEÇA')
    # print(f'  {design}')
    # time.sleep(0.1)
    if not design:
        # print('not design')
        return True
    # print(design)
    for padrao in padrões:
        # print(design, padrao)
        if design.startswith(padrao):

            if len(padrao) <= len(design) and is_possible(design[len(padrao):], padrões, tamanho_design, ja_foram):
                return  True
    else:
        return False




def contar_designs_possíveis1(padrões, designs):
    total_possiveis = 0
    for design in designs:
        ja_foram = set()
        # print(f'Cur design: {design}')

        if is_possible(design, padrões, tamanho_design, ja_foram):
        
            total_possiveis+=1
        else:
            print(f'Não é possivel')


    return total_possiveis




t1 = time.time()

print(contar_designs_possíveis1(available_towels, sequences))

print(time.time() - t1)


            




            