from enum import Enum


def _load(file: str):
    with open(file, "r") as f:
        content = f.read().rstrip("\n")
        content = content.split("\n\n")
        if len(content) == 1:
            return content[0].split("\n")
        return [block.split("\n") for block in content]


def load(config):
    match config:
        case 1:
            return _load("sample1.txt")
        case 2:
            return _load("input.txt")
        case 3:
            data = _load("sample2.txt")
            if data[0]:
                return data
            return _load("sample1.txt")
        case 4:
            return _load("input.txt")


def transpose(lines):
    if isinstance(lines[0], str):
        return ["".join(line) for line in zip(*lines)]
    return list(zip(*lines))


def l1(left, right):  # Distance in L1 metric
    return abs(left[0] - right[0]) + abs(left[1] - right[1])


def l2sq(left, right):  # Squared euclidian distance
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


class Grid:
    def __init__(self, block, to_int=False):
        self.matrix = [[(int(e) if to_int else e) for e in row] for row in block]
        self.h = len(block)
        self.w = len(block[0])

    def __getitem__(self, key):
        return self.matrix[key[1]][key[0]]

    def __contains__(self, pos):
        return 0 <= pos[1] < self.h and 0 <= pos[0] < self.w

    def __str__(self):
        return "\n".join(["".join(map(str, row)) for row in self.matrix])

    def bound(self):  # position with maximal coords
        return self.w - 1, self.h - 1


class Direction(Enum):
    right = (1, 0)
    down = (0, 1)
    left = (-1, 0)
    up = (0, -1)

    def __add__(self, other):
        if isinstance(other, int):
            directions = list(Direction)
            return directions[(directions.index(self) + other) % 4]
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, int):
            return self + (-other)
        raise TypeError()

    def __bool__(self):  # Is the direction horizontal?
        return self in (Direction.right, Direction.left)

    def __getitem__(self, other):  # Go 1 or multiple steps in direction
        match other:
            case (x, y), n:
                return x + n * self.value[0], y + n * self.value[1]
            case (x, y):
                return x + self.value[0], y + self.value[1]
            case _:
                return TypeError()

    def __lt__(self, other):
        if isinstance(other, Direction):
            directions = list(Direction)
            return directions.index(self) < directions.index(other)
        return TypeError()
