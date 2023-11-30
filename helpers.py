def load(file: str):
    with open(file, 'r') as f:
        content = f.read().rstrip("\n")
        content = content.split("\n\n")
        if len(content) == 1:
            return content[0].split("\n")
        return [block.split("\n") for block in content]
