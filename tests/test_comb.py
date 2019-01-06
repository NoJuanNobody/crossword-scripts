import unittest
import sys
sys.path.append('..')
from combinator import Combinator

class CombinatorTest(unittest.TestCase):
    """tests that combinator works as designed"""
    def setUp(self):
        callback = lambda a,b: str(b)+str(a)
        self.combinator = Combinator(callback)

    def testIter(self):
        """.cominator correctly applies callbacks to items"""
        print("combinator correctly itterates")
        arr = ['a', 'b', 'c']
        res = self.combinator.iterate(arr)
        self.assertEqual(len(res), 3)
        self.assertListEqual(res, ['ab', 'ac', 'bc'])

    def test_CrossProduct(self):
        """ test cross product"""
        print("combinator correctly makes cross product")
        arr = ['1', '6']
        arr2 = ['3','2', '4']
        res = self.combinator.cross_prod(arr,arr2)
        self.assertEqual(len(res), 6)

    
    def test_combination_exsists(self):
        """
        can tell when a combination exsists
        """
        print("correctly catches duplicates")
        arr = ['12']
        res = self.combinator.combination_exsists('21', arr)
        self.assertTrue(len(res) > 0)

    def test_large(self):
        arr = [1,2,3,4,5,6,7,8]
        res = self.combinator.iterate(arr)
        print("testing long combination")
        # print(res)
        # print(len(res))
        #? [1!,2!,3!,4!,5!,6!,7!,8!]
        #? ['12'p, '13', '23'p, '14', '24', '34', '15', '25', '35', '45', '16', '26', '36', '46', '56'p, '17', '27', '37', '47'p, '57', '67', '18'p, '28', '38', '48', '58', '68', '78']
        #? ['12'p, '23'p, '56'p, '47'p,'18'p]
        #? [1!,2!,3!,4!,5!,6!,7!,8!]
        # ? 8123 56 47 
        # ! need to keep track of words being paired
        # ! need to keep track of crosswords being generated
