
from pathlib import Path
import json
import re
import json

puzzle_input = Path(__file__).parent / 'inputday12.txt'
with open(puzzle_input, 'r') as archive:
    json_input = archive.read()

def part1():
    def find_all_ints(text):    
        padrao = r"[+-]?\d+"
        return re.findall(padrao, text)

    def sum_all(list):
        
        total = sum(int(i) for i in list) 
        return total

    numbers = find_all_ints(json_input)


    total = sum_all(numbers)

    print(f'The sum of all numbers in the document is {total}')



def ler_json_de_txt(arquivo_txt):
    with open(arquivo_txt) as arquivo:
        dados_json = arquivo.read()
        return json.loads(dados_json)

def ignore_red(data)-> int:
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(ignore_red(value) for value in data.values() if value)

    elif isinstance(data, list):
        return sum(ignore_red(i) for i in data if i)

    elif isinstance(data, int):
        return data
    return 0
    
def part2():

    data = ler_json_de_txt(puzzle_input)
    resultado = ignore_red(data)
    print(resultado)
part1()
part2()
    

            


