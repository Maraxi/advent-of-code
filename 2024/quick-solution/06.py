from helpers import load, wrap, Direction, Grid


def solution1(grid):
    dir = Direction.up
    current = grid.find_all("^")[0]

    seen = set()

    for _ in range(8000):
        seen.add(current)

        step = dir[current]
        if step not in grid:
            break
        if grid[step] == "#":
            dir += 1
            continue
        current = step
    else:
        return None

    # print(grid)
    return seen


def solution2(grid, path):
    total = 0
    for i, point in enumerate(path):
        if i % 100 == 0:
            print(i, "/", len(path))
        if grid[point] == "^":
            continue

        grid[point] = "#"
        sol = solution1(grid)
        if sol is None:
            total += 1
        grid[point] = "."
    return total


@wrap
def main():
    grid = Grid(load())
    path = solution1(grid)
    yield len(path)
    yield solution2(grid, path)


if __name__ == "__main__":
    main()
