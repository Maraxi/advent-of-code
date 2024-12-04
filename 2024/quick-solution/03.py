from helpers import load, wrap
import re


def matches(s: str):
    reg = re.compile(r"(do(?:n't)?\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    matches = reg.findall(s)
    # print(matches)
    return matches


def multiply(lis: list[tuple]):
    sum = 0
    for entry in lis:
        s, a, b = entry
        if s != "":
            continue
        sum += int(a) * int(b)
    return sum


def multiply2(lis: list[tuple]):
    sum = 0
    active = True
    for entry in lis:
        s, a, b = entry
        if s != "":
            if s == "do()":
                active = True
            elif s == "don't()":
                active = False
            else:
                raise ValueError(s)
        else:
            if active:
                sum += int(a) * int(b)
    return sum


@wrap
def main():
    content = "".join(load())
    results = matches(content)
    yield multiply(results)
    yield multiply2(results)


if __name__ == "__main__":
    main()
