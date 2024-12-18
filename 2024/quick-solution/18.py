from helpers import load, wrap, Direction, Point, Grid


def area(size, blocks):
    content = [["." for _ in range(size)] for _ in range(size)]
    g = Grid(content)
    for b in blocks:
        x, y = list(map(int, b.split(",")))
        g[x, y] = "#"
    return g


def solution1(size, lines):
    grid = area(size + 1, lines)

    seen = set()
    Q = [(0, Point([0, 0]))]

    while Q:
        val, p = Q.pop(0)
        if p in seen:
            continue
        seen.add(p)
        if p[0] == size and p[1] == size:
            return val

        for dir in Direction:
            step = dir[p]
            if step in grid and grid[step] == ".":
                Q.append((val + 1, step))


def solution2(size, low):
    high = len(lines)

    while low + 1 < high:
        med = (low + high) // 2
        val = solution1(size, lines[:med])

        if val is None:
            high = med
        else:
            low = med

    return lines[low]


@wrap
def main():
    size = 70
    line_no = 1024
    yield solution1(size, lines[:line_no])
    yield solution2(size, line_no)


if __name__ == "__main__":
    lines = load()
    main()
