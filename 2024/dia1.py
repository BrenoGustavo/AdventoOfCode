import os
import pathlib

nome_arquivo_txt ='INPUT.txt'
current_directory = os.path.dirname(os.path.abspath(__file__))
input_text = os.path.join(current_directory, nome_arquivo_txt)


"""
Objetivos de aprendizado
-Compreender melhor a função map
-Melhorar lógica de programação
"""

def somando_minimos(caminho_arquivo):

    with open(caminho_arquivo, 'r') as arquivo:

        left, right = zip(*(map(int, linha.split()) for linha in arquivo))

        left, right = sorted(left), sorted(right)

        return sum(abs(a - b) for a, b in zip(left, right))
    


print(somando_minimos(input_text))



"""
Aprendizado:
-Função Map transforma cada valor de iteráveis
-Ao fazer For em u arquivo.txt, o curso vai avançando, e ao final, a lista se esgota
-Utilizar arquivo.seek(0) para reiniciar o cursor
"""

