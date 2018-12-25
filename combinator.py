
class Combinator:
    def __init__(self, cb):
        self.cb = cb

    get_indexes = lambda self, x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

    def iterate(self, arr):
        self.history = []
        self.result = []
        for index, entity in enumerate(arr):
            for index2, entity2 in enumerate(arr):
                if(index == index2):
                    continue
                self.result.append(self.cb(entity, entity2))
        return self.result

#	todo: write cross product
    def cross_prod(self, arr, arr2):
        self.history = []
        self.result = []
        for entity in enumerate(arr):
            for entity2 in enumerate(arr2):
                self.result.append(self.cb(entity[1], entity2[1]))
        return self.result