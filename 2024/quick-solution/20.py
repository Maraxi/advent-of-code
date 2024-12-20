from helpers import load, wrap, Direction, Point, Grid, l1
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


def explore(grid, start, end):
    seen = {}
    Q = [(0, start)]
    while Q:
        val, pos = Q.pop(0)
        if pos in seen:
            continue
        seen[pos] = val

        if pos == end:
            break

        for dir in Direction:
            step = dir[pos]
            if grid[step] in "S.E":
                Q.append((val + 1, step))
    return seen


def solution1(grid):
    start = grid.find_all("S")[0]
    end = grid.find_all("E")[0]

    forward = explore(grid, start, end)
    backward = explore(grid, end, start)

    base_line = forward[end]
    cheats = defaultdict(int)

    for pos in forward:
        for dir in Direction:
            step = dir[pos]
            next_step = dir[step]
            if grid[step] == "#" and next_step in backward:
                length = forward[pos] + 2 + backward[next_step]
                if length + time_save <= base_line:
                    cheats[base_line - length] += 1

    total = 0
    for key, val in cheats.items():
        total += val

    return total


def solution2(grid, skip):
    start = grid.find_all("S")[0]
    end = grid.find_all("E")[0]

    forward = explore(grid, start, end)
    backward = explore(grid, end, start)

    base_line = forward[end]
    cheats = defaultdict(int)

    forward = {
        k: v for k, v in forward.items() if base_line - v - l1(k, end) >= time_save
    }
    backward = {
        k: v for k, v in backward.items() if base_line - v - l1(k, start) >= time_save
    }

    l = len(forward)
    for i, pos in enumerate(forward):
        if i % 1000 == 0:
            print(i, "/", l)
        for oth in backward:
            if l1(pos, oth) <= skip:
                length = forward[pos] + l1(pos, oth) + backward[oth]
                if length + time_save <= base_line:
                    cheats[base_line - length] += 1

    total = 0
    for key, val in cheats.items():
        total += val

    return total


@wrap
def main():
    grid = Grid(lines)
    yield solution1(grid)
    yield solution2(grid, skip)


if __name__ == "__main__":
    lines = load()
    time_save = 100
    skip = 20
    main()
