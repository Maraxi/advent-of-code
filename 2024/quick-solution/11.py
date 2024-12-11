from helpers import load, wrap
from collections import Counter


def rule(stone):
    if stone == 0:
        return [1]
    elif stone >= 10 and len(str(stone)) % 2 == 0:
        string = str(stone)
        length = len(string) // 2
        return [int(string[:length]), int(string[length:])]
    else:
        return [2024 * stone]


def solution1():
    line = [int(e) for e in lines.split(" ")]
    for _ in range(25):
        line = [k for stone in line for k in rule(stone)]
    total = len(line)
    return total


def solution2():
    line = [int(e) for e in lines.split(" ")]
    counter = Counter()
    for entry in line:
        counter[entry] += 1
    for i in range(75):
        # print(i)
        newcounter = Counter()
        for stone, val in counter.items():
            for new_stone in rule(stone):
                newcounter[new_stone] += val
        counter = newcounter
    return sum(counter.values())


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
