from Histogram import Histogram
from Word import Word
from copy import deepcopy

class WordPair:
    def __init__(self, word1, word2):
        # ? passed as a callback to 
        self.wordstrings = [word1, word2]
        self.words = []
        self.WORDUTIL = Word("")
        self.uniquechars = self.WORDUTIL.get_unique_chars(word1+word2)
        for w in self.wordstrings:
            self.words.append(Word(w))
            
        self.hist = Histogram(self.uniquechars, self.wordstrings, True)
        self.get_junctions()

    

    def get_junctions(self):
        self.junctions = {}
        for char in self.uniquechars:
            j = self.hist.get_junctions(char)
            if(len(j) > 0):
                self.junctions.update({char:j})
    
    
    def get_common_characters(self):
        commChars = ""
        for junction in self.junctions.items():
            for entry in junction[1]:
                for key, value in entry.items():
                    commChars += key[value]
        return self.WORDUTIL.get_unique_chars(commChars)

    def calculate_Entanglement(self, junctions):
        E = 0
        for junction in junctions.items():
            E += len(junction[1])
        return E


    def remainingJunctions(self, junc, juncs):
        junction = deepcopy(junc)
        junctions = deepcopy(juncs)
        # ? should selected junction also be removed?
        # ? could refactor with zip
        neighbors = {}
        for k, v in junction.items():
            neighbors.update({"pre": {k:v-1}})
            neighbors.update({"post": {k:v+1}})
            for junction in junctions.items():
                index = 0
                for entry in junction[1]:
                    for key, value in entry.items():
                        if(k == key and v ==value):
                            junctions[key[value]].pop(index)
                        for neighbor in neighbors.items():
                            for keyi, valuei in neighbor[1].items():                        
                                if(key == keyi and value == valuei ):                                    
                                    junctions[key[value]].pop(index)
                index += 1
        return junctions
    def sort_E(self, elem):
        return elem[0]*(-1)

    def shake(self):
        self.potentialE = []
        for tupple in self.junctions.items():
            for junction in tupple[1]:
                juncs = self.remainingJunctions(junction, self.junctions)
                self.potentialE.append((self.calculate_Entanglement(juncs), junction))
        self.potentialE.sort(key=self.sort_E)
        return self.potentialE  

    def compare_wordstrings(self, wrdstr):
        return ''.join(self.wordstrings).find(wrdstr) > -1