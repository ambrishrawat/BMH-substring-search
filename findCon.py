#!/usr/bin/env python

from classes.sentence import Sentence
from classes.concept import Concept
from utils_asgn import *
import argparse
import csv
from multiprocessing import Pool
import itertools


def run_singlep(specs):
    
    ''' Single-thread Processing '''
    
    return search(sen = specs['sen'],
            con_list = specs['conlist'])



def run_multip(specs):

    '''
    Multi-processing:

    A demonstration of seacrhing concepts asynchronously with
    data-parallelism 
    '''

    pool = Pool()

    def chunks(l, n):
        for i in range(0, len(l), n):
            yield {'sen':specs['sen'],'conlist':l[i:i + n]}

    y = [] 
    for x_ in pool.imap(run_singlep,chunks(specs['conlist'],5)):
        y.append(x_)

    y = list(itertools.chain(*y))   
    return y

    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to convert a list of strings to concepts')

    #epochs, batch_size and model ID
    parser.add_argument('--sen', type=str, default='Which restaurants do West Indian ?food', help='sentence string')
    parser.add_argument('--fpath', type=str, default='./concepts.list', help='location of file containing the list of concepts')
    args = parser.parse_args()
   
    
    #arguments from the parser
    sen = Sentence(args.sen)
    conlist_fpath = args.fpath

    #read the list of concepts from the specified file
    conlist = []
    with open(conlist_fpath,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            conlist.append(Concept(row[0]))

    '''
    the preprocessing innvolves on-the-fly generation of table 
    for each concept in the csv. This can be either be done apriori
    for the whole databse or can be done on-the-fly got batches of data
    for data_parallilsm case
    '''

    #specifictions for search-runs
    specs = {
            'sen': sen,
            'conlist':conlist, 
            }

    #run
    y = run_multip(specs)
   

    for y_ in y:
        print(y_)
    
