import os
caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia22.txt')
with open(caminho_arquivo, 'r') as arquivo:
    numeros = [int(i) for i in arquivo.readlines()]

def make_secret_number(secret):

    result1a = (secret* 64)
    result1b = result1a ^ secret
    result1c = result1b  % 16777216
    # print(f'\t{result1c}')

    result2a = (result1c // 32)
    result2b = result2a ^ result1c
    result2c = result2b % 16777216


    # print(f'\t{result2c}')
    result3a = (result2c * 2048) 
    result3b = result3a ^ result2c
    result3c = result3b % 16777216
    # print(f'\t{result3b}')
    # print(result3b)
    return result3c

# print(make_secret_number(123))


def somar_200th(lista_numeros):
    total = 0
    for secret in lista_numeros:
        for _ in range(2000):

            new = make_secret_number(secret)
            # print(new)
            secret = new

        total += secret
    return total

teste = [1, 10, 100, 2024]

print(somar_200th(numeros))



