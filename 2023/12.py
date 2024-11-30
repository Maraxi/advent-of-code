from helpers import *
import pyperclip
import re
import math


def can_fit(chunk, blocks):
    # print(chunk, blocks)
    if chunk.find("#") == -1:
        l = len(chunk) - sum(blocks) - len(blocks) + 1
        if l < 0:
            return 0
        return math.comb(l + len(blocks), l)
    if len(blocks) == 1:
        b = blocks[0]
        if len(chunk) < b:
            return 0
        if chunk.count("#") > b:
            return 0
        left = chunk.find("#")
        right = list(reversed(chunk)).index("#")
        right_bound = len(chunk) - right
        remain = b - (right_bound - left)
        if remain < 0:
            return 0
        l = min(remain, left)
        r = min(remain, len(chunk) - right_bound)
        return l + r - remain + 1
    shortest = sum(blocks) + len(blocks) - 1
    if len(chunk) < shortest:
        return 0
    if chunk.count("#") > sum(blocks):
        return 0
    if chunk.count("?") == 0:
        return 1 if len(blocks) == 1 and blocks[0] == len(chunk) else 0
    possiblilities = 0
    first_hash = chunk.find("#")
    if first_hash == -1:
        first_hash = len(chunk)
    for start in range(0, min(first_hash + 1, len(chunk) - blocks[0])):
        if chunk[start + blocks[0]] == "#":
            continue
        if start + blocks[0] > len(chunk):
            break
        possiblilities += can_fit(chunk[start + blocks[0] + 1 :], blocks[1:])
    return possiblilities


def search(chunks, nums):
    queue = [(1, chunks, nums)]
    total = 0
    while queue:
        item = queue.pop()
        # print("Using ", item)
        if len(item[1]) == 0:
            if len(item[2]) == 0:
                # print("  - finish")
                total += item[0]
            continue
        for i in range(0, len(item[2]) + 1):
            res = can_fit(item[1][0], item[2][:i])
            # print(" ", item[1][0], item[2][:i], res)
            if res > 0:
                queue.append((item[0] * res, item[1][1:], item[2][i:]))
                # print("    added ", queue[-1])
    return total


def solution1():
    total = 0
    for line in data:
        left, right = line.split()
        nums = list(map(int, right.split(",")))
        left = left.strip(".")
        chunks = re.split(r"\.+", left)
        total += search(chunks, nums)
    return total


def solution2():
    total = 0
    for line in data:
        left, right = line.split()
        nums = list(map(int, right.split(",")))
        left = "?".join(5 * [left]).strip(".")
        chunks = re.split(r"\.+", left)
        nums = 5 * nums
        total += search(chunks, nums)
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
