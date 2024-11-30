from helpers import *
import pyperclip
import re


def energise(start):
    queue = [start]
    mem = set()
    seen = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        x = curr[0]
        y = curr[1]
        if curr in mem or not (0 <= x < len(data[0]) and 0 <= y < len(data)):
            continue
        mem.add(curr)
        seen.add((x, y))
        char = data[y][x]
        match curr[2]:
            case 1:
                if char in ".-":
                    queue.append((x + 1, y, 1))
                if char in r"\|":
                    queue.append((x, y + 1, 2))
                if char in r"/|":
                    queue.append((x, y - 1, 4))
            case 2:
                if char in ".|":
                    queue.append((x, y + 1, 2))
                if char in r"\-":
                    queue.append((x + 1, y, 1))
                if char in r"/-":
                    queue.append((x - 1, y, 3))
            case 3:
                if char in ".-":
                    queue.append((x - 1, y, 3))
                if char in r"\|":
                    queue.append((x, y - 1, 4))
                if char in r"/|":
                    queue.append((x, y + 1, 2))
            case 4:
                if char in ".|":
                    queue.append((x, y - 1, 4))
                if char in r"\-":
                    queue.append((x - 1, y, 3))
                if char in r"/-":
                    queue.append((x + 1, y, 1))
    return len(seen)


def solution1():
    return energise((0, 0, 1))


def solution2():
    best = 0
    for y in range(len(data)):
        best = max(best, energise((0, y, 1)))
        best = max(best, energise((len(data[0]) - 1, y, 3)))
    for x in range(len(data[0])):
        best = max(best, energise((x, 0, 2)))
        best = max(best, energise((x, len(data) - 1, 4)))
    return best


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
