#!/usr/bin/env python

from model_defs import *
from utils import *
import argparse
import pandas as pd
import os
import numpy as np
import csv
from keras.callbacks import Callback
import time
from keras.optimizers import RMSprop, SGD, Adagrad, Adadelta, Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard



def run(specs):
    
    ''' Make the mid directory '''
    directory = os.path.join(specs['work_dir'],specs['save_id'])
    if not os.path.exists(directory):
        os.makedirs(directory)

    """logging"""
    logfilename = os.path.join(specs['work_dir'],specs['save_id'],"log.txt")
    with open(logfilename, mode='w') as logfile:
        for key in sorted(list(specs.keys())):
            value = specs[key]
            print("{}: {}".format(key, value))
            logfile.write("{}: {}\n".format(key, value))
            logfile.flush()

    '''define the optimiser and compile'''
    model = specs['model']()

    model.compile(loss='categorical_crossentropy', 
            optimizer=specs['optimisation'], 
            metrics=['accuracy'])

    '''callbacks'''
    checkpointer = ModelCheckpoint(
            filepath=os.path.join(specs['work_dir'],specs['save_id'],'model.hdf5'), 
            verbose=1, 
            save_best_only=True)

    earlystopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)

    tboard = TensorBoard(log_dir=os.path.join(specs['work_dir'],specs['save_id'],'logs_tb'),
            histogram_freq=0, write_graph=False, write_images=False)

    c = Cifar_npy_gen(batch_size=specs['batch_size'])

    ''' save the final model'''
    # serialize model to JSON
    model_json = model.to_json()
    with open(os.path.join(specs['work_dir'],specs['save_id'],"model_arch.json"), "w") as json_file:
        json_file.write(model_json)
    
    #Can be replaced by NPYGenerators so that the last batch doesnt roll over the training set

    '''call fit_generartor'''
    model.fit_generator(
        generator=c.train_gen,
        samples_per_epoch=50000,
        nb_epoch=epochs,
        validation_data = c.test_gen,
        nb_val_samples = 10000,
        callbacks=[checkpointer,earlystopping,tboard],
        verbose=1)

    model.save(os.path.join(specs['work_dir'],specs['save_id'],"model_final.h5"))
    pass


    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Script to convert a list of strings to concepts')

    #epochs, batch_size and model ID
    parser.add_argument('--sen', type=str, default='Which restaurants do West Indian food', help='sentence string')
    args = parser.parse_args()
   
    
    #arguments from the parser
    sen = args.sen
    
    specs = {
            'model': model,
            'epochs': epochs,
            'batch_size': batch_size,
            'save_id': model.__name__,
            'optimisation': 'adam',
            'work_dir': '/u/ambrish/models'
            }

    #run
    coneps = run(sen)
    
    
