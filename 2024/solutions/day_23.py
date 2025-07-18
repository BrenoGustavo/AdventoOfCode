"""
Analisa um mapa de conexões de computadores em uma rede.

Parte 1: Encontra todas as trincas de computadores em que todos estão conectados entre si,
e conta quantas dessas trincas possuem ao menos um computador cujo nome começa com 't'.

Parte 2: Encontra o maior grupo de computadores onde todos estão conectados entre si (clique máximo)
e gera a senha da LAN party ordenando alfabeticamente os nomes e unindo-os com vírgulas.
"""

import pathlib
from collections import defaultdict


def parse_input(file_path):
    with open(file_path, "r") as file:
        connections = [line.strip().split("-") for line in file.readlines()]
    return connections


def part_1(file_path):
    connections = parse_input(file_path)

    triples = set()

    for a, b in connections:
        for c1, c2 in connections:
            if {a, b} == {c1, c2}:
                continue
            if a in (c1, c2):
                mid = c2 if c1 == a else c1
                for d1, d2 in connections:
                    if mid in (d1, d2) and b in (d1, d2):
                        triple = tuple(sorted([a, mid, b]))
                        triples.add(triple)
            elif b in (c1, c2):
                mid = c2 if c1 == b else c1
                for d1, d2 in connections:
                    if mid in (d1, d2) and a in (d1, d2):
                        triple = tuple(sorted([a, mid, b]))
                        triples.add(triple)

    # Filtrar trios que têm ao menos um computador com nome começando com "t"
    count = sum(1 for triple in triples if any(pc.startswith("t") for pc in triple))
    return count


def build_graph(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph


def bron_kerbosch(graph, r=set(), p=None, x=set()):
    if p is None:
        p = set(graph.keys())
    if not p and not x:
        yield r
    for v in list(p):
        yield from bron_kerbosch(
            graph,
            r | {v},
            p & graph[v],
            x & graph[v],
        )
        p.remove(v)
        x.add(v)


def part_2(file_path):
    raw_connections = parse_input(file_path)
    graph = build_graph(raw_connections)

    largest_clique = max(bron_kerbosch(graph), key=len)
    password = ",".join(sorted(largest_clique))
    return password


def main():
    day = 23
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))


if __name__ == "__main__":
    main()
