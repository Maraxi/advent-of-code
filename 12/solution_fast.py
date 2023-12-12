from helpers import *
import pyperclip
import re


def search(chunk, nums, spare, ci, ni, mem):
    if ci < len(chunk) and chunk[ci] == ".":
        ci += 1
        spare -= 1
    if ci >= len(chunk) or ni == len(nums) or spare < 0:
        return 1 if "#" not in chunk[ci:] and ni == len(nums) else 0
    if (ci, ni) in mem:
        return mem[(ci, ni)]
    total = 0
    rest = chunk[ci:]
    if chunk[ci] in "?#":
        if (
            ci + nums[ni] < len(chunk)
            and chunk[ci + nums[ni]] != "#"
            and "." not in chunk[ci : ci + nums[ni]]
        ):
            total += search(chunk, nums, spare, ci + nums[ni] + 1, ni + 1, mem)
    if chunk[ci] == "?" and spare > 0:
        total += search(chunk, nums, spare - 1, ci + 1, ni, mem)
    mem[(ci, ni)] = total
    return total


def solution1():
    total = 0
    for line in data:
        left, right = line.split()
        nums = list(map(int, right.split(",")))
        left = re.subn(r"\.+", ".", left + ".")[0]
        total += search(left, nums, len(left) - sum(nums) - len(nums), 0, 0, {})
    return total


def solution2():
    total = 0
    for line in data:
        left, right = line.split()
        nums = list(map(int, right.split(",")))
        left = "?".join(5 * [left]).strip(".")
        left = re.subn(r"\.+", ".", left + ".")[0]
        nums = 5 * nums
        total += search(left, nums, len(left) - sum(nums) - len(nums), 0, 0, {})
    return total


from datetime import datetime

if __name__ == "__main__":
    config = 4
    s = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - s)
    pyperclip.copy(result)
