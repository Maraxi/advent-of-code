from helpers import load, wrap, Direction, Grid
from collections import defaultdict


def solution1():
    trails = grid.find_all("0")

    total = 0
    for trail in trails:
        current = defaultdict(int)
        current[trail] += 1
        for number in range(1, 10):
            update = defaultdict(int)
            for key, count in current.items():
                for dir in Direction:
                    step = dir[key]
                    if step in grid:
                        if grid[step] == str(number):
                            update[step] += count
            current = update
        total += len(current.keys())

    return total


def solution2():
    current = defaultdict(int)
    for pos in grid.find_all("0"):
        current[pos] += 1

    for number in range(1, 10):
        update = defaultdict(int)
        for key, count in current.items():
            for dir in Direction:
                step = dir[key]
                if step in grid:
                    if grid[step] == str(number):
                        update[step] += count
        current = update

    return sum(current.values())


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    grid = Grid(load())
    main()
