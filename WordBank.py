#	todo: need to figure out how many wordpairs should be selected from all wordpair combinations
from Word import Word
from combinator import Combinator
from WordPair import WordPair
from copy import deepcopy

class WordBank:
        def  __init__(self):
                self.state = {}
                self.history=0

        # def loop(self):
        #         self.iterateState()
        #         self.shake_junctions()
        #         self.shake_wp()

        def make_combinations(self, words):
                self.words = words
                CM = Combinator(WordPair)
                self.combinations = CM.iterate(words)

        def iterateState(self):
                self.history += 1
                self.state.update({str(self.history):{
                        "wordpairs":[]
                }})
        def get_wordpairs_at(self, history):
                return self.state[str(history)]["wordpairs"]
        
        def get_frame_at(self, history):
                return self.state[str(history)]
        
        def sort_WP(self, elem):
                return elem[1][0][0]
                        
        def shake_junctions(self): 
                for combination in self.combinations:
                        entanglmentArr = combination.shake()
                        self.state[str(self.history)]["wordpairs"].append((combination, entanglmentArr))
        
        def shake_wp(self):
                wordpairs = self.get_wordpairs_at(self.history)
                wordpairs.sort(key=self.sort_WP)

        def sameJunction(self, j1, j2):
                for tupple in j1.items():
                        for tupple2 in j2.items():
                                if(tupple == tupple2):
                                        return True
                

        def select_new_wordPairs(self):
                wordpairs = self.get_wordpairs_at(self.history)
                frame = self.get_frame_at(self.history)
                frame.update({
                        "s_junctions":[], 
                        "snakes": [], 
                        "words":deepcopy(self.words)
                        })
                selectedJunctions = frame["s_junctions"]
                for item in wordpairs:
                        loop = True
                        if(len(selectedJunctions)):
                                while loop:
                                        for i in selectedJunctions:
                                                
                                                if(item[1] == []):
                                                        loop = False
                                                        break 
                                                if(self.sameJunction(item[1][0][1], i)):
                                                        item[1].pop(0)
                                                else:
                                                        selectedJunctions.append(item[1][0][1])
                                                        # self.remove_word_list(frame["words"], item[1][0][1])
                                                        # self.merge_snakes(frame["snakes"], item[1][0][1])
                                                        #	todo: add snake to snakes list, or modify/merge entry if one or more words are already in snakes 
                                                        loop = False                                                
                                                        break
                        else:
                                selectedJunctions.append(item[1][0][1])
                                # self.remove_word_list(frame["words"], item[1][0][1])
                                # self.merge_snakes(frame["snakes"], item[1][0][1])
                                #	todo: add snake to snakes list, or modify/merge entry if one or more words are already in snakes 
                        #	todo: take item and pop words from word list
                        #	todo: when all words in arr are paired, use snakes to start new frame/iterate state
                # print("selected junctions", selectedJunctions) 
                # ! need to keep track of words being paired
                # ! need to keep track of crosswords being generated
                # ! stop selecting junctions when all words are paired
        def remove_word_list(self, words, junction):
                for tupple in junction.items():
                        i = 0
                        for word in words:
                                if(tupple[0] == word):
                                        words.pop(i)
                                i += 1

        def merge_snakes(self, snakes,  junction):
                print("j", junction)
                index = 0
                for word in junction.wordstrings:
                        for snake in snakes:
                                res = snake[0][0].compare_wordstrings(word)
                                index += 1