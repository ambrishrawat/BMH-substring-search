import unittest
from utils_asgn import *
from classes.concept import Concept
from classes.sentence import Sentence
import csv

class TestSearchMethods(unittest.TestCase):

    def test_BruteForce(self):
        self.assertTrue(BruteForce('Not in the pattern','in the'))
        self.assertFalse(BruteForce('Not in the pattern','in  the'))

    def test_BMHSearch(self):

        str_1 = 'in the'
        self.assertTrue(BMHSearch('Not in the pattern',str_1,Concept.preprocess_table(str_1)))


        str_2 = 'in  the'
        self.assertFalse(BMHSearch('Not in the pattern',str_2,Concept.preprocess_table(str_2)))


    def test_runs(self):

        #read sentences from a file
        import csv
        from findCon import run_singlep,run_multip

    	conlist = []
	with open('./concepts.list','r') as csvfile:
	    reader = csv.reader(csvfile)
	    for row in reader:
		conlist.append(Concept(row[0]))

        with open('./test.list','r') as csvfile:
           
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
               
                specs = {
                            'sen': Sentence(row[0]),
                            'conlist': conlist
                        }

		y1 = run_multip(specs)
		y2 = run_singlep(specs)	
                y3 = [r for r in row[1:] if r!='']
		case = set(y1)==set(y2)==set(y3)
		self.assertTrue(case)

if __name__ == '__main__':
    unittest.main()

