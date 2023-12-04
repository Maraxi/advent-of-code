from helpers import *
import pyperclip
import re
from collections import defaultdict


def solution1():
    total = 0
    for card in data:
        overview = card.split(": ")
        hands = overview[1].split(" | ")
        win = re.finditer(r"\d+", hands[0])
        win = {int(k.group()) for k in win}
        hand = re.finditer(r"\d+", hands[1])
        hand = {int(k.group()) for k in hand}
        intersec = win & hand
        if len(intersec) > 0:
            points = 1 << (len(intersec) - 1)
            total += points
    return total


def solution2():
    total = 0
    amounts = defaultdict(lambda: 1)
    for i, card in enumerate(data):
        total += amounts[i]
        overview = card.split(": ")
        hands = overview[1].split(" | ")
        win = re.finditer(r"\d+", hands[0])
        win = {int(k.group()) for k in win}
        hand = re.finditer(r"\d+", hands[1])
        hand = {int(k.group()) for k in hand}
        intersec = win & hand
        for k in range(1, len(intersec) + 1):
            amounts[i + k] += amounts[i]
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
