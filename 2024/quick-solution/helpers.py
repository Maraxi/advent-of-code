from enum import Enum
import sys
import pyperclip
from datetime import datetime


def load():
    day = sys.argv[0].removesuffix(".py")
    file_name = f"../{day}.input" if len(sys.argv) == 1 else sys.argv[1]

    with open(file_name) as file:
        blocks = file.read().strip().split("\n\n")
        if len(blocks) == 1:
            block = blocks[0].split("\n")
            return block[0] if len(block) == 1 else block
        blocks = [block.split("\n") for block in blocks]
        return [block[0] if len(block) == 1 else block for block in blocks]


def wrap(func):
    def inner(*args, **kwargs):
        start = datetime.now()

        generator = func(*args, **kwargs)

        result1 = next(generator)
        print(datetime.now() - start, "-", result1)

        result2 = next(generator)
        print(datetime.now() - start, "-", result2)

        clip = result1 if result2 == 0 else result2
        pyperclip.copy(clip)
        print(f"Copied {clip} to clipboard")

    return inner


def transpose(lines):
    if isinstance(lines[0], str):
        return ["".join(line) for line in zip(*lines)]
    return list(zip(*lines))


def l1(left, right):  # Distance in L1 metric
    return abs(left[0] - right[0]) + abs(left[1] - right[1])


def l2sq(left, right):  # Squared euclidian distance
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


def get_area(corners):  # shoelace formula
    pos = [x * y for (x, _), (_, y) in zip(corners, corners[1:] + corners[:1])]
    neg = [x * y for (x, _), (_, y) in zip(corners[1:] + corners[:1], corners)]
    return abs(sum(pos) - sum(neg)) // 2


def get_corners(points):
    # points are spaces in the grid
    # the point is a corner "offset by -1/2, -1/2"
    offset = {
        Direction.right: lambda x, y: Point((x, y)),
        Direction.down: lambda x, y: Point((x - 1, y)),
        Direction.left: lambda x, y: Point((x - 1, y - 1)),
        Direction.up: lambda x, y: Point((x, y - 1)),
    }
    point = min(points)
    dir = Direction.right

    result = [point]

    point = dir[point]
    while point != result[0]:
        outer_point = (dir - 1)[point]
        if offset[dir](*outer_point) in points:
            result.append(point)
            dir -= 1
        elif offset[dir](*point) not in points:
            result.append(point)
            dir += 1
        point = dir[point]
    return result


def is_inside_polygon(corners, point):
    # corners as returned by get_corners
    # edges between corners are alternating between horizontal and vertical,
    #   starting with horizontal between [0] and [1]
    # use ray casting algorithm with ray towards -y
    count = 0
    edges = (
        (l, r) for (l, y), (r, _) in zip(corners[::2], corners[1::2]) if y > point[1]
    )
    for l, r in edges:
        if (l <= point[0] < r) or (l >= point[0] > r):
            count += 1
    return count % 2 == 1


class Point(tuple):
    """pairs of (col, row)"""

    def __eq__(self, o):
        return o[0] == self[0] and o[1] == self[1]

    def __lt__(self, x):
        if self[1] < x[1]:
            return True
        elif self[1] == x[1] and self[0] < x[0]:
            return True
        return False

    def __hash__(self):
        return hash((self[0], self[1]))

    def __add__(self, other):
        return Point((self[0] + other[0], self[1] + other[1]))

    def __sub__(self, other):
        return Point((self[0] - other[0], self[1] - other[1]))

    def __neg__(self):
        return Point((-self.x, -self.y))

    def within(self, width, height):
        return 0 <= self[0] < width and 0 <= self[1] < height


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
                return Point((x + n * self.value[0], y + n * self.value[1]))
            case (x, y):
                return Point((x + self.value[0], y + self.value[1]))
            case _:
                return TypeError()

    def __lt__(self, other):
        if isinstance(other, Direction):
            directions = list(Direction)
            return directions.index(self) < directions.index(other)
        return TypeError()


class Grid:
    def __init__(self, block, to_int=False):
        self.matrix = [[(int(e) if to_int else e) for e in row] for row in block]
        self.h = len(block)
        self.w = len(block[0])

    def __setitem__(self, key, val):
        """key given like Point as (col, row)"""
        self.matrix[key[1]][key[0]] = val

    def __getitem__(self, key):
        """key given like Point as (col, row)"""
        return self.matrix[key[1]][key[0]]

    def __contains__(self, pos):
        return 0 <= pos[1] < self.h and 0 <= pos[0] < self.w

    def __str__(self):
        return "\n".join(["".join(map(str, row)) for row in self.matrix])

    def bound(self):  # position with maximal coords
        return self.w - 1, self.h - 1

    def find_all(self, char):
        return [
            Point((x, y))
            for y, line in enumerate(self.matrix)
            for x, entry in enumerate(line)
            if entry == char
        ]
