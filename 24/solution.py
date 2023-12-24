from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime
import numpy as np
import sympy as sp


def intersection(l, r):
    (lx, ldx), (ly, ldy), (lz, ldz) = l
    (rx, rdx), (ry, rdy), (rz, rdz) = r
    A = np.array([[rdx, -ldx], [rdy, -ldy]])
    b = np.array([lx - rx, ly - ry])
    try:
        x = np.linalg.solve(A, b)
        pos = x[1] * np.array([ldx, ldy]) + np.array([lx, ly])
        if x[0] >= 0 and x[1] >= 0:
            return pos
    except np.linalg.LinAlgError:
        pass
    return False


def parse(block):
    hails = []
    for line in block:
        l, r = line.split(" @ ")
        lc = map(int, l.split(", "))
        rc = map(int, r.split(", "))
        hails.append(list(zip(lc, rc)))
    return hails


def solution1(full=False):
    if full:
        low, up = 200000000000000, 400000000000000
    else:
        low, up = 7, 27
    total = 0
    p = parse(data)
    for i, h1 in enumerate(p):
        for h2 in p[i + 1 :]:
            inter = intersection(h1, h2)
            if inter is not False:
                if all([low <= d <= up for d in inter]):
                    total += 1
    return total


def solution2():
    p = parse(data)
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    z = sp.Symbol("z")
    dx = sp.Symbol("dx")
    dy = sp.Symbol("dy")
    dz = sp.Symbol("dz")
    equations = []
    times = []
    for i, [(px, pdx), (py, pdy), (pz, pdz)] in enumerate(p[:3]):
        ti = sp.Symbol(f"t{i}")
        times.append(ti)
        equations.append(x + ti * dx - px - ti * pdx)
        equations.append(y + ti * dy - py - ti * pdy)
        equations.append(z + ti * dz - pz - ti * pdz)
    res = sp.solve_poly_system(equations, x, y, z, dx, dy, dz, *times)
    return int(sum(res[0][:3]))


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1(config == 2) if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
