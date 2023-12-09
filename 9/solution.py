from helpers import *
import pyperclip
import re


def diffs(line, end=True):
    if all((a == 0 for a in line)):
        return 0
    else:
        update = [b - a for a, b in zip(line, line[1:])]
        diff = diffs(update, end)
        if end:
            return update[-1] + diff
        else:
            return update[0] - diff


def solution1():
    total = 0
    for line in data:
        line = list(map(int, line.split()))
        total += diffs(line) + line[-1]
    return total


def solution2():
    total = 0
    for line in data:
        line = list(map(int, line.split()))
        total += -diffs(line, False) + line[0]
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
