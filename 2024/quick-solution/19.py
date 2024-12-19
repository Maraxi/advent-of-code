from helpers import load, wrap, Direction, Point, Grid
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


def solution1():
    total = 0
    for target in targets:
        Q = [target]
        while Q:
            current = Q.pop()
            if current == "":
                total += 1
                break
            for avai in available:
                if len(current) >= len(avai) and current[: len(avai)] == avai:
                    Q.append(current[len(avai):])

    return total


def solution2():
    total = 0
    for target in targets:
        possible = [0 for _ in range(len(target) + 1)]
        possible[0] = 1

        for j in range(1, len(target) + 1):
            for avai in available:
                la = len(avai)
                if la > j:
                    continue
                if target[j - la: j] == avai:
                    possible[j] += possible[j - la]
        total += possible[-1]

    return total


@wrap
def main():
    global available, targets
    available, targets = load()
    available = available.split(", ")

    yield solution1()
    yield solution2()


if __name__ == "__main__":
    main()
