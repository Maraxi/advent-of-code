from helpers import *

config = [
    False,
    #True,
    1
]


def solution1():
    pass


def solution2():
    pass


if __name__ == "__main__":
    data = load("input.txt") if config[0] else load("sample.txt")
    if config[1] == 1:
        solution1()
    else:
        solution2()
