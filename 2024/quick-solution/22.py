from helpers import load, wrap, Direction, Point, Grid
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


modulo = 16777216


def solution1():
    total = 0
    for line in lines:
        sec = int(line)
        for _ in range(2000):
            sec = (sec ^ (sec * 64)) % modulo
            sec = ((sec // 32) ^ sec) % modulo
            sec = ((sec * 2048) ^ sec) % modulo
        total += sec
    return total


def solution2():
    sequences = []
    nums = []
    for line in lines:
        seq = []
        num = []
        sec = int(line)
        current = sec % 10
        for _ in range(2000):
            sec = (sec ^ (sec * 64)) % modulo
            sec = ((sec // 32) ^ sec) % modulo
            sec = ((sec * 2048) ^ sec) % modulo

            update = sec % 10
            seq.append(update - current)
            num.append(update)
            current = update

        sequences.append(seq)
        nums.append(num)

    total_mappings = Counter()
    for seq, num in zip(sequences, nums):
        mapping = {}
        for i in range(len(seq) - 3):
            current = tuple(seq[i: i + 4])
            if current not in mapping:
                mapping[current] = num[i + 3]

        for key, val in mapping.items():
            total_mappings[key] += val

    return total_mappings.most_common(1)[0][1]


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
