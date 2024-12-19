from helpers import load, wrap


class Trie:
    def __init__(self):
        self.val = 0
        self.children = {}

    def add(self, word):
        if word == "":
            self.val += 1
        else:
            if word[0] not in self.children:
                self.children[word[0]] = Trie()
            self.children[word[0]].add(word[1:])

    def __getitem__(self, letter=None):
        if letter is None:
            return self.val
        if letter not in self.children:
            return None
        return self.children[letter]


def solution():
    trie = Trie()
    for word in available:
        trie.add(word)

    res1, res2 = 0, 0
    for target in targets:
        tries = [[1, trie]]

        for letter in target:
            new_tries = []
            total = 0
            for val, t in tries:
                tnew = t[letter]
                if tnew is not None:
                    new_tries.append((val, tnew))
                    total += val * tnew.val
            if total > 0:
                new_tries.append((total, trie))
            tries = new_tries
        else:
            if total > 0:
                res1 += 1
                res2 += tries[-1][0]

    return res1, res2


@wrap
def main():
    global available, targets
    available, targets = load()
    available = available.split(", ")

    res1, res2 = solution()
    yield res1
    yield res2


if __name__ == "__main__":
    main()
