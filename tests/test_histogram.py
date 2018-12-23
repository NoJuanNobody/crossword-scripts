import unittest
import sys
sys.path.append('..')
from Histogram import Histogram

class HistogramTest(unittest.TestCase):
    "tests for histogram.py and histEntry.py"
    def setUp(self):
        self._originalWord = 'wonderous'
        self._uniqueChars = "denorsuw"
        self._char = 'o'
        self.hist = Histogram(self._uniqueChars, self._originalWord)

    def test_get_hist_entry(self):
        """tests that histogram entries return correctly when search and indexed"""
        entry = self.hist.get_hist_entry(self._char)
        self.assertTrue(entry)
        self.assertTrue(entry.char == self._char)
        self.assertTrue(len(entry.indexes) == 2)
        self.assertEqual([1,6],entry.indexes)