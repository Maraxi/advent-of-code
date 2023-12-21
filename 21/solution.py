from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def walk(grid, steps, start):
    seen = [start]
    next_queue = [start]
    spaces = [1, 0]
    for i in range(1, steps + 1):
        queue = next_queue
        next_queue = []
        for q in queue:
            for d in list(Direction):
                pos = d[q]
                if pos not in seen and pos in grid and grid[pos] != "#":
                    next_queue.append(pos)
                    seen.append(pos)
                    spaces[i % 2] += 1
    print(steps, start, spaces)
    return spaces


def solution1():
    g = Grid(data)
    for y, row in enumerate(data):
        if "S" in row:
            start = (row.index("S"), y)
            break
    return walk(g, 64, start)[0]


def floyd_warshall(grid):
    # takes too long
    positions = [
        (x, y) for x in range(grid.w) for y in range(grid.h) if grid[x, y] != "#"
    ]
    matrix = [
        [
            0 if first == second else 1 if l1(first, second) == 1 else 10000
            for first in positions
        ]
        for second in positions
    ]
    l = len(positions)
    for a in range(l):
        for i in range(l):
            for j in range(l):
                matrix[i][j] = min(matrix[i][j], matrix[i][a] + matrix[a][j])
    return positions, matrix


def solution2():
    g = Grid(data)
    assert g.w == g.h

    start = (g.w // 2, g.h // 2)
    assert g[start] == "S"

    steps = 26501365
    divi, remain = divmod(steps, g.w)

    # full covered boards
    full = walk(g, 150, start)
    rings = divi - 1
    inner_even = 1 + 4 * (rings // 2) * (rings // 2 + 1)
    inner_odd = 4 * ((rings + 1) // 2) ** 2
    inner = inner_even * full[steps % 2] + inner_odd * full[(steps + 1) % 2]

    # boards diagonal from start, consists of partially (small - p)
    # and mostly covered fields (big - b)
    #     s.s
    #    sb.bs
    #   sb...bs
    #   ...S...
    #   sb...bs
    #    sb.bs
    #     s.s
    corners = [(0, 0), (g.w - 1, 0), (0, g.h - 1), (g.w - 1, g.h - 1)]
    small = sum(walk(g, remain - 1, c)[(divi + 1 + steps) % 2] for c in corners)
    big = sum(walk(g, remain - 1 + g.w, c)[(divi + steps) % 2] for c in corners)
    outer = divi * small + (divi - 1) * big

    # tips in cardinal directions
    starts = [(0, start[1]), (g.w - 1, start[1]), (start[0], 0), (start[0], g.h - 1)]
    points = sum(walk(g, remain + g.w // 2, s)[(divi + 1 + steps) % 2] for s in starts)
    return inner + outer + points


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
