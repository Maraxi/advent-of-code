from helpers import *
import pyperclip
import re



def solution1():
    total = 0
    block = transpose(data)
    for line in block:
        parts = line.split("#")
        shift = ["O" * part.count("O") + "." * part.count(".") for part in parts]
        nline = "#".join(shift)
        counts = zip(nline, range(len(nline), 0, -1))
        total += sum([i for c, i in counts if c == "O"])
    return total


def shift(block, direc):
    if direc in "ns":
        block = transpose(block)
    result = []
    for line in block:
        parts = line.split("#")
        if direc in "nw":
            shift = ["O" * part.count("O") + "." * part.count(".") for part in parts]
        else:
            shift = ["." * part.count(".") + "O" * part.count("O") for part in parts]
        nline = "#".join(shift)
        result.append(nline)
    if direc in "ns":
        result = transpose(result)
    return tuple(result)


def cycle(block):
    b = shift(block, "n")
    c = shift(b, "w")
    d = shift(c, "s")
    return shift(d, "e")


def score(block):
    total = 0
    for line in transpose(block):
        counts = zip(line, range(len(line), 0, -1))
        total += sum([i for c, i in counts if c == "O"])
    return total

def solution2():
    total = 0
    m = {}
    current = data
    for i in range(1, 1000000001):
        current = cycle(current)
        if current in m:
            break
        m[current] = i
    remaining = (1000000000 - i) % (i - m[current])
    for _ in range(remaining):
        current = cycle(current)
    return score(current)


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
