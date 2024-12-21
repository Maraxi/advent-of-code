from helpers import load, wrap, Point, Grid
from functools import cache
from collections import defaultdict


def find_with_forbid(start, end, forbid):
    # take preferred path if that does not cross forbidden point
    if start[0] >= end[0]:
        horz = "<" * (start[0] - end[0])
    else:
        horz = ">" * (end[0] - start[0])
    if start[1] >= end[1]:
        vert = "^" * (start[1] - end[1])
    else:
        vert = "v" * (end[1] - start[1])

    if start[0] >= end[0]:
        # prefer left -> up over up -> left
        # prefer left -> down over down -> left
        intermed = (end[0], start[1])
        if intermed == forbid:
            return vert + horz
        else:
            return horz + vert
    else:
        # prefer down -> right over right -> down
        # order for top right does not matter
        intermed = (start[0], end[1])
        if intermed == forbid:
            return horz + vert
        else:
            return vert + horz


def get_numeric_presses(code):
    current = Point(2, 3)

    sequences = defaultdict(int)

    for char in code:
        end = numeric_grid.find_all(char)[0]
        seq = find_with_forbid(current, end, (0, 3))
        sequences[seq + "A"] += 1
        current = end
    return sequences


@cache
def get_directional_presses(code):
    current = Point(2, 0)

    sequence = []

    for char in code:
        end = direction_grid.find(char)
        seq = find_with_forbid(current, end, (0, 0))
        sequence.append(seq + "A")
        current = end
    return sequence


def solution(directional_bots):
    total = 0
    for line in lines:
        ddict = get_numeric_presses(line)
        for i in range(directional_bots):
            next_ddict = defaultdict(int)
            for key, val in ddict.items():
                for seq in get_directional_presses(key):
                    next_ddict[seq] += val
            ddict = next_ddict

        factor = int(line[:3])
        total_len = sum(len(key) * val for key, val in ddict.items())
        total += factor * total_len
    return total


@wrap
def main():
    global numeric_grid, direction_grid
    matrix = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
    numeric_grid = Grid(matrix)
    matrix = [["#", "^", "A"], ["<", "v", ">"]]
    direction_grid = Grid(matrix)

    yield solution(2)
    yield solution(25)


if __name__ == "__main__":
    lines = load()
    main()
