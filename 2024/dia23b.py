import os
conexoes = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputdia23.txt')


with open(conexoes, 'r') as arquivo:

    conexoes_list = [linha.strip() for linha in arquivo.readlines()]



from collections import defaultdict

def parse_input(connections):
    graph = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
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

def find_largest_clique(graph):
    largest_clique = max(bron_kerbosch(graph), key=len)
    return largest_clique


graph = parse_input(conexoes_list)
# # Parse input to graph
# graph = parse_input(connections)

# Find the largest clique
largest_clique = find_largest_clique(graph)

# Generate the password
password = ','.join(sorted(largest_clique))

print(f"The largest clique is: {largest_clique}")
print(f"The password to the LAN party is: {password}")
