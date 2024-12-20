from helpers import load, wrap, Direction, Grid, l1


def find_path(grid, start, end):
    path = [start]
    prev = start

    for dir in Direction:
        current = dir[prev]
        if grid[current] == ".":
            path.append(current)
            break

    while current != end:
        for dir in Direction:
            step = dir[current]
            if grid[step] != "#" and step != prev:
                path.append(step)
                prev, current = current, step
                break
    return path


def solution(path):
    small_cheats = 0
    cheats = 0
    for i, pos in enumerate(path):
        j = i + TIME_SAVE + 2
        while j < len(path):
            other_pos = path[j]
            dist = l1(pos, other_pos)

            buffer = j - (i + dist + TIME_SAVE)
            if buffer < 0:
                j -= buffer // 2
                continue

            if dist > LARGE_SKIP:
                j += dist - LARGE_SKIP
                continue

            if dist == 2:
                small_cheats += 1
                lower_check = 4
            else:
                lower_check = dist - 2
            upper_check = LARGE_SKIP + 1 - dist
            remaining = len(path) - j

            till_next_check = max(1, min(lower_check, upper_check, remaining))
            cheats += till_next_check
            j += till_next_check
    return small_cheats, cheats


@wrap
def main():
    grid = Grid(load())
    start = grid.find_all("S")[0]
    end = grid.find_all("E")[0]
    path = find_path(grid, start, end)

    res1, res2 = solution(path)
    yield res1
    yield res2


if __name__ == "__main__":
    TIME_SAVE = 100
    LARGE_SKIP = 20
    main()
