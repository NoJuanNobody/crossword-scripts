import enum

class Orientation(enum.Enum):
        x = 1
        y = 2


class Tile:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y

    def get_coords(self):
        return {
            'x': self.x,
            'y': self.y
        }


class Crossword:
    def __init__(self, word):
        self.words = {}
        self.root = word
        self.tail = None
        self.place_root_word()
        self.orientation = Orientation.x
        self.place_root_word()

    def switch_orientation(self):
        self.orientation = Orientation.y if self.orientation == Orientation.x else Orientation.y

    def place_root_word(self):
        self.place_word(self.root, None)

    def get_tile_by_char(self, tiles, char):
        matchTile = None
        for tile in tiles:
            if tile.char == char:
                matchTile = tile
        return matchTile
    def prepare_locale(self, junction):
        if(junction):
            # index of word to be placed
            index = junction.secondaryWordIndex.indexes[0]
            self.switch_orientation()
            # coords of junction where it should be placed
            origin = self.get_tile_by_char(self.tail.tiles, junction.char).get_coords()
            origin['y'] -= 1
        else:
            index = 0
            self.orientation = Orientation.x
            origin = {'x':0, 'y':0}
        return {
            'index': index, 
            'origin':origin
        }

    def iterate_around_junction(self, word, locale, cb):
        resList = []
        print (self.orientation)
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


    def place_word(self, word, junction):
        self.words.update({word.word:word})
        locale = self.prepare_locale(junction)
        self.words[word.word].tiles = self.iterate_around_junction(word, locale, self.place_char)
        self.tail = word

    def merge_crossword(self, secondaryCrossword, junction):
        # prepare locale
        locale = self.prepare_locale(junction)
        secondaryCrossword.update_crossword_coords()
        for word in secondaryCrossword.words:
            self.words.update(word)

    def update_crossword_coords(self, lastLocale):
        for key, word in self.words.items():
            for tile in word.tiles:
                tile.x += lastLocale['origin']['x']
                tile.y += lastLocale['origin']['y']

    # todo pass wordpair to crossword?