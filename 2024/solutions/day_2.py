import pathlib

def is_increasing(report):
    cur_lev = report[0]
    for i in range(len(report) - 1):
        if 3 >= (report[i + 1] - cur_lev) >= 1:
            cur_lev = report[i + 1]
        else:
            return False
    return True

def is_decreasing(report):
    cur_lev = report[-1]
    for i in range(len(report) - 1, 0, -1):
        if 3 >= (report[i - 1] - cur_lev) >= 1:
            cur_lev = report[i - 1]
        else:
            return False
    return True

def is_safe(report):
    return is_increasing(report) or is_decreasing(report)

def part_1(file_path):
    with open(file_path, 'r') as file:
        reports_list = [[int(numero) for numero in linha.split()] for linha in file.readlines()]

    safe_counts = 0
    for report in reports_list:
        if is_safe(report):
            safe_counts += 1

    return safe_counts

def is_safe_part2(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def reactor_dumpener(report):
    if is_safe_part2(report):  # Already safe
        return True

    for i in range(len(report)):
        cut_report = report[:i] + report[i + 1:]
        if is_safe_part2(cut_report):
            return True

    return False

def part_2(file_path):
    with open(file_path, 'r') as file:
        listed_reports = [[int(numero) for numero in linha.split()] for linha in file.readlines()]

    contagem = 0
    for report in listed_reports:
        if reactor_dumpener(report):
            contagem += 1

    return contagem

def main():
    day = 2
    puzzle_path = pathlib.Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"

    print("Part 1:", part_1(puzzle_path))
    print("Part 2:", part_2(puzzle_path))

if __name__ == "__main__":
    main()