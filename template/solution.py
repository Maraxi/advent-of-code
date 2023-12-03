from helpers import *
import pyperclip
import re


def solution1():
    pass


def solution2():
    pass


if __name__ == "__main__":
    config = 1
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
