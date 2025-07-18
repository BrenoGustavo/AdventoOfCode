"""
Simulador de um computador de 3 bits com registradores A, B e C.
Parte 1: Executa um programa interpretando os opcodes e operandos, com suporte a instruções de divisão, XOR, salto condicional, etc.
Parte 2: Busca o menor valor para o registrador A que faça o programa imprimir uma cópia exata de si mesmo.
"""

import pathlib


def pega_informacao(information):
    sections = information.split("\n\n")

    register_lines = sections[0].strip()
    programs = list(map(int, sections[1].split(": ")[1].split(",")))

    registers = {}
    for line in register_lines.splitlines():
        ID, value = line.split(": ")
        registers[ID[-1]] = int(value.strip())

    return registers, programs


def get_combo_operand(registros, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registros["A"]
    elif operand == 5:
        return registros["B"]
    elif operand == 6:
        return registros["C"]
    else:
        raise NotImplementedError


def part_1(file_path):
    with open(file_path) as file:
        information = file.read()

    registros, opcodes = pega_informacao(information)
    output = []
    i = 0

    while i < len(opcodes):
        cur_upcode = opcodes[i]
        cur_operand = opcodes[i + 1]

        if cur_upcode == 0:  # adv
            numerator = registros["A"]
            denominator = 2 ** get_combo_operand(registros, cur_operand)
            registros["A"] = int(numerator / denominator)

        elif cur_upcode == 1:  # bxl
            registros["B"] ^= cur_operand

        elif cur_upcode == 2:  # bst
            registros["B"] = get_combo_operand(registros, cur_operand) % 8

        elif cur_upcode == 3:  # jnz
            if registros["A"] != 0:
                i = cur_operand
                continue

        elif cur_upcode == 4:  # bxc
            registros["B"] = int(registros["B"]) ^ int(registros["C"])

        elif cur_upcode == 5:  # out
            output.append(get_combo_operand(registros, cur_operand) % 8)

        elif cur_upcode == 6:  # bdv
            numerator = registros["A"]
            denominator = 2 ** get_combo_operand(registros, cur_operand)
            registros["B"] = numerator / denominator

        elif cur_upcode == 7:  # cdv
            numerator = registros["A"]
            denominator = 2 ** get_combo_operand(registros, cur_operand)
            registros["C"] = numerator / denominator

        i += 2

    return ",".join(map(str, output))


def run(a: int, b: int):
    output = ""
    while a != 0:
        b = (a % 8) ^ (a // (2 ** ((a % 8) ^ 5))) ^ 3
        output += str(b % 8) if not output else f",{b % 8}"
        a //= 8
    return output


def part_2():
    expected = "2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0"

    ras = []
    for i in range(1, 8):
        output = run(i, 0)
        if output == expected[-len(output) :]:
            ras.append(i)

    octal_digit_count = 1
    while octal_digit_count < 16:
        new_ras = []
        for a in ras:
            a *= 8
            for i in range(8):
                output = run(a + i, 0)
                if output == expected[-len(output) :]:
                    new_ras.append(a + i)
        ras = new_ras
        octal_digit_count += 1

    return min(ras)


def main():
    day = 17
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2())


if __name__ == "__main__":
    main()
