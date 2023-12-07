from helpers import *
import pyperclip
import re
from collections import Counter

cards = "AKQJT98765432"
cards2 = "AKQT98765432J"
# rating: 5 of a kind  / 4 of a kind / full house / 3 of a kind
# 2 pair / pair / nothing


def rank_hand(hand, rating=cards):
    c = Counter(hand)
    if "J" in c and rating == cards2:
        jokers = c["J"]
        c["J"] = 0
        common = c.most_common()
        common[0] = (common[0][0], common[0][1] + jokers)
    else:
        common = c.most_common()
    if common[0][1] == 5:
        rank = 1
    elif common[0][1] == 4:
        rank = 2
    elif common[0][1] == 3:
        if common[1][1] == 2:
            rank = 3
        else:
            rank = 4
    elif common[0][1] == 2:
        if common[1][1] == 2:
            rank = 5
        else:
            rank = 6
    else:
        rank = 7
    for letter in hand:
        rank = rank * 100 + rating.index(letter)
    return rank


def solution1():
    rows = [row.split() for row in data]
    rows = [(-rank_hand(a), int(b)) for a, b in rows]
    rows.sort()
    rows = [r[1] * i for r, i in zip(rows, range(1, len(rows) + 1))]
    return sum(rows)


def solution2():
    rows = [row.split() for row in data]
    rows = [(-rank_hand(a, cards2), int(b)) for a, b in rows]
    rows.sort()
    rows = [r[1] * i for r, i in zip(rows, range(1, len(rows) + 1))]
    return sum(rows)


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
