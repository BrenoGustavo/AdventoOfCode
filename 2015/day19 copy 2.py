from collections import deque
import re

def parse_input(input_data):
    """Parses the replacement rules and the target molecule from input."""
    replacements = []
    molecule = None
    for line in input_data.strip().split("\n"):
        if " => " in line:
            src, dest = line.split(" => ")
            replacements.append((dest, src))  # Reverse direction
        else:
            molecule = line.strip()
    return replacements, molecule

def bfs_reduce_molecule(molecule, replacements):
    """Uses BFS to find the minimum steps from molecule to 'e'."""
    queue = deque([(molecule, 0)])  # (current molecule, steps taken)
    visited = set()

    while queue:
        current_molecule, steps = queue.popleft()

        if current_molecule == "e":
            return steps  # Return the shortest path found

        for before, after in replacements:
            for match in list(re.finditer(before, current_molecule)):
                new_molecule = (
                    current_molecule[:match.start()] +
                    after +
                    current_molecule[match.end():]
                )

                if new_molecule not in visited:
                    visited.add(new_molecule)
                    queue.append((new_molecule, steps + 1))

    return None  # If no solution is found (shouldn't happen with valid input)

# Puzzle input
input_data = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr
"""

# Parse input
replacements, target_molecule = parse_input(input_data)

# Solve using BFS
steps = bfs_reduce_molecule(target_molecule, replacements)
print("Minimum steps to create the molecule:", steps)
