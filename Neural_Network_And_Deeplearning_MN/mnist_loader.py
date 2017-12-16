#!/usr/bin/env python

"""
mnist_loader : for loading MNIST data and reture proper data structure for neural network
"""

#### Libraries
# Standard libraries
import cPickle
import gzip

# Third-party libraties
import numpy as np

def load_data(datapath='data/mnist.pkl.gz'):

    f = gzip.open(datapath, 'rb')
    training_data, validation_data, test_data = cPickle.load(f)
    f.close()
    return (training_data, validation_data, test_data)


def load_data_wapper(datapath='data/mnist.pkl.gz'):

    tr_d, va_d, te_d = load_data(datapath)

    training_inputs   = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results  = [vectorized_result(y) for y in tr_d[1]] # for NN with 10x1 matrix 
    training_data     = zip(training_inputs, training_results)

    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data   = zip(validation_inputs, va_d[1])

    test_inputs       = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data         = zip(test_inputs, te_d[1])

    return (training_data, validation_data, test_data)

def vectorized_result(j):

    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

