from helpers import *
import pyperclip
import re


def solution1():
    total = 1
    times = data[0].split()[1:]
    dist = data[1].split()[1:]
    for t, d in zip(times, dist):
        t = int(t)
        d = int(d)
        i = 1
        while i * (t - i) <= d and i < t:
            i += 1
        total *= t - 2 * i + 1
    print(times, dist)
    return total


def solution2():
    total = 1
    times = data[0].replace(" ", "").split(":")[1]
    dist = data[1].replace(" ", "").split(":")[1]
    t = int(times)
    d = int(dist)
    lower = 1
    upper = t // 2
    while upper - lower > 1:
        mid = (upper + lower) // 2
        if mid * (t - mid) > d:
            upper = mid
        else:
            lower = mid
    print(upper, lower)
    total *= t - 2 * upper + 1
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
