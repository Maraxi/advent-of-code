from pathlib import Path


def _load(file: str):
    with open(file, "r") as f:
        content = f.read().rstrip("\n")
        content = content.split("\n\n")
        if len(content) == 1:
            return content[0].split("\n")
        return [block.split("\n") for block in content]


def load(config):
    if config[0] == 2:
        return _load("input.txt")
    if config[1] == 2 and Path("sample2.txt").exists():
        return _load("sample2.txt")
    return _load("sample1.txt")
