#!/usr/bin/env python

from utils_asgn import *
import argparse

def run(specs):
    
    pass


    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to convert a list of strings to concepts')

    #epochs, batch_size and model ID
    parser.add_argument('--sen', type=str, default='Which restaurants do West Indian food', help='sentence string')
    parser.add_argument('--conlist', type=str, default='./concepts.list', help='location of file containing the list of concepts')
    args = parser.parse_args()
   
    
    #arguments from the parser
    sen = args.sen
    conlist_fpath = args.conlist

    #read the list of concepts from the specified file

    specs = {
            'sen': sen,
            'conlist':conlist     
            }

    #run
    coneps = run(sen)
    
    
