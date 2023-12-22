from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def bricks(data):
    b = []
    for line in data:
        s, e = line.split("~")
        s = map(int, s.split(","))
        e = map(int, e.split(","))
        b.append(list(map(sorted, zip(*[s, e]))))
    return b


def distance(l, r):
    for direc in range(2):
        dmin = max(l[direc][0], r[direc][0])
        dmax = min(l[direc][1], r[direc][1])
        if dmax < dmin:
            return None
    if l[2][1] < r[2][0]:
        return r[2][0] - l[2][1]
    return r[2][1] - l[2][0]


def covering(bricks):
    above = [{} for _ in range(len(bricks))]
    below = [{} for _ in range(len(bricks))]
    for i, b in enumerate(bricks):
        for j, p in enumerate(bricks[i + 1 :]):
            d = distance(b, p)
            if d is not None:
                if d > 0:
                    lower = i
                    upper = i + 1 + j
                    dist = d
                elif d < 0:
                    lower = i + 1 + j
                    upper = i
                    dist = -d
                else:
                    print("intersection", b, p)
                    return
                above[lower][upper] = dist
                below[upper][lower] = dist
    return above, below


def falling(above, below, bricks):
    change = True
    while change:
        change = False
        for i, b in enumerate(bricks):
            bel = below[i]
            if bel:
                dist = min(bel.values()) - 1
            else:
                dist = b[2][0] - 1
            if dist < 0:
                print("panic", b, bel)
            if dist > 0:
                change = True
                b[2][0] -= dist
                b[2][1] -= dist
                for x in bel:
                    bel[x] -= dist
                    above[x][i] -= dist
                for x in above[i]:
                    above[i][x] += dist
                    below[x][i] += dist


def solution1():
    b = bricks(data)
    above, below = covering(b)
    falling(above, below, b)
    total = 0
    supports = [len([i for i in b.values() if i == 1]) for b in below]
    for i in range(len(b)):
        can_remove = True
        for a in above[i]:
            if above[i][a] == 1 and supports[a] == 1:
                can_remove = False
                break
        if can_remove:
            total += 1
    return total


def solution2():
    b = bricks(data)
    above, below = covering(b)
    falling(above, below, b)
    total = 0
    supports = [{i for i, v in b.items() if v == 1} for b in below]
    for i, brick in enumerate(b):
        if brick[2][0] == 1:
            supports[i].add(-1)
    for i in range(len(b)):
        chain = {i}
        change = True
        while change:
            change = False
            for j in range(len(b)):
                if j not in chain and supports[j] <= chain:
                    chain.add(j)
                    change = True
        total += len(chain) - 1
    return total


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
