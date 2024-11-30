from helpers import *
import pyperclip
import re


def elf_map(origin, nums):
    shuffle = [list(map(int, stuff.split(" "))) for stuff in nums]
    result = []
    for current in origin:
        for shuff in shuffle:
            if current in range(shuff[1], shuff[1] + shuff[2]):
                result.append(current + shuff[0] - shuff[1])
                break
        else:
            result.append(current)
    return result


def solution1():
    status = [int(a) for a in data[0][0].split(" ")[1:]]
    for line in data[1:]:
        status = elf_map(status, line[1:])
    return min(status)


def elf_map_ranges(origin, nums):
    shuffle = [list(map(int, stuff.split(" "))) for stuff in nums]
    queue = list(origin)
    result = []
    while len(queue) > 0:
        current = queue.pop()
        cstart = current[0]
        cend = current[0] + current[1]
        for shuff in shuffle:
            sstart = shuff[1]
            send = shuff[1] + shuff[2]
            if cend <= sstart or cstart >= send:
                continue
            elif cstart < sstart:
                if cend <= send:
                    result.append([shuff[0], cend - sstart])
                    queue.append([cstart, sstart - cstart])
                    break
                if cend > send:
                    result.append([shuff[0], shuff[2]])
                    queue.append([cstart, sstart - cstart])
                    queue.append([send, cend - send])
                    break
            else:  # cstart >= sstart, cstart < send
                if cend <= send:
                    result.append([cstart + shuff[0] - shuff[1], current[1]])
                    break
                else:
                    result.append([cstart + shuff[0] - shuff[1], send - cstart])
                    queue.append([send, cend - send])
                    break
        else:
            result.append(current)
    return result


def solution2():
    status = [int(a) for a in data[0][0].split(" ")[1:]]
    status = [(a, b) for a, b in zip(status[::2], status[1::2])]

    for line in data[1:]:
        status = elf_map_ranges(status, line[1:])
    return min(status)[0]


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
