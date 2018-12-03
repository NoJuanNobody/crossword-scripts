import Word as WD
import combinator as COM

class WordBank:
        def  __init__(self):
                self.wordPairs=[]
                self.words = []

        def freq(self, arr):
                return lambda x:[i for (y, i) in zip(arr, range(len(arr))) if x == y]

        def compare_word_histograms(self, wordPair):
                junctions = []
                for pChar in wordPair.primary.uniqueChars:
                        if(len(wordPair.secondary.exists(pChar)) > 0):
                                junctions.append(WD.Junction(pChar, wordPair.primary, wordPair.secondary))
                wordPair.add_junctions(junctions)
                self.wordPairs.append(wordPair)

        def findWordJunctions(self, wordStrings):
                for wordStr in wordStrings:
                        self.words.append(WD.Word(wordStr))
                self.history = COM.Combinator(self.compare_word_histograms).iterate(self.words)

        def get_combinations(self):
                historyDictionary = {}
                for combination in self.history:
                        historyDictionary.update({combination:combination.split()})
                return historyDictionary