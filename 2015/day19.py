from pathlib import Path
from collections import defaultdict
import re

puzzle_input_txt = Path(__file__).parent / 'inputday19.txt'
def part1():
    def parse_input(puzzle_input):
        with open(puzzle_input, 'r') as archive:
            replacements, molecule = archive.read().strip().split('\n\n')
            replacements = replacements.splitlines()
            molecules_replacements = defaultdict(list)
            for r in replacements:
                mol1, mol2 = r.split(' => ')
                molecules_replacements[mol1].append(mol2)
        
        return molecules_replacements, molecule
    def generate_molecules(replacements, molecule):
        "Generate all possible molecules by applying one replacement"
        all_molecules = set()
        for mol, repl in replacements.items():
            for repl_mols in repl:
                # Find all ocurrences of mol in the molecule
                for match in re.finditer(mol, molecule):
                    new_molecule = molecule[:match.start()] + repl_mols + molecule[match.end():]
                    all_molecules.add(new_molecule)
        
        return all_molecules


    replacements, molecule = parse_input(puzzle_input_txt)
    molecules = generate_molecules(replacements, molecule)

    print(f'The number of distinct molecules: {len(molecules)}')

# part1()

def part2():
    import re
    import random

    def parse_input(input_text):
        replacements = []
        molecule = ""
        for line in input_text.strip().split("\n"):
            if "=>" in line:
                src, dst = line.split(" => ")
                replacements.append((dst, src))  # Invertendo para redução
            elif line:
                molecule = line
        return replacements, molecule

    def min_steps_to_synthesize(molecule, replacements):
        steps = 0
        while molecule != "e":
            for dst, src in replacements:
                if src in molecule:
                    molecule = molecule.replace(src, dst, 1)
                    steps += 1
                    break  # Reinicia a busca
            else:
                random.shuffle(replacements)  # Evita loops
                steps = 0  # Reinicia a contagem
                molecule = target  # Começa novamente
        return steps

    # Exemplo de entrada
    data = """
    H => HO
    H => OH
    O => HH
    e => H
    e => O
    "
    HOHOHO
    """
    replacements, target = parse_input(data)
    steps = min_steps_to_synthesize(target, replacements)
    print("Mínimo de passos necessários:", steps)
part2()

