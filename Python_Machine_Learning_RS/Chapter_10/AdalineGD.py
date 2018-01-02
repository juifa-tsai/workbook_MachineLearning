#!/usr/bin/env python
import numpy as np

# Adapte Linear Neuron Gradian Decent
class AdalineGD(object):

    def __init__(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        # initial w_ = [w_0,w_1....w_features] = 0
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):

            # Caculate difference (dy = errors) from net input
            output = self.net_input(X)   # X is Nxd 2-D array
            errors = (y - output)        # errors is N 1-D array

            # dW = eta * Sum_data(dy * X)
            self.w_[1:] += self.eta * X.T.dot(errors) # same with np.dot(X, errors) but much efficient
            self.w_[0] += self.eta * errors.sum()     # eta * dy * x_0 (x_0=1)

            cost = (errors**2).sum()/2.
            self.cost_.append(cost)

        return self

    def net_input(self, X):
        # w.X = w'.X' + w_0.X_0, (X_0 = 1), self.w_[0] is a single value
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        # Compute linear activiation
        return self.net_input(X)
