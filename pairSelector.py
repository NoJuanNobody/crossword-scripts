class PairSelector:
    def __init__(self, wordPairs):
        wordPairs.sort(key=self.take_entanglement)
        self.wordPairs = wordPairs
        for wordpair in self.wordPairs:
            print(wordpair.entanglement)

    def take_entanglement(self,elem):
        return elem.calc_entanglement()

    # todo: select junctions
    # ? if junction
