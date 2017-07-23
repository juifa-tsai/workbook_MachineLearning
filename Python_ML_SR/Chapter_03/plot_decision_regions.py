import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_regions( X, y, classifier, test_idx=None, resolution=0.02, highlightSize=100 ):

    ### setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # np.unique(y) -> (1, -1)
    # colors[:len(np.unique(y))] -> ('red', 'blue')

    ### plot the decision suface
    # extract the minimum of 0 colume-variable & expand with 1 cm
    x1_min = X[:, 0].min() - 1 if X[:, 0].min() - 1 < 0 else 0
    x2_min = X[:, 1].min() - 1 if X[:, 0].min() - 1 < 0 else 0
    x1_max = X[:, 0].max() + 1
    x2_max = X[:, 1].max() + 1

    # Making a grid 2-D suface w.r.t. the resolution
    xx1, xx2 = np.meshgrid( np.arange(x1_min, x1_max, resolution),
                            np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(x1_min, xx1.max())
    plt.ylim(x2_min, xx2.max())

    # plot all samples
    for idx, c1 in enumerate(np.unique(y)):
        plt.scatter( x=X[y == c1, 0], y=X[y == c1, 1],
                     alpha=0.8, c=cmap(idx), marker=markers[idx],
                     label=c1)

    # Highlight test samlpes
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter( X_test[:, 0], X_test[:, 1], c='', alpha=1., linewidths=1, marker='o', s=highlightSize, edgecolors='black', label='test set' )
