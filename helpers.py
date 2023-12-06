from pathlib import Path


def _load(file: str):
    with open(file, "r") as f:
        content = f.read().rstrip("\n")
        content = content.split("\n\n")
        if len(content) == 1:
            return content[0].split("\n")
        return [block.split("\n") for block in content]


def load(config):
    match config:
        case 1:
            return _load("sample1.txt")
        case 2:
            return _load("input.txt")
        case 3:
            data = _load("sample2.txt")
            if data[0]:
                return data
            return _load("sample1.txt")
        case 4:
            return _load("input.txt")
