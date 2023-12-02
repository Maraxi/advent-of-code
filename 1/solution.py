from helpers import *
import re


letters = "abcdefghijklmnopqrstuvwxyz"


def solution1():
    s = 0
    for e in data:
        f = e.strip(letters)
        g = f[0] + f[-1]
        s = s + int(g)
    print(s)


def solution2():
    s = 0
    translate = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for e in data:
        print("##")
        print(e)

        words = "|".join(translate.keys())

        start = re.search(rf"{words}|\d", e)
        number = start.group(0)
        if len(number) > 1:
            number = translate[number]
        end = re.search(rf".*({words}|\d)", e)
        num2 = end.group(1)
        if len(num2) > 1:
            num2 = translate[num2]
        s = s + int(number + num2)
    print(s)


if __name__ == "__main__":
    config = 4
    data = load(config)
    solution1() if config < 3 else solution2()
