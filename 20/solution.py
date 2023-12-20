from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def parse(block):
    modules = {}
    for line in block:
        l, r = line.split(" -> ")
        if l == "broadcaster":
            name = "broadcaster"
            type = "b"
            state = None
        else:
            name = l[1:]
            type = l[0]
            if type == "%":
                state = [0]
            if type == "&":
                state = {}
        targets = r.split(", ")
        modules[name] = (type, targets, state)
    for name, module in modules.items():
        for target in module[1]:
            if target in modules and modules[target][0] == "&":
                modules[target][2][name] = 0
    return modules


def press(modules, watchlist=None, i=-1):
    pulses = [0, 0]
    rx = 0
    queue = [(0, "button", "broadcaster")]
    while queue:
        pulse, source, target = queue.pop(0)
        if (
            watchlist is not None
            and source in watchlist
            and pulse == 1
            and watchlist[source] is None
        ):
            watchlist[source] = i
        if target == "qr":
            print(pulse, source, target)
        pulses[pulse] += 1
        if target not in modules:
            continue
        type, targets, state = modules[target]
        if type == "b":
            for t in targets:
                queue.append((0, target, t))
        if type == "%":
            if pulse == 0:
                state[0] = 1 - state[0]
                for t in targets:
                    queue.append((state[0], target, t))
        if type == "&":
            state[source] = pulse
            if all([v == 1 for v in state.values()]):
                for t in targets:
                    queue.append((0, target, t))
            else:
                for t in targets:
                    queue.append((1, target, t))
    return pulses


def solution1():
    total = 0
    mods = parse(data)
    hi = 0
    lo = 0
    for _ in range(5):
        for _ in range(1000):
            [l, h], _ = press(mods)
            lo += l
            hi += h
        pass
    return hi * lo


def solution2():
    total = 0
    mods = parse(data)
    target = [n for n in mods.values() if "rx" in n[1]][0]
    watchlist = {key: None for key in target[2].keys()}

    i = 0
    while None in watchlist.values():
        i += 1
        press(mods, watchlist, i)
    return math.lcm(*watchlist.values())


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
