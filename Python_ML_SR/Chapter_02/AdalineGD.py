#!/usr/bin/env python
import numpy as np

# Adapte Linear Neuron Gradian Decent
class AdalineGD(object):

    def __init__(self, eta=0.01, n_iter=10):
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

    def activation(self, X):
        # Compute linear activiation
        return self.net_output(X)

    def predict(self, X):
        # y = sign(w.X)
        return np.where(self.activation(X) >= 0.0, 1, -1)

    def checkMisclassified(self, X, y):
        #self.misc = np.zeros(len(y),len(X[0]))
        self.misc = np.array([])

        for xi, target in zip(X,y):
            check = target * self.predict(xi)
            if check < 0 :
                if len(self.misc) == 0:
                    self.misc = np.append(self.misc, xi)
                else :
                    self.misc = np.vstack((self.misc, xi))

        return len(self.misc)
