from wordBank import WordBank
words = ['hadal','parvitude','peruvian', 'boring']
bank = WordBank()
bank.findWordJunctions(words)
bank.count_junctions_by_char()



#  *separate script for assembling words and junctions to be layout friendly
# ? could have alot to do with word length and number or junctions available after
# ? determined junctions are picked from non determined junctions
# ? words with more possible junctions are described as a high degree of entanglement
# ? entanglent has a direct relationship with layout flexibility
# ? order of junction determines flexibility.
# * separate script should be written for visualisation
#	todo: use python package to generate image
#	todo: iterate through the data structure and print words in crossword layout