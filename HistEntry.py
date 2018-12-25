class HistEntry:
    def __init__(self, char, word):
        self.char = char
        self.indexes = self.get_indexes(char, word)

    get_indexes = lambda self, x, xs:[(i, xs) for (y, i) in zip(xs, range(len(xs))) if x == y]
