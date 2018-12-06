from wordBank import WordBank
from pairSelector import PairSelector

from crossword import Crossword
from Word import Word
from junction import Junction

words = ['hadal','parvitude','peruvian', 'boring']
bank = WordBank()
bank.findWordJunctions(words)
selector = PairSelector(bank.wordPairs)
first = selector.next()
second = selector.next()
third = selector.next()

print(first.name, second.name, third.name)

# crosswrd = Crossword(selector.next().words[0])

# crosswrd.place_word(parvitude, aJunc)
# origin = {
#     'x':100,
#     'y':100
# }
# locale = {
#     'index':2,
#     'origin':origin
# }
# crosswrd.update_crossword_coords(locale)
# for key, value in crosswrd.words.items():
#     for tile in value.tiles:
#         print(key, '=>', tile.char, tile.x, tile.y,)



#  *separate script for assembling words and junctions to be layout friendly
# ? could have alot to do with word length and number or junctions available after
# ? determined junctions are picked from non determined junctions
# ? words with more possible junctions are described as a high degree of entanglement
# ? entanglent has a direct relationship with layout flexibility
# ? order of junction determines flexibility.
# * separate script should be written for visualisation
#	todo: use python package to generate image
#	todo: iterate through the data structure and print words in crossword layout
