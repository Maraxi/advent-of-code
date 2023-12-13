from helpers import *
import pyperclip
import re


m = {}


def hor(data):
    total = 0
    for i, block in enumerate(data):
        if i not in m:
            m[i] = []
        rev = list(reversed(block))
        if len(rev) % 2 == 0:
            if all((a == b for a, b in zip(block, rev))):
                total += 100 * (len(rev) // 2)
                m[i].append(len(rev) // 2)
            for offset in range(0, len(block), 2):
                if all((a == b for a, b in zip(block[offset:], rev))):
                    total += 100 * (len(block) + offset) // 2
                    m[i].append(len(block) + offset // 2)
                if all((a == b for a, b in zip(block, rev[offset:]))):
                    total += 100 * (len(block) - offset) // 2
                    m[i].append(len(block) - offset // 2)
        else:
            for offset in range(1, len(block), 2):
                if all((a == b for a, b in zip(block[offset:], rev))):
                    total += 100 * (len(block) + offset) // 2
                    m[i].append(len(block) + offset // 2)
                if all((a == b for a, b in zip(block, rev[offset:]))):
                    total += 100 * (len(block) - offset) // 2
                    m[i].append(len(block) - offset // 2)
    return total


def solution1():
    total = 0
    total += hor(data)
    data_t = []
    for block in data:
        b_t = []
        for i in range(len(block[0])):
            b_t.append("".join([c[i] for c in block]))
        data_t.append(b_t)
    total += hor(data_t) // 100
    print(m)
    return total


def hor2(data):
    total = 0
    for i, block in enumerate(data):
        if i not in m:
            m[i] = []
        for row in range(1, len(block)):
            errors = 0
            lower = row - 1
            upper = row
            while lower >= 0 and upper < len(block) and errors <= 1:
                errors += sum([a != b for a, b in zip(block[lower], block[upper])])
                lower -= 1
                upper += 1
            if errors == 1:
                m[i].append(row)
                total += row

    return total


def solution2():
    total = 0
    total += hor2(data) * 100
    data_t = []
    for block in data:
        b_t = []
        for i in range(len(block[0])):
            b_t.append("".join([c[i] for c in block]))
        data_t.append(b_t)
    total += hor2(data_t)
    print(m)
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
