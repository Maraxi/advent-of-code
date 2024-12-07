from helpers import load, wrap


def solution1():
    total = 0
    for line in lines:
        res, remain = line.split(": ")
        res = int(res)
        args = [int(e) for e in remain.split(" ")]

        possible = [args[0]]
        for arg in args[1:]:
            update = []
            for p in possible:
                update.append(p + arg)
                update.append(p * arg)
            possible = update
        if res in possible:
            total += res
    return total


def solution2():
    total = 0
    for line in lines:
        res, remain = line.split(": ")
        res = int(res)
        args = [int(e) for e in remain.split(" ")]

        possible = [args[0]]
        for arg in args[1:]:
            update = []
            for p in possible:
                update.append(p + arg)
                val = p * arg
                if val <= res:
                    update.append(val)
                l = len(str(arg))
                val = p * 10**l + arg
                if val <= res:
                    update.append(val)
            possible = update
        if res in possible:
            total += res
    return total


@wrap
def main():
    yield solution1()
    yield solution2()


if __name__ == "__main__":
    lines = load()
    main()
