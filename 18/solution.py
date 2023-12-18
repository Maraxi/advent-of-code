from helpers import *
import pyperclip
import re
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def dig(lines):
    coords = [(0, 0)]
    last = (0, 0)
    for line in lines:
        last = line[0][last, line[1]]
        coords.append(last)

    segments = list(zip(coords, coords[1:] + [coords[0]]))
    area = abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in segments)) // 2
    perimeter = sum([l1(*seg) for seg in segments]) // 2
    return area + perimeter + 1


def solution1():
    lines = [l.split(" ") for l in data]
    lines = [
        (
            {
                "R": Direction.right,
                "U": Direction.up,
                "L": Direction.left,
                "D": Direction.down,
            }[line[0]],
            int(line[1]),
        )
        for line in lines
    ]
    return dig(lines)


def solution2():
    lines = [l.split(" ")[2] for l in data]
    l = list(Direction)
    lines = [(l[int(w[-2])], int(w[2:-2], 16)) for w in lines]
    return dig(lines)


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
