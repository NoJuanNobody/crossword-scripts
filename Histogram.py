from HistEntry import HistEntry
from combinator import Combinator
class Histogram:
    def __init__(self, referenceChars, entities, unique):
        self.hist = {}
        for ent in entities:
            for char in referenceChars:
                if(unique):
                    key = char+"_"+ent
                else:
                    key = char
                self.hist.update({key:HistEntry(char, ent)})

    def get_hist_entry(self, char):
        for key in self.hist.keys():
            if(char == key):
                return self.hist[key]
    
    def get_junctions(self, char):
        entries = []
        for key, value in self.hist.items():
            if(key[:1] == char):
                entries.append(value)
        combinator = Combinator(self.junctionCallback)
        res =  combinator.cross_prod(entries[0].indexes, entries[1].indexes)
        return res

    def junctionCallback(self, ent, ent2):
        return {ent[1]:ent[0], ent2[1]:ent2[0]}