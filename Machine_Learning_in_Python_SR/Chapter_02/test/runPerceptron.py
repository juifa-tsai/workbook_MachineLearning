#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Perceptron import Perceptron

df = pd.read_csv('../data/iris.data', header=None)
print df.tail()

# Filling y and X
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0,2]].values

# Ploting : significance variables
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
#plt.show()


# Percpetron setting
print 'Running percepton algorithm....'
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X,y)
print 'Done'

# Plotting
plt.plot
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()
