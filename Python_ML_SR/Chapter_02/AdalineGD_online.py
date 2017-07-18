#!/usr/bin/env python
import numpy as np
from numpy.random import seed

# Adapte Linear Neuron Gradian Decent
class AdalineGD_online(object):

    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        if random_state:
            seed(random_state)

    def fit(self, X, y):
        # initial w_ = [w_0,w_1....w_features] = 0
        self._initialize_weights(X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost)/len(y)
            self.cost_.append(avg_cost)

        return self

    def partial_fit(self, X, y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
            
        return self

    def _shuffle(self, X, y):
        r = np.random.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):
        self.w_ = np.zeros(1+m)
        self.w_initialized = True

    def _update_weights(self, xi, target):
        # Caculate difference (dy = errors) from net input
        output = self.net_input(xi)
        error = (target - output)

        # dW = eta * Sum_data(dy * X)
        self.w_[1:] += self.eta * xi.dot(error) # same with np.dot(X, errors) but much efficient
        self.w_[0] += self.eta * error     # eta * dy * x_0 (x_0=1)
        cost = 0.5 * error**2
        return cost


    def net_input(self, X):
        # w.X = w'.X' + w_0.X_0, (X_0 = 1), self.w_[0] is a single value
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        # Compute linear activiation
        return self.net_input(X)

    def predict(self, X, outputBound=False, zeroRange=0.00001):
        # y = sign(w.X)
        return np.where(self.activation(X) >= 0.0, 1, -1)
