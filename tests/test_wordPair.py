import unittest
import sys
sys.path.append("..")
from WordPair import WordPair
from Histogram import Histogram

class WordPairTest(unittest.TestCase):
    """tests for wordpair.py class"""

    def setUp(self):
        self.ardous = "arduous"
        self.auror = "auror"
        self.commChars = ['a', 'o', 'r', 'u']
        self.unChars = ['a', 'd', 'o', 'r', 's', 'u']
        self.wp = WordPair(self.ardous, self.auror)

    def test_init(self):
        """test that initialization occurs.
            -wordpair class should init with two words
            -find the unique characters from both words
            -create a histogram of all possible junctions
        """
        print("wordpair inits correctly")
        self.assertEqual(len(self.wp.words), 2)
        self.assertListEqual(self.wp.uniquechars,self.unChars, "these unique chars should be the same but not necessarily in the same order")
        self.assertIsInstance(self.wp.hist, Histogram, "this should be a histogram")

    def test_getJunctions(self):
        """
            test should ensure that junctions are being collected for the wordpair correctly. 
            -for all common chars, a junction will be present
            -empty junctions (hist entries) will not be present
        """
        print("word pair gets junctions for common chars only")
        self.wp.get_junctions()
        self.assertEqual(len(self.commChars), len(self.wp.junctions))
    
    def test_getCommChars(self):
        """
            should return all common characters in a wordpair
        """
        print("should return all common characters in a wordpair")
        comm = self.wp.get_common_characters()
        self.assertEqual(len(comm), len(self.commChars))

    def test_calc_E(self):
        """Should calculate Entanglement for the word pair"""
        print("calc Entanglement for wordpair")
        self.wp.get_junctions()
        E =self.wp.calculate_Entanglement(self.wp.junctions)
        self.assertEqual(E, 6, "Entanglement should be 6" )

    def test_removeNeigbors(self):
        """
        should remove junctions that are neigboars of selected junction
        but should not mutate the original dictionary includes selected junction
        """
        print("remove neighbors")
        self.wp.get_junctions()
        juncts = self.wp.remainingJunctions(self.wp.junctions['r'][0], self.wp.junctions)
        self.assertEqual(len(juncts['u']), 1)
        self.assertEqual(len(juncts['a']), 0)
        self.assertEqual(len(juncts['o']), 0)
        self.assertEqual(len(juncts['r']), 1)
        self.assertNotEqual(len(self.wp.junctions['u']), 1)
        self.assertNotEqual(len(self.wp.junctions['a']), 0)
        self.assertNotEqual(len(self.wp.junctions['o']), 0)
        self.assertNotEqual(len(self.wp.junctions['o']), 2)

    def test_shake(self):
        """
            Shake should return an arr of sorted potential E values when a junctin is selected
        """
        print("testing the j shake")
        self.wp.get_junctions()
        Es = self.wp.shake()
        EsArr = [ key for (key, value) in Es]
        self.assertEqual(EsArr, [3,3,2,2,1,1])

    def test_compareWordstrings(self):
        """
            should be able to tell if there i a word match btwn two word strings
        """
        print("compare wordstrings")
        self.assertFalse(self.wp.compare_wordstrings('jat'))
        self.assertTrue(self.wp.compare_wordstrings('auror'))