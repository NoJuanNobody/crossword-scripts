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
        print("word is initializing correctly")
        uniquechars = self.word.get_unique_chars_str()
        self.assertTrue(len(uniquechars) == 8)
        for char in self.originalWord:
            self.assertTrue(uniquechars.find(char) > -1)

