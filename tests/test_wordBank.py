import unittest
import sys
sys.path.append('..')
from WordBank import WordBank
from WordPair import WordPair

class WordBankTest(unittest.TestCase):
    """ tests for wordbank.py class"""
    def setUp(self):
        self._words = ["auror", "author", "wednesday"]
        self.bank = WordBank()
        self.bank.make_combinations(self._words)

    def test_makeCombinations(self):
        """ should make combinations with the desired callback"""
        print("combinator test")
        for comb in self.bank.combinations:
            self.assertIsInstance(comb, WordPair, "all items should be wordpairs")
            self.assertGreater(len(comb.junctions), 0, "should have at least one junction")

    def test_jShake(self):
        """ tests the ability to shake all junctions to get best junction"""
        print("testing the J shake from WB")
        self.bank.iterateState()
        self.bank.shake_junctions()
        Es = [ value[0][0] for (key, value) in self.bank.state['1']["wordpairs"]]
        self.assertEqual(Es, [3, 0, 0])

    def test_wpShake(self):
        """
            tests the sorting or shaking of a state frame
        """
        print("testing the WP shake")
        self.bank.iterateState()
        self.bank.shake_junctions()
        self.bank.shake_wp()
        framePrime = self.bank.get_wordpairs_at(self.bank.history)
        EarrPrime = [v[0][0] for (k,v) in framePrime]
        self.assertListEqual(EarrPrime, [0, 0, 3])

    def test_select_new_wordPars(self):
        """
            selects the new words for printing
        """
        print("selects the new words for printing")
        self.bank.iterateState()
        self.bank.shake_junctions()
        self.bank.shake_wp()
        self.bank.select_new_wordPairs()
        framePrime = self.bank.get_frame_at(self.bank.history)
        testArr = [{'wednesday': 7, 'auror': 0}, {'author': 4, 'auror': 3}]
        self.assertListEqual(framePrime["s_junctions"], testArr, "junctions should match")
