#!/usr/bin/env python
import numpy as np

class Perceptron_online(object):

    def __init__(self, eta=0.01):
        self.eta = eta

    def fit(self, X, y, max_iter=1):
        self.w_ = np.zeros(1 + X.shape[1]) # initial w_ = [w_0,w_1....w_features] = 0

        i = 0
        for it in range(max_iter):
            n_error = 0
            while i < y.shape[0]:
                update = self.eta * (y[i] - self.predict(X[i])) # = eta.dy
                # dw = eta.dy.X = update.X
                self.w_[1:] += update * X[i]
                self.w_[0]  += update
                if update != 0:
                    n_error += 1
                i += 1

            #if n_error is not 0:
            #    print ' ', it, n_error
            if n_error is 0:
                #print ' stop: ', it
                break

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
