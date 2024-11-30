from helpers import *
import pyperclip
import re


def myhash(data):
    total = 0
    for char in data:
        total = ((total + ord(char)) * 17) % 256
    return total


def solution1():
    total = 0
    for w in data[0].split(","):
        total += myhash(w)
    return total


def solution2():
    total = 0
    boxes = [[] for _ in range(256)]
    for w in data[0].split(","):
        if w[-1] == "-":
            label = w[:-1]
            h = myhash(label)
            for i, b in enumerate(boxes[h]):
                if b[0] == label:
                    boxes[h].pop(i)
                    break
        if w[-2] == "=":
            label = w[:-2]
            h = myhash(label)
            for i, b in enumerate(boxes[h]):
                if b[0] == label:
                    b[1] = int(w[-1])
                    break
            else:
                boxes[h].append([label, int(w[-1])])
    x = [list(zip(b, range(1, len(b) + 1))) for b in boxes]
    y = [(i + 1) * sum([a[1] * b for a, b in c]) for i, c in enumerate(x)]
    return sum(y)


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
