from helpers import load, wrap, Direction, Point, Grid, transpose
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


def solution1():
    locks = []
    keys = []
    for block in blocks:
        bitting = [line.count("#") for line in transpose(block)]
        if block[0][0] == "#":
            locks.append(bitting)
        else:
            keys.append(bitting)

    total = 0
    for lock in locks:
        for key in keys:
            comb = [l + k for l, k in zip(lock, key)]
            if all([val <= 7 for val in comb]):
                total += 1

    return total


@wrap
def main():
    yield solution1()
    yield 0


if __name__ == "__main__":
    blocks = load()
    main()
