from helpers import load, wrap


def get_combo_op(operand, a, b, c):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            raise ValueError()
        case _:
            raise ValueError()


def run_program(a, b, c):
    pointer = 0
    out = []
    while pointer < len(program):
        inst, operand = program[pointer : pointer + 2]
        combo_op = get_combo_op(operand, a, b, c)
        match inst:
            case 0:
                a = a >> combo_op
            case 1:
                b ^= operand
            case 2:
                b = combo_op % 8
            case 3:
                if a != 0:
                    pointer = operand
                    continue
            case 4:
                b ^= c
            case 5:
                out.append(combo_op % 8)
            case 6:
                b = a >> combo_op
            case 7:
                c = a >> combo_op
            case _:
                raise TypeError()
        pointer += 2
    return out


def solution1():
    return ",".join(map(str, run_program(*registers)))


def solution2():
    queue = [(len(program), 0)]
    while queue:
        offset, val = queue.pop()
        if offset == 0:
            return val
        target = program[offset - 1 :]
        for digit in reversed(range(8)):
            new_val = (val << 3) + digit
            if run_program(new_val, 0, 0) == target:
                queue.append((offset - 1, new_val))


@wrap
def main():
    global registers, program
    registers, program = load()
    registers = [int(reg.split(" ")[-1]) for reg in registers]
    program = [int(p) for p in program.split(" ")[-1].split(",")]

    yield solution1()
    yield solution2()


if __name__ == "__main__":
    main()
