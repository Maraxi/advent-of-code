from helpers import *
import pyperclip
import re


def solution1():
    total = 0
    extracols = []
    extrarows = []
    for col in range(len(data)):
        if all((row[col] == "." for row in data)):
            extracols.append(col)
    for i, row in enumerate(data):
        if row.find("#") == -1:
            extrarows.append(i)
    print(extrarows, extracols)
    galax = []
    for i, row in enumerate(data):
        matches = re.finditer(r"#", row)
        for match in matches:
            galax.append([i, match.start()])
    print(galax)
    for col in reversed(extracols):
        for gal in galax:
            if gal[1] > col:
                gal[1] += 1
    for row in reversed(extrarows):
        for gal in galax:
            if gal[0] > row:
                gal[0] += 1
    print(galax)
    for i, gal in enumerate(galax):
        for other in galax[i + 1 :]:
            total += abs(gal[0] - other[0]) + abs(gal[1] - other[1])
    return total


def solution2():
    total = 0
    extracols = []
    extrarows = []
    for col in range(len(data)):
        if all((row[col] == "." for row in data)):
            extracols.append(col)
    for i, row in enumerate(data):
        if row.find("#") == -1:
            extrarows.append(i)
    print(extrarows, extracols)
    galax = []
    for i, row in enumerate(data):
        matches = re.finditer(r"#", row)
        for match in matches:
            galax.append([i, match.start()])
    print(galax)
    for col in reversed(extracols):
        for gal in galax:
            if gal[1] > col:
                gal[1] += 999999
    for row in reversed(extrarows):
        for gal in galax:
            if gal[0] > row:
                gal[0] += 999999
    print(galax)
    for i, gal in enumerate(galax):
        for other in galax[i + 1 :]:
            total += abs(gal[0] - other[0]) + abs(gal[1] - other[1])
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
