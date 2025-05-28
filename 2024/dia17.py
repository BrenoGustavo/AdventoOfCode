import time
information = '''Register A: 105875099912602
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,0,3,1,6,4,3,5,5,3,0'''

def pega_informacao(information):
    sections = information.split("\n\n")

    register_lines = sections[0].strip()
    programs = list(map(int, sections[1].split(': ')[1].split(',')))

    # print(register_lines)
    registers = {}
    for line in register_lines.splitlines():

        ID, value = line.split(': ')

        registers[ID[-1]] = int(value.strip())

    return registers, programs

registros, opcodes  = pega_informacao(information)

def read_operators(registros, opcodes):

    output = []

    def get_combo_operand(registros, operand):
        if 0 <= operand <= 3:
          return operand
        elif operand == 4:
            return registros['A']
        elif operand == 5:
            return registros['B']
        elif operand == 6:
            return registros['C']
        else:
            raise NotImplementedError

    i = 0
    while i < len(opcodes):
        # time.sleep(0.2)
        cur_upcode = opcodes[i]
        cur_operand = opcodes[i+1]
        # print(f'Cur output: {output}')
        # print(f'\tupcode: {cur_upcode}')
        if cur_upcode == 0: #adv
            numerator = registros['A']
            combo = get_combo_operand(registros, cur_operand)
            denominator = 2 ** combo 
            result = numerator / denominator
            registros['A'] = int(result)
        
        elif cur_upcode == 1: #bxl
            result = registros['B'] ^ cur_operand
            registros['B'] = result
            
        elif cur_upcode == 2: #bst
            combo = get_combo_operand(registros, cur_operand)
            result = combo % 8
            registros['B'] = result


        elif cur_upcode == 3: #jnz
            if registros['A'] == 0:
                i +=2
                continue
            else:
                i = cur_operand
                continue

        elif cur_upcode == 4: # bxc
            b = int(registros['B'])
            c = int(registros['C'])
            result = b ^ c
            registros['B'] = result

        elif cur_upcode == 5: # out
            combo = get_combo_operand(registros, cur_operand)
            result = combo % 8
            # time.sleep(0.2)
            # print(f'\t\tCombo: {combo},  Result: {result}')
            output.append(result)

        elif cur_upcode == 6: # bdv
            numerator = registros['A']
            combo = get_combo_operand(registros, cur_operand)
            denominator = 2 ** combo 
            result = numerator / denominator
            registros['B'] = result

        elif cur_upcode == 7:
            numerator = registros['A']
            combo = get_combo_operand(registros, cur_operand)
            denominator = 2 ** combo 
            result = numerator / denominator
            registros['C'] = result
        
        i +=2
    # print(registros['B'])
    return output

def parte1():
    resultado = read_operators(registros, opcodes)

    print(f'Resultado: {resultado}')
    print(f'Opcodes: {opcodes}')
    print(resultado == opcodes)


parte1()




