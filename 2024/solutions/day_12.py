"""
Dia 12 - Lavaterras

Este script analisa um mapa 2D com regiões rotuladas (por exemplo, com letras ou símbolos) e calcula:

- Parte 1: A soma da área de cada região multiplicada pelo seu perímetro.
- Parte 2: A soma da área de cada região multiplicada pelo número de voltas (curvas) que seu contorno realiza.

A lógica detecta regiões conectadas (áreas com o mesmo rótulo), contorna seus limites, e aplica as fórmulas desejadas.
"""

import pathlib


def carregar_mapa(file_path):
    input_locs = [line for line in open(file_path).read().splitlines()]
    locs = {
        complex(i, j): input_locs[j][i]
        for j in range(len(input_locs))
        for i in range(len(input_locs[0]))
    }
    return input_locs, locs


def calcular_areas(locs):
    deltas = {1, -1, 1j, -1j}
    all_deltas = {1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}

    neighs = {
        l: [l + d for d in deltas if l + d in locs and locs[l + d] == locs[l]]
        for l in locs
    }

    outside_neighs = {
        l: set([l + d for d in deltas if l + d not in neighs[l]]) for l in locs
    }

    def get_area(z, areas):
        if any(z in A for A in areas):
            return False
        area = set([z])
        front = set([z])
        while front:
            front = set(w for x in front for w in neighs[x] if w not in area)
            area.update(front)
        return area

    def get_perimeter(area):
        outs = []
        for a in area:
            outs += outside_neighs[a]
        return len(outs)

    def get_sides(area):
        turns = 0
        border = set(z + d for z in area for d in all_deltas if z + d not in area)
        ccw = -1j
        cw = 1j

        out_done = False
        while border:
            r = 1 + 0j
            d = -1j

            if not out_done:
                left_pts = [z for z in border if z.real == min(z.real for z in border)]
                down = [z for z in left_pts if z.imag == max(z.imag for z in left_pts)]
                p = down[0]
                seen = set([(p, d)])
                done = set([p])
                out_done = True
            else:
                right_pts = [z for z in border if z.real == max(z.real for z in border)]
                down = [
                    z for z in right_pts if z.imag == max(z.imag for z in right_pts)
                ]
                p = down[0]
                seen.add((p, d))
                done.add(p)

            while True:
                if p + d in border and p + d + r in area:
                    p += d
                elif (p + d in border and p + d + r not in area and p + r in area) or (
                    p + d in area and p + d + r in border
                ):
                    p += d
                    d *= cw
                    r *= cw
                    turns += 1
                elif p + d in area:
                    d *= ccw
                    r *= ccw
                    turns += 1
                if (p, d) not in seen:
                    seen.add((p, d))
                    done.add(p)
                else:
                    break

            border -= done
        return turns

    total1 = total2 = 0
    areas = []

    for l in locs.keys():
        a = get_area(l, areas)
        if a:
            areas.append(a)
            total1 += len(a) * get_perimeter(a)
            total2 += len(a) * get_sides(a)

    return total1, total2


def part_1_e_2(locs):
    return calcular_areas(locs)


def main():
    day = 12
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    _, locs = carregar_mapa(puzzle_path)

    part1, part2 = part_1_e_2(locs)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
