import unittest
import sys
sys.path.append('..')
from Histogram import Histogram
from Word import Word
class HistogramTest(unittest.TestCase):
    "tests for histogram.py and histEntry.py"
    def setUp(self):
        self._char = 'o'

    def test_get_hist_entry(self):
        """tests that histogram entries return correctly when search and indexed"""
        print("""histogram entries return correctly""")
        self._originalWord = ['wonderous']
        self._uniqueChars = "denorsuw"
        self.hist = Histogram(self._uniqueChars, self._originalWord, False)
        entry = self.hist.get_hist_entry(self._char)
        self.assertTrue(entry)
        self.assertTrue(entry.char == self._char)
        
        self.assertEqual(len(entry.indexes), 2)
        self.assertEqual([(1, 'wonderous'),(6, 'wonderous')],entry.indexes)

    def test_junction_init(self):
        """test that histogram can create a junction
        -returns a tupple with the letter and an arry of tuples.
        each tupple contains the index and the word string
        """
        print("""histogram can create a junction""")
        self._char = 'o'
        self.originalWords = ["wonderous", 'proton']
        self.hist = Histogram([self._char], self.originalWords, True)
        junctions = self.hist.get_junctions(self._char)
        
        self.assertEqual(self._char, junctions[0])
        self.assertEqual(len(junctions[1]), 4)

    def test_junctions_init(self):
        """test that histogram can create many junctions
        -returns a tupple with the letter and an arry of tuples.
        each tupple contains the index and the word string
        """
        print("""histogram can make many junctions""")
        wonderous = Word("wonderous")
        proton = Word("proton")
        self._chars = wonderous.get_unique_chars_str() + proton.get_unique_chars_str()
        print(self._chars)
        self.originalWords = [wonderous.word, proton.word]
        self.hist = Histogram(self._chars, self.originalWords, True)
        junctions_r = self.hist.get_junctions('r')
        junctions_o = self.hist.get_junctions('o')
        junctions_n = self.hist.get_junctions('n')
        self.assertEqual('r', junctions_r[0])
        print(junctions_r)
        self.assertEqual(len(junctions_r[1]), 1)
        self.assertEqual('o', junctions_o[0])
        self.assertEqual(len(junctions_o[1]), 4)
        self.assertEqual('n', junctions_n[0])
        self.assertEqual(len(junctions_n[1]), 1)