from helpers import *
import pyperclip
import re


def first_parse():
    visited = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    location = [list(a) for a in data]
    total = 0
    start = [line.find("S") for line in data]
    start = start.index(max(start)), max(start)
    queue = []
    visited[start[0]][start[1]] = True
    if data[start[0]][start[1] - 1] in "-LF" and start[1] > 0:
        queue.append((start[0], start[1] - 1, 1))
    if data[start[0]][start[1] + 1] in "-7J":
        queue.append((start[0], start[1] + 1, 1))
    if data[start[0] + 1][start[1]] in "|LJ":
        queue.append((start[0] + 1, start[1], 1))
    if data[start[0] - 1][start[1]] in "|7F" and start[0] > 0:
        queue.append((start[0] - 1, start[1], 1))
    while len(queue) > 0:
        row, col, step = queue.pop(0)
        if visited[row][col]:
            continue
        visited[row][col] = True
        total = max(total, step)
        char = data[row][col]
        location[row][col] = str(step % 10)
        if row < len(data) - 1 and char in ["7", "|", "F"]:
            queue.append((row + 1, col, step + 1))
        if row > 0 and char in ["J", "|", "L"]:
            queue.append((row - 1, col, step + 1))
        if col > 0 and char in ["7", "-", "J"]:
            queue.append((row, col - 1, step + 1))
        if col < len(data[0]) - 1 and char in ["L", "-", "F"]:
            queue.append((row, col + 1, step + 1))
    return total, visited


def solution1():
    return first_parse()[0]


def solution2():
    pipe = first_parse()[1]
    inside = [[True for _ in data[0]] for _ in data]
    corners = [[False for _ in range(len(data[0]) + 1)] for _ in range(len(data) + 1)]
    queue = (
        [[0, a] for a in range(len(corners[0]))]
        + [[len(corners) - 1, a] for a in range(len(corners[0]))]
        + [[a, 0] for a in range(len(corners))]
        + [[a, len(corners[0]) - 1] for a in range(len(corners))]
    )
    while len(queue) > 0:
        row, col = queue.pop(0)
        if corners[row][col]:
            continue
        corners[row][col] = True
        if row > 0 and col > 0:
            inside[row - 1][col - 1] = False
        if row > 0 and col < len(inside[0]):
            inside[row - 1][col] = False
        if row < len(inside) and col > 0:
            inside[row][col - 1] = False
        if row < len(inside) and col < len(inside[0]):
            inside[row][col] = False
        if row > 0 and col > 0 and col < len(inside[0]):
            if (
                pipe[row - 1][col - 1]
                and pipe[row - 1][col]
                and (data[row - 1][col - 1] in "-FL" or data[row - 1][col] in "-7J")
            ):
                pass
            else:
                queue.append([row - 1, col])
        if row < len(inside) - 1 and col > 0 and col < len(inside[0]):
            if (
                pipe[row][col - 1]
                and pipe[row][col]
                and (data[row][col - 1] in "-FL" or data[row][col] in "-7J")
            ):
                pass
            else:
                queue.append([row + 1, col])
        if row > 0 and row < len(inside) and col > 0:
            if (
                pipe[row - 1][col - 1]
                and pipe[row][col - 1]
                and (data[row - 1][col - 1] in "|F7" or data[row][col - 1] in "|LJ")
            ):
                pass
            else:
                queue.append([row, col - 1])
        if row > 0 and row < len(inside) and col < len(inside[0]) - 1:
            if (
                pipe[row - 1][col]
                and pipe[row][col]
                and (data[row - 1][col] in "|F7" or data[row][col] in "|LJ")
            ):
                pass
            else:
                queue.append([row, col + 1])

    total = sum([line.count(True) for line in inside])
    return total


if __name__ == "__main__":
    config = 4
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result)
    pyperclip.copy(result)
