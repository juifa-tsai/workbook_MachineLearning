#!/usr/bin/env python
import numpy as np

class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        # initial w_ = [w_0,w_1....w_features] = 0
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0

            for xi, target in zip(X, y):
                # update = eta.dy
                update = self.eta * (target - self.predict(xi))
                # dw = eta.dy.X = update.X
                self.w_[1:] += update * xi
                self.w_[0] += update # dy.x_0 (x_0=1)
                # Number of misclassifications in each iteration (epoch)
                errors += int(update != .0)

            self.errors_.append(errors)

        return self

    def net_input(self, X):
        # w.X = w'.X' + w_0.X_0, (X_0 = 1)
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        # y = sign(w.X)
        return np.where(self.net_input(X) >= 0.0, 1, -1)
