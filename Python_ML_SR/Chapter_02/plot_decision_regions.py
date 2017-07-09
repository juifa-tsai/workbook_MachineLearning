import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.02):
    ### setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'ligtgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # np.unique(y) -> (1, -1)
    # colors[:len(np.unique(y))] -> ('red', 'blue')

    ### plot the decision suface
    x1_min = X[:, 0].min() - 1 # extract the minimum of 0 colume-variable & expand with 1 cm
    x1_max = X[:, 0].max() + 1 # extract the maximum of 0 colume-variable & expand with 1 cm
    x2_min = X[:, 1].min() - 1
    x2_max = X[:, 1].max() + 1

    # Making a grid 2-D suface w.r.t. the resolution
    xx1, xx2 = np.meshgrid(np.arange(0., x1_max, resolution),
                           np.arange(0., x2_max, resolution))

    # np.arange(x1_min, x1_max, resolution) -> 1-D array w.r.t. resolution bewteen min & max values
    # len(np.arange(x1_min, x1_max, resolution)) -> 235 length
    # len(np.arange(x2_min, x2_max, resolution)) -> 305 length
    # len(xx1), 'x' ,len(xx1[0]) -> 305 x 235 grid
    # len(xx2), 'x' ,len(xx2[0]) -> 305 x 235 grid

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(0., xx1.max())
    plt.ylim(0., xx2.max())

    # plot class samples
    for idx, c1 in enumerate(np.unique(y)):
        plt.scatter(x=X[y == c1, 0], y=X[y == c1, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label='setosa' if c1==-1 else 'versicolor' )
