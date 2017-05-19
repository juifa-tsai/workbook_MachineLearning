#!/usr/bin/env python
#import os, re, sys, shutil
#import math, ROOT
import numpy as np

class Perceptron(object):
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):

