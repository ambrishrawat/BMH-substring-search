#!/usr/bin/env python

from classes.sentence import Sentence
from classes.concept import Concept
from utils_asgn import *
import argparse
import csv

def run(specs):

    #preprocess the sentemce
    sen = process_sen(specs['sen'])

    #find concepts
    con_in_sen = filter(lambda concept: specs['search_algo'](sen,concept),specs['conlist'])


    print(con_in_sen)
    #reduce
    '''
    def reduce_c(x,y):
        if x[[0] is True:
            return True
    reduce(lambda x,y: (True,x[1]+y[1]))
    '''
    pass


    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to convert a list of strings to concepts')

    #epochs, batch_size and model ID
    parser.add_argument('--sen', type=str, default='Which restaurants do West Indian ?food', help='sentence string')
    parser.add_argument('--conlist', type=str, default='./concepts.list', help='location of file containing the list of concepts')
    args = parser.parse_args()
   
    
    #arguments from the parser
    sen = Sentence(args.sen)
    conlist_fpath = args.conlist

    #read the list of concepts from the specified file
    conlist = []
    with open(conlist_fpath,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            conlist.append(Concept(row[0]))

    specs = {
            'sen': sen,
            'conlist':conlist, 
            'search_algo':naivePythonComparison 
            }

    #run
    coneps = run(specs)
    
    
