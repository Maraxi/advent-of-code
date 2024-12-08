from helpers import load, wrap, Point


def solution1():
    signals = {}
    for y, line in enumerate(lines):
        for x, s in enumerate(line):
            if s != ".":
                if s not in signals:
                    signals[s] = [Point((x, y))]
                else:
                    signals[s].append(Point((x, y)))

    antennas = set()
    width = len(lines[0])
    height = len(lines)
    for val in signals.values():
        for i, first in enumerate(val):
            for second in val[i + 1 :]:
                dist = second - first
                p = first - dist
                if p.within(width, height):
                    antennas.add(p)
                p = second + dist
                if p.within(width, height):
                    antennas.add(p)
    return len(antennas)


def solution2():
    signals = {}
    for y, line in enumerate(lines):
        for x, s in enumerate(line):
            if s != ".":
                if s not in signals:
                    signals[s] = [Point((x, y))]
                else:
                    signals[s].append(Point((x, y)))

    antennas = set()
    width = len(lines[0])
    height = len(lines)
    for val in signals.values():
        for i, first in enumerate(val):
            for second in val[i + 1 :]:
                dist = second - first
                p = first
                while p.within(width, height):
                    antennas.add(p)
                    p -= dist
                p = second
                while p.within(width, height):
                    antennas.add(p)
                    p += dist
    return len(set(antennas))


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
