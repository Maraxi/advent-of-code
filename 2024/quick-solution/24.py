from helpers import load, wrap, Direction, Point, Grid
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


functions = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x ^ y,
}


def solution1(inputs):
    state = dict(inputs.items())
    unresolved = [*gates]

    while unresolved:
        for i, (x, op, y, _, out) in enumerate(unresolved):
            if x in state and y in state:
                state[out] = functions[op](state[x], state[y])
                unresolved.pop(i)
                break
    total = 0
    for key, val in reversed(sorted(state.items())):
        if key[0] == "z":
            total = (total << 1) + val
        else:
            break
    return total


def solution2():
    empty_state = {}
    for i in range(45):
        empty_state[f"x{i:02}"] = 0
        empty_state[f"y{i:02}"] = 0

    for i in range(45):
        test_state = dict(empty_state.items())
        test_state[f"x{i:02}"] = 1
        test_state[f"y{i:02}"] = 1
        res = solution1(test_state)
        print(f"left{i:2}", f"{res:57_b}")
        # Look at outputs manually and compare with image from jupyter notebook
    return 0


@wrap
def main():
    global inputs, gates
    inputs = [inp.split(": ") for inp in inputs]
    inputs = {name: int(val) for name, val in inputs}
    gates = [gate.split(" ") for gate in gates]

    yield solution1(inputs)
    yield solution2()


if __name__ == "__main__":
    inputs, gates = load()
    main()
