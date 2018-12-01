from junction import Junction
from Histogram import Histogram

class Word:
    def __init__(self, word):
        self.word = word
        self.uniqueChars = list(sorted(set(self.word)))
        self.hist = Histogram(self.uniqueChars, self.word)

    exists = lambda self, x:[i for (y, i) in zip(self.uniqueChars, range(len(self.uniqueChars))) if x == y]

    def find_hist_entry(self, char):
        return self.hist.get_hist_entry(char)

    def get_unique_chars(self):
        return ''.join(self.uniqueChars)