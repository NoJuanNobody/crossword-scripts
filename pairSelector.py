class PairSelector:
    def __init__(self, wordPairs):
        wordPairs.sort(key=self.take_entanglement)
        self.wordPairs = wordPairs
        self.iter = iter(self.wordPairs)

    def take_entanglement(self,elem):
        return elem.calc_entanglement()

    def next(self):
        return next(self.iter)
# todo build on function to recieve callback?