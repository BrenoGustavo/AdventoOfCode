from pathlib import Path

day = 23
# input_path = Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
input_path = Path(__file__).parent / "inputday23.txt"
data = open(input_path).read()


def treat_line(line):

    parts = line.split(" ")
    if len(parts) == 3:
        instruction, register, jump = parts[0], parts[1][0], parts[2]
        return instruction, register, jump
    else:
        parts.append(None)
        return tuple(parts)


def solve(is_part_2=False):

    registeres = dict()
    if is_part_2:
        registeres["a"] = 1

    ins_and_regs = data.splitlines()
    location = 0
    while 0 <= location < len(ins_and_regs):
        line = ins_and_regs[location]

        parts = treat_line(line)
        # print(parts)
        instruction = parts[0]

        if parts[2]:
            # print("a")
            instruction, register, jump_str = parts
            # print(instruction, register, jump_str)

            if register not in registeres:
                registeres[register] = 0
                # print(register)

            if instruction == "jio":
                if registeres[register] == 1:
                    location += int(jump_str[1:])
                    # print(location)

                    continue
                else:
                    location += 1
                    continue

            if instruction == "jie":
                if registeres[register] % 2 == 0:
                    location += int(jump_str[1:])
                else:
                    location += 1
                    continue

        elif instruction == "jmp":

            instruction, jump, _ = parts
            if jump.startswith("+"):
                location += int(jump[1:])

            elif jump.startswith("-"):
                location -= int(jump[1:])

            continue

        instruction, register, _ = parts

        if register not in registeres:
            registeres[register] = 0

        if instruction == "hlf":
            # register = parts[1]
            registeres[register] = registeres[register] / 2
            location += 1
            continue

        elif instruction == "tpl":
            # register = parts[1]
            registeres[register] = registeres[register] * 3
            location += 1
            continue

        elif instruction == "inc":
            # register = parts[1]
            registeres[register] = registeres[register] + 1
            location += 1
            continue

    print(registeres.items())


def part1():
    solve()


def part2():
    solve(is_part_2=True)


part2()
