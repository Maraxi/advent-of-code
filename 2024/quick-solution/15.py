from helpers import load, wrap, Direction, Point, Grid


def push(grid: Grid, position: Point, direction: Direction):
    if direction in [Direction.left, Direction.right]:
        current = position
        while grid[current] in "O@[]":
            current = direction[current]
        if grid[current] == "#":
            return position
        else:
            reverse = direction + 2
            l, r = current, reverse[current]
            while l != position:
                grid[l] = grid[r]
                l, r = r, reverse[r]
            grid[position] = "."
            return direction[position]
    else:
        front = [position]
        switches = []
        while front:
            next_front = set()
            for f in front:
                n = direction[f]
                sym = grid[n]
                if sym == "#":
                    return position
                elif sym == ".":
                    switches.append((f, n))
                    continue
                elif sym == "O":
                    switches.append((f, n))
                    next_front.add(n)
                elif sym == "[":
                    if grid[Direction.right[n]] == "#":
                        return position
                    switches.append((f, n))
                    next_front.add(n)
                    next_front.add(Direction.right[n])
                elif sym == "]":
                    if grid[Direction.left[n]] == "#":
                        return position
                    switches.append((f, n))
                    next_front.add(n)
                    next_front.add(Direction.left[n])
                else:
                    print(f, n, sym)
                    raise ValueError
            front = list(next_front)
        for l, r in reversed(switches):
            grid[l], grid[r] = grid[r], grid[l]
        return direction[position]


def solution1():
    g = Grid(grid)
    current = g.find_all("@")[0]

    for i in instructions:
        current = push(g, current, i)

    loc = g.find_all("O")
    return sum([l[0] + l[1] * 100 for l in loc])


def solution2():
    wide = (
        "\n".join(grid)
        .replace("#", "##")
        .replace(".", "..")
        .replace("O", "[]")
        .replace("@", "@.")
        .split("\n")
    )

    g = Grid(wide)
    current = g.find_all("@")[0]

    for i in instructions[:]:
        current = push(g, current, i)

    loc = g.find_all("[")
    return sum([l[0] + l[1] * 100 for l in loc])


@wrap
def main():
    global instructions, mapper
    instructions = "".join(instructions)
    mapper = {
        "^": Direction.up,
        "<": Direction.left,
        "v": Direction.down,
        ">": Direction.right,
    }
    instructions = [mapper[char] for char in instructions.strip()]

    yield solution1()
    yield solution2()


if __name__ == "__main__":
    grid, instructions = load()
    main()
