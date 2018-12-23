import enum

class Orientation(enum.Enum):
        x = 1
        y = 2


class Tile:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
        self.j = False

    def get_coords(self):
        return {
            'x': self.x,
            'y': self.y,
            'char':self.char,
            'j': self.j
        }


class Crossword:
    def __init__(self):
        self.words = {}
        self.root = None
        self.tail = None
        self.orientation = Orientation.x

    def switch_orientation(self):
        self.orientation = Orientation.y if self.orientation == Orientation.x else Orientation.y

    def place_root_word(self, root, junction):
        self.root = root
        self.place_word(self.root, junction)

    def get_tile_by_char(self, tiles, char):
        matchTile = None
        for tile in tiles:
            if tile.char == char:
                tile.j = True
                matchTile = tile
        return matchTile
    def prepare_locale(self, word, junction):
        # index of char for the word to be placed
        print(word.word, junction.primary.word)
        if(word.word == junction.primary.word):
            index = junction.primaryWordIndex.indexes[0]
        else:
            index = junction.secondaryWordIndex.indexes[0]
            # ? find the tile that is a junction to return the origin on the board
            origin = self.get_tile_by_char(self.tail.tiles, junction.char).get_coords()
        self.switch_orientation()
        print('index', index, 'origin', origin)
        return {
            'index': index, 
            'origin': origin
        }

    def iterate_around_junction(self, word, locale, cb):
        resList = []
        for char in word.word:
            resList.append(
                cb(
                    word.word,
                    locale['origin'],
                    locale['index'], 
                    self.orientation
                )
            )
            locale['index'] -= 1
            if locale['index'] < 0:
                locale['index'] = len(word.word)-1
                
        return resList

    def place_char(self, word, pos, index, orientation):
        if orientation == Orientation.x:
            return Tile(word[index], pos['x'] + index, pos['y'])
        else:
            return Tile(word[index], pos['x'], pos['y'] + index)

#	todo: index for second word and positioning differ
# ?currently it is treated as the same.
    def place_word(self, word, junction):
        self.words.update({word.word:word})
        locale = self.prepare_locale(word, junction)
        self.words[word.word].tiles = self.iterate_around_junction(word, locale, self.place_char)
        self.tail = word

    def merge_crossword(self, secondaryCrossword, junction):
        # prepare locale
        locale = self.prepare_locale(junction)
        secondaryCrossword.update_crossword_coords()
        for word in secondaryCrossword.words:
            self.words.update(word)

    def update_crossword_coords(self, lastLocale):
        for word in self.words.items():
            for tile in word.tiles:
                tile.x += lastLocale['origin']['x']
                tile.y += lastLocale['origin']['y']

    # todo pass wordpair to crossword?
    # ? all this needs to do is iterativley update coordinates for all tiles i guess
    def place_word_pair(self, wordPair):
        return None

    def get_max_cords(self):
        xNeg = 0
        xPos = 0
        yNeg = 0
        yPos = 0
        for word in self.words.items():
            for tile in word[1].tiles:
                coords = tile.get_coords()
                
                if(coords['x'] > 0  and xPos < coords['x']):
                    xPos = coords['x']
                elif(coords['x'] < 0  and xNeg > coords['x']):
                    xNeg = coords['x']
                
                if(coords['y'] > 0 and yPos < coords['y']):
                    yPos = coords['y']
                elif(coords['y'] < 0  and yNeg > coords['y']):
                    yNeg = coords['y']

        return (xPos, yPos, xNeg, yNeg)

    def print_crossword(self):
        win = self.get_max_cords()
        board =[]
        for i in range(win[1]-win[3]+1):
            row = []
            for j in range(win[0]-win[2]+1):
                row.append(' ')
            board.append(row)
        for word in self.words.items():
            for tile in word[1].tiles:
                xpos = tile.x-win[2]
                ypos = tile.y-win[3]
                board[ypos-1][xpos-1] = tile.char 
        for rows in board:
                print(str(''.join(rows)))
        print('\n\n')

        

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