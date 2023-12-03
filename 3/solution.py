from helpers import *
import pyperclip
import re


def solution1():
    total = 0
    sym = []
    for i, line in enumerate(data):
        symbos = re.finditer(r"[^.\d]", line)
        for s in symbos:
            sym.append((i, s.start()))
    for i, line in enumerate(data):
        finds = re.finditer(r"\d+", line)
        for f in finds:
            if any(
                (
                    i - 1 <= s[0] <= i + 1 and f.start() - 1 <= s[1] <= f.end()
                    for s in sym
                )
            ):
                total += int(f.group())
    return total


def solution2():
    total = 0
    nums = []
    for i, line in enumerate(data):
        num = re.finditer(r"\d+", line)
        for n in num:
            nums.append((i, n.start(), n.end(), n.group()))
    for i, line in enumerate(data):
        finds = re.finditer(r"\*", line)
        for f in finds:
            filtered = [
                n[3]
                for n in nums
                if i - 1 <= n[0] <= i + 1 and n[1] - 1 <= f.start() <= n[2]
            ]
            if len(filtered) == 2:
                total += int(filtered[0]) * int(filtered[1])
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
