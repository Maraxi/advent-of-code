from helpers import load, wrap, Direction, Point, Grid, get_corners, l1


def get_components(grid):
    g = Grid(grid)
    # print(g)
    seen = [[False for x in range(g.w)] for y in range(g.h)]

    components = []
    for y in range(g.h):
        for x in range(g.w):
            if seen[y][x] is False:
                comp = [Point((x, y))]
                letter = g[comp[0]]
                seen[y][x] = True
                queue = [(x, y)]
                while len(queue) > 0:
                    e = queue.pop()
                    for dir in Direction:
                        step = dir[e]
                        if (
                            step in g
                            and g[step] == letter
                            and seen[step[1]][step[0]] is False
                        ):
                            seen[step[1]][step[0]] = True
                            comp.append(step)
                            queue.append(step)
                components.append(comp)
    return components


def fence(corners, task):
    if task == 0:
        return sum(l1(l, r) for l, r in zip(corners, corners[1:] + corners[:1]))
    return len(corners)


def solution(task):
    total = 0
    for comp in components:
        corners = get_corners(comp)
        all_x = [c[0] for c in corners]
        all_y = [c[1] for c in corners]

        min_x = min(all_x)
        min_y = min(all_y)

        x_bound = range(max(all_x) - min_x + 2)
        y_bound = range(max(all_y) - min_y + 2)
        bounding_box = [["." for x in x_bound] for y in y_bound]
        for p in comp:
            bounding_box[p[1] - min_y + 1][p[0] - min_x + 1] = "#"
        inner_components = get_components(bounding_box)

        circum = fence(corners, task) + sum(
            fence(get_corners(c), task) for c in inner_components[2:]
        )
        area = len(comp)
        total += area * circum

    return total


@wrap
def main():
    global components
    components = get_components(lines)

    yield solution(0)
    yield solution(1)


if __name__ == "__main__":
    lines = load()
    main()
