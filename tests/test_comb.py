import unittest
import sys
sys.path.append('..')
from combinator import Combinator

class CombinatorTest(unittest.TestCase):
    """tests that combinator works as designed"""
    def setUp(self):
        callback = lambda a,b: a+b
        self.combinator = Combinator(callback)

    def testIter(self):
        """cominator correctly applies callbacks to items"""
        print("combinator correctly itterates")
        arr = ['a', 'b', 'c']
        res = self.combinator.iterate(arr)
        self.assertTrue(len(res) == 6)
        self.assertListEqual(res, ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'])

    def test_CrossProduct(self):
        """ test cross product"""
        print("combinator correctly makes cross product")
        arr = ['1', '6']
        arr2 = ['3','2', '4']
        res = self.combinator.cross_prod(arr,arr2)
        self.assertEqual(len(res), 6)