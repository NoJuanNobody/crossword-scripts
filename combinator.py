from wordPair import WordPair

class Combinator:
    def __init__(self, cb):
        self.cb = cb

    get_indexes = lambda self, x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

    def iterate(self, arr):
        self.history = []
        self.result = []
        for index, entity in enumerate(arr):
            for index2, entity2 in enumerate(arr):
                if(index == index2):
                    continue
                wPair = WordPair(entity, entity2)
                if(not self.get_indexes(wPair.name, self.history) and not self.get_indexes(wPair.reverseName, self.history)):
                    self.result.append(self.cb(wPair))
                    self.history.append(wPair.name)
        return self.history
