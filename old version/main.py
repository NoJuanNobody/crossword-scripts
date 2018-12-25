from wordBank import WordBank
from pairSelector import PairSelector

from crossword import Crossword
from Word import Word
from junction import Junction

words = ['parvitude','peruvian']
bank = WordBank()
bank.findWordJunctions(words)
selector = PairSelector(bank.wordPairs)
for i in selector.wordPairs:
    wp = selector.next()
    crossword = Crossword()
    crossword.place_root_word(wp[0], wp[2])
    crossword.place_word(wp[1] ,wp[2])
    crossword.print_crossword()
    
    

