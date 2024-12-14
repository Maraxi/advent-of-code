from helpers import load, wrap


def get_robots(lines):
    robots = []
    for line in lines:
        l, r = line.split(" v=")
        pos = tuple(map(int, l[2:].split(",")))
        vel = tuple(map(int, r.split(",")))
        robots.append((pos, vel))
    return robots


def move(robot, steps, bound):
    r = (robot[0][0] + steps * robot[1][0]) % bound[0]
    c = (robot[0][1] + steps * robot[1][1]) % bound[1]
    return r, c


def solution1():
    cols = 101
    rows = 103
    steps = 100

    quads = [0, 0, 0, 0]
    for robot in robots:
        pos = move(robot, steps, (cols, rows))
        if pos[0] < cols // 2:
            if pos[1] < rows // 2:
                quads[0] += 1
            elif pos[1] > rows // 2:
                quads[1] += 1
        elif pos[0] > cols // 2:
            if pos[1] < rows // 2:
                quads[2] += 1
            elif pos[1] > rows // 2:
                quads[3] += 1
    return quads[0] * quads[1] * quads[2] * quads[3]


def solution2():
    cols = 101
    rows = 103

    for i in range(cols * rows):
        field = [["." for _ in range(cols)] for _ in range(rows)]
        for robot in robots:
            pos = move(robot, i, (cols, rows))
            field[pos[1]][pos[0]] = "#"

        neighbors = 0
        for r in range(1, rows - 1):
            row = field[r]
            for c in range(1, cols - 1):
                if row[c] == "#":
                    for d in [-1, 1]:
                        if row[c + d] == "#" or field[r + d][c] == "#":
                            neighbors += 1

        if neighbors > 300:
            for line in field:
                print("".join(line))
            return i


@wrap
def main():
    global robots
    robots = get_robots(lines)

    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
