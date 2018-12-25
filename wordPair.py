from Histogram import Histogram

class WordPair:
    def __init__(self, word1, word2):
        # ? passed as a callback to 
        self.words = [word1, word2]
        self.junctions =[]


    def get_junctions(self, one, two):
        uniqueChars = one.get_unique_chars()
        hist = Histogram(uniqueChars, [one, two], True)
        junctions = []
        for char in uniqueChars:
            juncs = hist.get_junctions(char)
            for junc in juncs:
                junctions.append(junc)
        
        