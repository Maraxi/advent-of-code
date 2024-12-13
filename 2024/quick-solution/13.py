from helpers import load, wrap


def get_numbers(block):
    a = list(map(int, block[0][11:].split(", Y")))
    b = list(map(int, block[1][11:].split(", Y")))
    r = list(map(int, block[2][9:].split(", Y=")))

    return a, b, r


def solve_equation(a, b, r):
    det = a[0] * b[1] - a[1] * b[0]
    if det == 0:
        ib = r[0] // b[0]
        if b[0] * ib == r[0] and b[1] * ib == r[1]:
            return ib
        return 0

    ia = (b[1] * r[0] - b[0] * r[1]) // det
    ib = (-a[1] * r[0] + a[0] * r[1]) // det

    if ia * a[0] + ib * b[0] == r[0] and ia * a[1] + ib * b[1] == r[1]:
        return 3 * ia + ib
    return 0


def solution1():
    total = 0
    for a, b, r in numbers:
        total += solve_equation(a, b, r)
    return total


def solution2():
    total = 0
    for a, b, r in numbers:
        rx, ry = r[0] + 10000000000000, r[1] + 10000000000000
        total += solve_equation(a, b, (rx, ry))
    return total


@wrap
def main():
    global numbers
    numbers = []
    for block in blocks:
        numbers.append(get_numbers(block))

    yield solution1()
    yield solution2()


if __name__ == "__main__":
    blocks = load()
    main()
