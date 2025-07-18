import pathlib

def checar_mul_part1(string: str):
    lista_expressoes = []
    mul = 'mul('

    for i in range(len(string)):
        open = False
        comma = False

        primeiros_digitos = []
        segundos_digitos = []
        letras = string[i:i+4]
        if letras == mul:
            sequencia = string[i+3:i+12]
            for character in sequencia:
                if character == '(':
                    open = True

                elif open and character.isdigit() and not comma:
                    primeiros_digitos.append(int(character))

                elif open and character.isdigit() and comma:
                    segundos_digitos.append(int(character))

                elif open and character == ',':
                    comma = True

                elif open and comma and character == ")":
                    comma = False
                    open = False

                    antes_virgula = int(''.join([str(n) for n in primeiros_digitos]))
                    depois_virgula = int(''.join([str(n) for n in segundos_digitos]))
                    lista_expressoes.append([antes_virgula, depois_virgula])
                    break
                else:
                    break
    return lista_expressoes

def checar_mul_part2(string: str):
    lista_expressoes = []
    mul = 'mul('
    do_str = 'do()'
    dont_str = "don't()"
    do = True

    for i in range(len(string)):
        open = False
        comma = False

        primeiros_digitos = []
        segundos_digitos = []
        letras = string[i:i+4]
        letras_dont = string[i:i+7]

        if letras_dont == dont_str:
            do = False
        elif letras == do_str:
            do = True

        if do and letras == mul:
            sequencia = string[i+3:i+12]
            for character in sequencia:
                if character == '(':
                    open = True

                elif open and character.isdigit() and not comma:
                    primeiros_digitos.append(int(character))

                elif open and character.isdigit() and comma:
                    segundos_digitos.append(int(character))

                elif open and character == ',':
                    comma = True

                elif open and comma and character == ")":
                    comma = False
                    open = False

                    antes_virgula = int(''.join([str(n) for n in primeiros_digitos]))
                    depois_virgula = int(''.join([str(n) for n in segundos_digitos]))
                    lista_expressoes.append([antes_virgula, depois_virgula])
                    break
                else:
                    break
    return lista_expressoes

def soma_multiplicacoes(lista_expressoes):
    return sum(x * y for x, y in lista_expressoes)

def part_1(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    expressoes = checar_mul_part1(data)
    return soma_multiplicacoes(expressoes)

def part_2(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    expressoes = checar_mul_part2(data)
    return soma_multiplicacoes(expressoes)

def main():
    day = 3
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))

if __name__ == "__main__":
    main()
