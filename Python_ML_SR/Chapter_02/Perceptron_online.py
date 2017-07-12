#!/usr/bin/env python
import numpy as np

class Perceptron_online(object):

    def __init__(self, eta=0.01):
        self.eta = eta
        self.error_ = 0
        self.errorId_ = []

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1]) # initial w_ = [w_0,w_1....w_features] = 0

        i = 0
        while i < y.shape[0]:
            update = self.eta * (y[i] - self.predict(X[i])) # = eta.dy
            # dw = eta.dy.X = update.X
            self.w_[1:] += update * X[i]
            self.w_[0]  += update
            if update != 0:
                self.error_ += 1
                self.errorId_.append(i)
            i += 1

        return self

    def net_input(self, X):
        # w.X = w'.X' + w_0.X_0, (X_0 = 1)
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        # y = sign(w.X)
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def checkMisclassified(self, X, y):
        self.misc = np.array([])

        for xi, target in zip(X,y):
            check = target * self.predict(xi)
            if check < 0 :
                if len(self.misc) == 0:
                    self.misc = np.append(self.misc, xi)
                else :
                    self.misc = np.vstack((self.misc, xi))

        return len(self.misc)
