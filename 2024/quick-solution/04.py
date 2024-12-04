from helpers import load, wrap
import re


def solution1():
    total = 0
    for line in lines:
        matches = re.findall("XMAS", line)
        total += len(matches)
        matches = re.findall("SAMX", line)
        total += len(matches)
    transposed = ["".join(line) for line in zip(*lines)]
    for line in transposed:
        matches = re.findall("XMAS", line)
        total += len(matches)
        matches = re.findall("SAMX", line)
        total += len(matches)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "X":
                if i + 3 < len(lines):
                    if j + 3 < len(lines):
                        if (
                            lines[i + 1][j + 1] == "M"
                            and lines[i + 2][j + 2] == "A"
                            and lines[i + 3][j + 3] == "S"
                        ):
                            total += 1
                    if j - 3 >= 0:
                        if (
                            lines[i + 1][j - 1] == "M"
                            and lines[i + 2][j - 2] == "A"
                            and lines[i + 3][j - 3] == "S"
                        ):
                            total += 1
                if i - 3 >= 0:
                    if j + 3 < len(lines):
                        if (
                            lines[i - 1][j + 1] == "M"
                            and lines[i - 2][j + 2] == "A"
                            and lines[i - 3][j + 3] == "S"
                        ):
                            total += 1
                    if j - 3 >= 0:
                        if (
                            lines[i - 1][j - 1] == "M"
                            and lines[i - 2][j - 2] == "A"
                            and lines[i - 3][j - 3] == "S"
                        ):
                            total += 1

    return total


def solution2():
    total = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            if lines[i][j] == "A":
                if (lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S") or (
                    lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M"
                ):
                    if (lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S") or (
                        lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M"
                    ):
                        total += 1
    return total


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
