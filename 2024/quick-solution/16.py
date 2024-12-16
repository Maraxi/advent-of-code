from helpers import load, wrap, Direction, Grid
from heapq import heappush, heappop


def solution1():
    grid = Grid(lines)
    start = grid.find_all("S")[0]
    end = grid.find_all("E")[0]

    current = (0, start, Direction.right)

    seen = set()
    Q = [current]

    while Q:
        score, p, d = heappop(Q)
        if p == end:
            return score
        if (p, d) in seen:
            continue
        seen.add((p, d))

        for i in range(1, 500):
            new_pos = d[p, i]
            if grid[new_pos] == "#":
                break
            heappush(Q, (score + i, new_pos, d))
        for i in [+1, -1]:
            new_d = d + i
            new_pos = new_d[p]
            if grid[new_pos] == ".":
                heappush(Q, (score + 1001, new_pos, new_d))


def solution2():
    grid = Grid(lines)
    start = grid.find_all("S")[0]
    end = grid.find_all("E")[0]

    current = (0, start, Direction.right, None, (start,))
    turned = (1000, start, Direction.up, None, (start,))

    seen = {}
    Q = [current, turned]
    best_score = 1 << 128
    best_paths = {}

    i = 0
    while Q:
        score, p, d, prev, history = heappop(Q)
        if score > best_score:
            break

        if (p, d) in seen:
            if seen.get((p, d)) == score:
                s = best_paths[(p, d)]
                for o in best_paths.get(prev, []):
                    s.add(o)
                for h in history:
                    s.add(h)
            continue
        else:
            seen[(p, d)] = score
            s = set()
            for o in best_paths.get(prev, []):
                s.add(o)
            for h in history:
                s.add(h)
            best_paths[(p, d)] = s

        if p == end:
            best_score = score
            continue

        new_history = []
        for i in range(1, 500):
            new_pos = d[p, i]
            if grid[new_pos] == "#":
                break
            new_history.append(new_pos)

            if new_pos == end:
                heappush(Q, (score + i, new_pos, d, (p, d), new_history))
                break
            for j in [+1, -1]:
                new_d = d + j
                new_p = new_d[new_pos]
                if grid[new_p] == ".":
                    heappush(
                        Q,
                        (
                            score + i + 1000,
                            new_pos,
                            new_d,
                            (p, d),
                            [*new_history],
                        ),
                    )
    total = set()
    for dir in Direction:
        for x in best_paths.get((end, dir), []):
            total.add(x)
            grid[x] = "O"
    print(grid)
    return len(total)


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
