from pathlib import Path
from collections import defaultdict
import re

puzzle_input_txt = Path(__file__).parent / 'inputday19.txt'

with open(puzzle_input_txt, 'r') as archive:
    lines, molecule = archive.read().strip().split('\n\n')
    lines = lines.splitlines()
    replacements = []
    for r in lines:
        mol1, mol2 = r.split(' => ')
        replacements.append((mol1, mol2))


def min_steps_greedy(target, replacements):
    # Reverse the replacements to work backwards from the target to 'e'
    reverse_replacements = sorted(
        [(value, key) for key, value in replacements],
        key=lambda x: -len(x[0])  # Sort by length of the replacement in descending order
    )
    
    steps = 0
    molecule = target
    
    while molecule != 'e':
        for replacement, precursor in reverse_replacements:
            if replacement in molecule:
                # Replace the first occurrence of the replacement with the precursor
                molecule = molecule.replace(replacement, precursor, 1)
                steps += 1
                break
        else:
            # If no replacement can be applied, the molecule cannot be reduced to 'e'
            return -1
    
    return steps


# Calculate the minimum number of steps
result = min_steps_greedy(molecule, replacements)
print("Minimum number of steps:", result)