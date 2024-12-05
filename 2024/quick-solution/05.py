from helpers import load, wrap
from collections import Counter


def solution1():
    total = 0
    global rules
    rules = [(rule.split("|")) for rule in rules]
    for update in updates:
        entries = update.split(",")

        ignore = False
        for i, first in enumerate(entries):
            if ignore:
                break
            for second in entries[i + 1 :]:
                if [second, first] in rules:
                    # print(f"found {(second, first)}. ignore")
                    ignore = True
                    incorrect.append(update)
                    break

        if ignore:
            continue
        middle = int(entries[len(entries) // 2])
        total += middle
    return total


def get_sorting(nodes, rules):
    if len(nodes) == 0:
        return []
    relevant = [rule for rule in rules if rule[0] in nodes and rule[1] in nodes]
    # print(relevant)
    if len(relevant) == 0:
        return nodes

    lefts = Counter()
    rights = Counter()
    for rel in relevant:
        lefts[rel[0]] += 1
        rights[rel[1]] += 1

    # print(lefts, rights)
    begin = [key for key in lefts.keys() if rights[key] == 0]
    end = [key for key in rights.keys() if lefts[key] == 0]
    # print(begin + end)
    remain = [n for n in nodes if n not in begin and n not in end]
    recursion = get_sorting(remain, relevant)
    # print(remain, recursion)

    return begin + recursion + end


def solution2():
    total = 0
    # print(incorrect)
    # print(rules)
    for update in incorrect:
        entries = update.split(",")
        # print(update)
        s = get_sorting(entries, rules)
        # print(s)
        total += int(s[len(s) // 2])
    return total


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    rules, updates = load()
    incorrect = []
    main()
