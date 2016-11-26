import unittest
from utils_asgn import *
from classes.concept import Concept

class TestSearchMethods(unittest.TestCase):

    def test_BruteForce(self):
        self.assertTrue(BruteForce('Not in the pattern','in the'))
        self.assertFalse(BruteForce('Not in the pattern','in  the'))

    def test_BMHSearch(self):

        str_1 = 'in the'
        self.assertTrue(BMHSearch('Not in the pattern',str_1,Concept.preprocess_table(str_1)))


        str_2 = 'in  the'
        self.assertFalse(BMHSearch('Not in the pattern',str_2,Concept.preprocess_table(str_2)))


if __name__ == '__main__':
    unittest.main()

