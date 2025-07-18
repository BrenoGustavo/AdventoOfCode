"""
Day 24 - Crossed Wires

Parte 1:
  - Simula a propagação de sinais booleanos por portas lógicas AND, OR, XOR.
  - Concatena os valores finais dos fios zXX como binário e retorna o número decimal.

Parte 2:
  - A rede representa a soma de dois números binários formados por fios x* e y*.
  - Detecta exatamente 4 pares de portas com suas saídas trocadas.
  - Retorna os nomes dos 8 fios trocados ordenados alfabeticamente e unidos por vírgula.
"""

from collections import defaultdict
import pathlib


def parse_input(caminho):
    with open(caminho) as f:
        raw_data = f.read()

    values = {}
    ops = []

    # Primeira parte: valores iniciais dos fios
    for line in raw_data.split("\n\n")[0].splitlines():
        name, value = line.split(": ")
        values[name] = int(value)

    # Segunda parte: operações lógicas (gates)
    for line in raw_data.split("\n\n")[1].splitlines():
        inp1, gate, inp2 = line.split(" ->")[0].split(" ")
        out = line.split("-> ")[1]
        ops.append((inp1, inp2, gate, out))

    return values, ops


def simulate_circuit(values, ops):
    while True:
        missing = 0
        for inp1, inp2, gate, out in ops:
            if out in values:
                continue
            if inp1 not in values or inp2 not in values:
                missing += 1
                continue

            match gate:
                case "OR":
                    values[out] = values[inp1] | values[inp2]
                case "AND":
                    values[out] = values[inp1] & values[inp2]
                case "XOR":
                    values[out] = values[inp1] ^ values[inp2]

        if missing == 0:
            break

    return values


def solve_part1(caminho):
    values, ops = parse_input(caminho)
    final_values = simulate_circuit(values, ops)

    # Pegar apenas os fios que começam com 'z' e montar o número binário
    output = 0
    for k, v in final_values.items():
        if k.startswith("z"):
            output |= v << int(k[1:])

    print("Parte 1:", output)
    return output, ops


def highest_bit(n):
    """Retorna o índice do bit mais significativo de n."""
    if not n:
        return None
    bit = 0
    while n:
        n >>= 1
        bit += 1
    return bit - 1


def solve_part2(output, ops):
    # Determinar uso de cada fio por tipo de gate
    usage = defaultdict(set)
    for inp1, inp2, gate, _ in ops:
        usage[inp1].add(gate)
        usage[inp2].add(gate)

    last_output = f"z{highest_bit(output)}"
    errors = []

    for inp1, inp2, gate, out in ops:
        if out == last_output:
            if inp1[0] in "xy" or inp2[0] in "xy" or gate != "OR":
                errors.append(out)
            continue

        if out == "z00":
            if sorted([inp1, inp2]) != ["x00", "y00"] or gate != "XOR":
                errors.append(out)
            continue

        if "x00" in (inp1, inp2) or "y00" in (inp1, inp2):
            if (inp1[0] == "x" and inp2[0] == "y") or (
                inp1[0] == "y" and inp2[0] == "x"
            ):
                if gate not in ("XOR", "AND"):
                    errors.append(out)
            continue

        if gate == "XOR":
            if inp1[0] in "xy":
                if inp2[0] not in "xy":
                    errors.append(out)
                if out[0] == "z":
                    errors.append(out)
                if not {"AND", "XOR"}.issubset(usage[out]):
                    errors.append(out)
            elif out[0] != "z":
                errors.append(out)

        elif gate == "OR":
            if inp1[0] in "xy" or inp2[0] in "xy" or out[0] == "z":
                errors.append(out)
            if not {"AND", "XOR"}.issubset(usage[out]):
                errors.append(out)

        elif gate == "AND":
            if inp1[0] in "xy" and inp2[0] not in "xy":
                errors.append(out)
            if "OR" not in usage[out]:
                errors.append(out)

    errors = sorted(set(errors))
    assert len(errors) == 8, f"Esperado 8 fios, mas encontrei {len(errors)}"
    print("Parte 2:", ",".join(errors))


def main():
    day = 24
    caminho = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    output, ops = solve_part1(caminho)
    solve_part2(output, ops)


if __name__ == "__main__":
    main()
