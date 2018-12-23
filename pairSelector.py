class PairSelector:
    def __init__(self, wordPairs):
        wordPairs.sort(key=self.take_entanglement)
        self.wordPairs = wordPairs
        self.iter = iter(self.wordPairs)

    def take_entanglement(self,elem):
        return elem.calc_entanglement()

    def next(self):
        wp = next(self.iter)
        return (wp.words[0], wp.words[1], self.select_junction(wp))
# ?how do we know which junction returns the highest entanglement for all wordpairs
    def recalc_entanglement(self):
        self.wordPairs.sort(key=self.take_entanglement)
    
    def select_junction(self, wp):
        junc = wp.non_det_junctions.pop()
        self.recalc_entanglement()
        return junc