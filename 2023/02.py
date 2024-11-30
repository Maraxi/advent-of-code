from helpers import *


def prep():
    for line in data:
        k = line.split(":")
        id = int(k[0][5:])
        shows = k[1].split(";")
        possible = True
        for show in shows:
            show = show.replace(" ", "")
            show = show.split(",")
            for ele in show:
                if ele[-3:] == "red":
                    if int(ele[:-3]) > 12:
                        possible = False
                elif ele[-4:] == "blue":
                    if int(ele[:-4]) > 14:
                        possible = False
                elif ele[-5:] == "green":
                    if int(ele[:-5]) > 13:
                        possible = False
        if possible == True:
            yield id


def solution1():
    data = prep()
    l = list(data)
    print(sum(l))


def solution2():
    total = 0
    for line in data:
        k = line.split(":")
        id = int(k[0][5:])
        shows = k[1].split(";")
        minimums = [0, 0, 0]
        possible = True
        for show in shows:
            show = show.replace(" ", "")
            show = show.split(",")
            for ele in show:
                if ele[-3:] == "red":
                    minimums[0] = max(minimums[0], int(ele[:-3]))
                elif ele[-4:] == "blue":
                    minimums[1] = max(minimums[1], int(ele[:-4]))
                elif ele[-5:] == "green":
                    minimums[2] = max(minimums[2], int(ele[:-5]))
        total += minimums[0] * minimums[1] * minimums[2]
    print(total)


if __name__ == "__main__":
    config = 4
    data = load(config)
    solution1() if config < 3 else solution2()
