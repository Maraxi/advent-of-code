from helpers import *
import pyperclip
import re
import math
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop
from functools import reduce
from datetime import datetime


def solution1():
    total = 0
    return total


def solution2():
    total = 0
    return total


if __name__ == "__main__":
    config = 1
    start = datetime.now()
    data = load(config)
    result = solution1() if config < 3 else solution2()
    print(result, datetime.now() - start)
    pyperclip.copy(result)
