
class Histogram:
    def __init__(self, uniqueChars, word):
        self.hist = {}
        for char in uniqueChars:
            self.hist.update({char:HistEntry(char, word)})

    def get_hist_entry(self, char):
        for key in self.hist.keys():
            if(char == key):
                return self.hist[key]

class HistEntry:
    def __init__(self, char, word):
        self.char = char
        self.indexes = self.get_indexes(char, word)

    get_indexes = lambda self, x, xs:[i for (y, i) in zip(xs, range(len(xs))) if x == y]
