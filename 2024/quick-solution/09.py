from helpers import load, wrap
from copy import deepcopy


def solution1():
    disk = []
    id = 0
    space = False
    for char in lines:
        if space:
            disk.extend(["."] * int(char))
            space = False
        else:
            disk.extend([id] * int(char))
            space = True
            id += 1
    left = 0
    right = len(disk) - 1
    while left < right:
        if disk[left] != ".":
            left += 1
            continue
        if disk[right] == ".":
            right -= 1
            continue
        disk[left] = disk[right]
        disk[right] = "."
        left += 1
        right -= 1
    total = 0
    for i, val in enumerate(disk):
        if val != ".":
            total += i * val
    return total


def solution2():
    blocks = []
    id = 0
    space = False
    for char in lines:
        if space:
            blocks.append([".", int(char)])
            space = False
        else:
            blocks.append([id, int(char)])
            space = True
            id += 1
    right = len(blocks) - 1
    while right >= 0:
        if blocks[right][0] == ".":
            right -= 1
            continue
        else:
            length = blocks[right][1]
            for i, block in enumerate(blocks[:right]):
                if block[0] == "." and block[1] >= length:
                    if block[1] == length:
                        block[0] = blocks[right][0]
                        blocks[right][0] = "."
                        right -= 1
                    else:
                        block[1] -= length
                        blocks.insert(i, deepcopy(blocks[right]))
                        blocks[right + 1][0] = "."
                    break
            else:
                right -= 1
    total = 0
    i = 0
    for block in blocks:
        if block[0] == ".":
            i += block[1]
        else:
            for _ in range(block[1]):
                total += i * block[0]
                i += 1

    return total


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
