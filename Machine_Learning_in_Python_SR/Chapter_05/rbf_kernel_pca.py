#!/usr/bin/env python

"""
rbf_kernel_pca : RBF kernel PCA algorithm
"""

#### Libraries
# Standard libraries
# Third-party libraties
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np

def rbf_kernel_pca(X, gamma, n_componets):

    # Calculate pairwise squared Euclidean distance
    # in the MxN dimensional dataset
    sq_dists = pdist(X, 'sqeuclidean')

    # Convert pairwise distances into a square matrix
    mat_sq_dists = squareform(sq_dists)

    # Compute the symmetric kernel matrix
    K = exp(-gamma * mat_sq_dists)

    # Center the kernel matrix
    N = K.shape[0]
    one_n = np.ones((N, N))/N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)

    # Obtaining eigenpairs from the centrered kernel matrix
    # numpy.eigh returns them in sorted order
    eigvals, eigvecs = eigh(K)  

    # Collect the top k eigenvectors (projected smaples)
    alpha = np.column_stack((eigvecs[:, -i] for i in range(1, n_components + 1))) # X_pc
    
    # Collect the correspoding eigenvalues
    lambdas = [eigvals[-i] for i in range(1, n_components+1)]

    return alpha, lambdas
