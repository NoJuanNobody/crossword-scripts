
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
            name = str(index)+' '+str(index2)
            if(not self.get_indexes(name, self.history) and not self.get_indexes(name[::-1], self.history)):
               self.result.append(self.cb(entity, entity2))
               self.history.append(name)
      return self.result
