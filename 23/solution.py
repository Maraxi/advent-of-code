from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def is_intersection(grid, pos):
    if grid[pos] == "#":
        return False
    return (
        sum([1 for d in list(Direction) if d[pos] in grid and grid[d[pos]] != "#"]) > 2
    )


def dag(grid, start, end, hard=False):
    intersections = [
        (x, y)
        for x in range(grid.w)
        for y in range(grid.h)
        if is_intersection(grid, (x, y))
    ]
    intersections.insert(0, start)
    intersections.append(end)
    transitions = [{} for _ in range(len(intersections))]
    for i, inter in enumerate(intersections):
        seen = [inter]
        queue = [(d[inter], 1) for d in list(Direction)]
        while queue:
            pos, n = queue.pop(0)
            if pos not in grid or grid[pos] == "#" or pos in seen:
                continue
            if pos in intersections:
                transitions[i][intersections.index(pos)] = n
                continue
            seen.append(pos)
            if hard:
                grid[pos] = "."
            match grid[pos]:
                case ">":
                    queue.append((Direction.right[pos], n + 1))
                case "<":
                    queue.append((Direction.left[pos], n + 1))
                case "^":
                    queue.append((Direction.up[pos], n + 1))
                case "v":
                    queue.append((Direction.down[pos], n + 1))
                case ".":
                    queue.append((Direction.right[pos], n + 1))
                    queue.append((Direction.down[pos], n + 1))
                    queue.append((Direction.up[pos], n + 1))
                    queue.append((Direction.left[pos], n + 1))
                case _:
                    raise ValueError(f"Invalid {grid[pos]}")
    return intersections, transitions


def best_route(transistions):
    queue = [(0, -0, 0, 1)]
    best = 0
    most = [{} for _ in range(len(transistions))]
    i = 0
    while queue:
        i += 1
        if i % 100000 == 0:
            qn, qs, qp, qi = queue[0]
            print(i, len(queue), qn, -qs, f"{qp:2}", f"{bin(qi):>38}")
        n, neg_steps, pos, locations = heappop(queue)
        steps = -neg_steps
        if most[pos].get(locations, -1) >= steps:
            continue
        most[pos][locations] = steps
        if pos == len(transistions) - 1:
            best = max(best, steps)
        for next_pos, update in transistions[pos].items():
            i_next = 1 << next_pos
            new_locations = locations | i_next
            if new_locations == locations:
                continue
            new_steps = steps + update
            heappush(queue, (n + 1, -new_steps, next_pos, new_locations))
    return best


def path(grid, start, end):
    seen = []
    queue = [(start, 0)]
    while queue:
        (pos, n) = queue.pop(0)
        if pos == end:
            return n
        if pos not in grid or grid[pos] == "#" or pos in seen:
            continue
        seen.append(pos)
        match grid[pos]:
            case ">":
                queue.append((Direction.right[pos], n + 1))
            case "<":
                queue.append((Direction.left[pos], n + 1))
            case "^":
                queue.append((Direction.up[pos], n + 1))
            case "v":
                queue.append((Direction.down[pos], n + 1))
            case ".":
                queue.append((Direction.right[pos], n + 1))
                queue.append((Direction.down[pos], n + 1))
                queue.append((Direction.up[pos], n + 1))
                queue.append((Direction.left[pos], n + 1))
            case _:
                raise ValueError(f"Invalid {grid[pos]}")


def solution1():
    g = Grid(data)
    s = (data[0].index("."), 0)
    e = (data[-1].index("."), g.h - 1)
    inter, trans = dag(g, s, e)
    length = best_route(trans)
    return length


def solution2():
    g = Grid(data)
    s = (data[0].index("."), 0)
    e = (data[-1].index("."), g.h - 1)
    inter, trans = dag(g, s, e, True)
    length = best_route(trans)
    return length


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)

# first solution for part 2:
#   locations as sets
#     6590 0:08:37.952818
#   locations as bitmask
#     6590 0:02:22.868062
