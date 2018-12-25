class Junction:
    def __init__(self, char, primary, secondary):
        self.char = char
        self.primary = primary
        self.primaryWordIndex = primary.find_hist_entry(char)
        self.secondary = secondary
        self.secondaryWordIndex = secondary.find_hist_entry(char)
        self.unselect()
        self.junction_output()


    def select(self):
        self.selected = True

    def unselect(self):
        self.selected = False

    def is_neighbor(self):
        self.neighbor = True

    def junction_output(self):
        print(self.char)
        print(self.primary.word)
        print(self.secondary.word)
        print(self.secondaryWordIndex.indexes)
        print(self.primaryWordIndex.indexes)