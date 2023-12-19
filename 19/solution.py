from helpers import *
import pyperclip
import re
from operator import mul
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime
from ast import literal_eval


def get_rules(block):
    rules = {}
    for line in block:
        name = line.split("{")[0]
        rule = []
        regex = r"(\w+)([<>])(\d+):(\w+)"
        matches = re.finditer(regex, line)
        for m in matches:
            rule.append((m.group(1), m.group(2), int(m.group(3)), m.group(4)))
        a = re.search(r",(\w+)}", line)
        rule.append(a.group(1))
        rules[name] = rule
    return rules


def get_parts(block):
    for part in block:
        s = re.sub(r"(\w+)=", '"\g<1>":', part)
        yield literal_eval(s)


def solution1():
    total = 0
    rules = get_rules(data[0])
    for part in get_parts(data[1]):
        state = "in"
        while state not in "AR":
            rule = rules[state]
            for entry in rule[:-1]:
                if entry[1] == "<":
                    if part[entry[0]] < entry[2]:
                        state = entry[3]
                        break
                else:
                    if part[entry[0]] > entry[2]:
                        state = entry[3]
                        break
            else:
                state = rule[-1]
        if state == "A":
            total += sum(part.values())
    return total


def combinations(part):
    return reduce(mul, map(lambda x: x[1] - x[0], part.values()))


def solution2():
    total = 0
    rules = get_rules(data[0])
    queue = [("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
    while queue:
        state, part = queue.pop()
        if any(map(lambda x: x[0] == x[1], part.values())):
            continue
        if state == "A":
            total += combinations(part)
            continue
        if state == "R":
            continue
        rule = rules[state]
        for entry in rule[:-1]:
            n, cond, val, nexts = entry
            if cond == "<":
                if part[n][0] < val:
                    new_part = part.copy()
                    new_val = min(val, new_part[n][1])
                    new_part[n] = (new_part[n][0], new_val)
                    part[n] = (new_val, part[n][1])
                    queue.append((nexts, new_part))
            if cond == ">":
                if part[n][1] > val + 1:
                    new_part = part.copy()
                    new_val = max(val + 1, new_part[n][0])
                    new_part[n] = (new_val, new_part[n][1])
                    part[n] = (part[n][0], new_val)
                    queue.append((nexts, new_part))
        queue.append((rule[-1], part))
    return total


if __name__ == "__main__":
    config = 4
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
