import Word as WD
import combinator as COM


class WordBank:
        def  __init__(self):
                self.junctions=[]
                self.words = []

        def freq(self, arr):
                return lambda x:[i for (y, i) in zip(arr, range(len(arr))) if x == y]

        def compare_word_histograms(self, wordOne, wordTwo):
                primary = wordOne if len(wordOne.uniqueChars) < len(wordTwo.uniqueChars) else wordTwo
                secondary = wordOne if (primary != wordOne) else wordTwo
                for pChar in primary.uniqueChars:

                        if(len(secondary.exists(pChar)) > 0):
                                self.junctions.append(WD.Junction(pChar, primary, secondary))

        def findWordJunctions(self, wordStrings):
                for wordStr in wordStrings:
                        self.words.append(WD.Word(wordStr))
                COM.Combinator(self.compare_word_histograms).iterate(self.words)

        def count_junctions_by_char(self):
                self.charCount = {}
                for junction in self.junctions:
                        if junction.char in self.charCount:
                                self.charCount[junction.char] += 1
                        else:
                                self.charCount.update({junction.char:1})
                print('junction count',self.charCount)

