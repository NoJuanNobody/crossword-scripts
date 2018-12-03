class WordPair:
    def __init__(self, word1, word2):
        self.delimiter = '--'
        name = [word1.word, self.delimiter, word2.word]
        self.name = ''.join(name)
        self.reverseName = ''.join(name[::-1])
        self.non_det_junctions =[]
        self.words = [word1, word2]
        self.get_primary_secondary()
    
    def add_junctions(self, junctions):
        self.non_det_junctions= junctions

    def calc_entanglement(self):
        self.entanglement = len(self.non_det_junctions)
        return self.entanglement

    def get_primary_secondary(self):
        self.primary = self.words[0] if len(self.words[0].uniqueChars) < len(self.words[1].uniqueChars) else self.words[1]
        self.secondary = self.words[0] if self.primary != self.words[0] else self.words[1]
