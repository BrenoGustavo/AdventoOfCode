import pathlib
from collections import Counter
from statistics import variance
from re import findall


def carregar_dados(file_path):
    with open(file_path) as file:
        return [linha.strip() for linha in file]


def positions_and_velocity(linhas):
    posicoes = []
    velocidades = []
    for linha in linhas:
        location, velocity = linha.split()
        x, y = map(int, location[2:].split(","))
        vx, vy = map(int, velocity[2:].split(","))
        posicoes.append((x, y))
        velocidades.append((vx, vy))
    return posicoes, velocidades


def simular_movimento(posicoes, velocidades, largura, altura, tempo):
    espaço = [[0] * largura for _ in range(altura)]
    for (x, y), (vx, vy) in zip(posicoes, velocidades):
        novo_x = (x + tempo * vx) % largura
        novo_y = (y + tempo * vy) % altura
        espaço[novo_y][novo_x] += 1
    return espaço


def calcular_safety_factor(espaço):
    altura = len(espaço)
    largura = len(espaço[0])
    meio_y = altura // 2
    meio_x = largura // 2

    q1 = sum(sum(row[:meio_x]) for row in espaço[:meio_y])
    q2 = sum(sum(row[meio_x + 1 :]) for row in espaço[:meio_y])
    q3 = sum(sum(row[:meio_x]) for row in espaço[meio_y + 1 :])
    q4 = sum(sum(row[meio_x + 1 :]) for row in espaço[meio_y + 1 :])

    return q1 * q2 * q3 * q4


def part_1(linhas):
    largura, altura, tempo = 101, 103, 100
    posicoes, velocidades = positions_and_velocity(linhas)
    espaço = simular_movimento(posicoes, velocidades, largura, altura, tempo)
    return calcular_safety_factor(espaço)


def part_2(linhas):
    largura, altura = 101, 103
    dados = [[int(n) for n in findall(r"-?\d+", linha)] for linha in linhas]

    def simular(t):
        return [
            ((x + t * vx) % largura, (y + t * vy) % altura) for x, y, vx, vy in dados
        ]

    melhor_tx, var_x = 0, float("inf")
    melhor_ty, var_y = 0, float("inf")

    for t in range(max(largura, altura)):
        xs, ys = zip(*simular(t))
        if (vx := variance(xs)) < var_x:
            melhor_tx, var_x = t, vx
        if (vy := variance(ys)) < var_y:
            melhor_ty, var_y = t, vy

    inverso_modular = pow(largura, -1, altura)
    return melhor_tx + ((inverso_modular * (melhor_ty - melhor_tx)) % altura) * largura


def main():
    day = 14
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    linhas = carregar_dados(puzzle_path)

    print("Part 1:", part_1(linhas))
    print("Part 2:", part_2(linhas))


if __name__ == "__main__":
    main()
