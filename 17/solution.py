from helpers import *
import pyperclip
import re
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def search(block, stepmin, stepmax):
    seen = set()
    queue = [
        (block.w + block.h, 0, (0, 0), Direction.right),
        (block.w + block.h, 0, (0, 0), Direction.down),
    ]
    while queue:
        heu, cost, pos, last = heappop(queue)
        if pos[0] == block.w - 1 and pos[1] == block.h - 1:
            return cost
        id = pos, bool(last)
        if id in seen:
            continue
        seen.add(id)

        for turn in [-1, 1]:
            new_cost = cost
            direc = last + turn
            for steps in range(1, stepmax + 1):
                new_pos = direc[pos, steps]
                if new_pos not in block:
                    break
                new_cost += block[new_pos]
                if steps < stepmin:
                    continue
                heappush(
                    queue,
                    (new_cost + l1(block.bound(), new_pos), new_cost, new_pos, direc),
                )


def solution1():
    g = Grid(data, True)
    return search(g, 1, 3)


def solution2():
    g = Grid(data, True)
    return search(g, 4, 10)


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
