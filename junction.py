class Junction:
    def __init__(self, char, primary, secondary):
        self.char = char
        self.primary = primary
        self.secondary = secondary
        self.primaryWordIndex = primary.find_hist_entry(char)
        self.secondaryWordIndex = secondary.find_hist_entry(char)
        self.select()
        # print(self.char, self.primary.word, self.secondary.word)
    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def is_neighbor(self):
        self.neighbor = True