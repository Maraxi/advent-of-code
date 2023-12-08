from helpers import *
import pyperclip
import re


def instructions(start):
    while True:
        yield from start


def solution1():
    total = 0
    moves = instructions(data[0][0])
    maping = {}
    for row in data[1]:
        maping[row[:3]] = {"L": row[7:10], "R": row[12:15]}
    status = "AAA"
    while status != "ZZZ":
        total = total + 1
        status = maping[status][next(moves)]
        print(status)
    return total


def solution2():
    moves = instructions(data[0][0])
    maping = {}
    for row in data[1]:
        maping[row[:3]] = {"L": row[7:10], "R": row[12:15]}
    starts = [start for start in maping.keys() if start[2] == "A"]
    ends = [end for end in maping.keys() if end[2] == "Z"]
    print(starts, ends)
    all_steps = []
    # This worked by accident. The generator moves has not been reset.
    # Also we need to consider the behavior of the cyclic semigroups instead of
    # just the time until the first end.
    for start in starts:
        status = start
        steps = 0
        while status[2] != "Z":
            steps = steps + 1
            status = maping[status][next(moves)]
            print(status)
        all_steps.append(steps)
    import math

    return math.lcm(*all_steps)


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
