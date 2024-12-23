from helpers import load, wrap, Direction, Point, Grid
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop


def solution1():
    total = set()
    for key, val in pcs.items():
        if key[0] != "t":
            continue
        listing = list(sorted(val))
        for i, v1 in enumerate(listing):
            for v2 in listing[i + 1 :]:
                if v2 in pcs[v1]:
                    triple = tuple(sorted([key, v1, v2]))
                    total.add(triple)

    return len(total)


def solution2():
    all_nodes = tuple(sorted(pcs.keys()))
    next_nodes = [[n] for n in all_nodes]
    while next_nodes:
        last_nodes = next_nodes
        next_nodes = []
        for nodes in last_nodes:
            last_node = nodes[-1]
            i = all_nodes.index(last_node)
            for other_node in all_nodes[i + 1 :]:
                edges = pcs[other_node]
                for node in nodes:
                    if node not in edges:
                        break
                else:
                    next_nodes.append([*nodes, other_node])

    clique = ",".join(sorted(last_nodes[0]))
    return clique


@wrap
def main():
    global pcs
    pcs = defaultdict(set)
    for line in lines:
        p1, p2 = line.split("-")
        pcs[p1].add(p2)
        pcs[p2].add(p1)
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
