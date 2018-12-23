import unittest
import sys
sys.path.append('..')
from Word import Word


class WordTest(unittest.TestCase):
    """ tests for word.py class """
    def setUp(self):
        self.originalWord = "wonderous"
        self.word = Word(self.originalWord)

    def testInitialization(self):
        """ test if initialization is happening correctly
        -unique chars correctly collects all chars in original word
        -unique chars is correct length
        -original word is present in word instance
        - histogram is present
        """
        uniquechars = self.word.get_unique_chars()
        self.assertTrue(len(uniquechars) == 8)
        for char in self.originalWord:
            self.assertTrue(uniquechars.find(char) > -1)

    def testFindHistEntry(self):
        """ tests that correct histogram entries are returned"""
        char = 'o'
        entry = self.word.find_hist_entry(char)
        self.assertTrue(entry)
        self.assertTrue(entry.char == char)
        self.assertTrue(len(entry.indexes) == 2)
        self.assertEqual([1,6],entry.indexes)

    if __name__ == '__main__':
        unittest.main()