from helpers import *
import math
import pyperclip
from datetime import datetime


def solve_quadratic(p, q):
    # x**2 - px - q <= 0
    if p % 2 == 0:
        return -1 + 2 * math.ceil((p * p / 4 - q) ** 0.5)
    else:
        return 2 * round((p * p / 4 - q) ** 0.5)


def solution1():
    times = map(int, data[0].split()[1:])
    dist = map(int, data[1].split()[1:])
    return math.prod(map(solve_quadratic, times, dist))


def solution2():
    time = int(data[0].replace(" ", "").split(":")[1])
    dist = int(data[1].replace(" ", "").split(":")[1])
    return solve_quadratic(time, dist)


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    mid = datetime.now()
    result = solution1() if config < 3 else solution2()
    end = datetime.now()
    print(result, mid - start, end - mid, end - start)
    pyperclip.copy(result)
