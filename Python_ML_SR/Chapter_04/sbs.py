#!/usr/bin/env python
from itertools import combinations
from sklearn.base import clone
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

class SBS():

    def __init__( self, estimator, k_features, scoring=accuracy_score, test_size=0.25, random_state=1 ):

        self.scoring      = scoring
        self.estimator    = clone(estimator)
        self.k_features   = k_features
        self.test_size    = test_size
        self.random_state = random_state


    def fit( self, X, y ):
        
        """
        self.indices_ : the last subset, default is all features
        self.subsets_ : the best subsets for each iteration, default is all features
        self.scores_  : the best scores for each iteration, default is the scores of all features
        ------------
        1. Iterate (dim - k_features) times
        2. scan and check the perfomance of the combinations,
        3. record the best performance, (dim - 1)
        4. stop if dim < k_features, or back to 1.
        """

        X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=self.test_size, random_state=self.random_state )

        dim = X_train.shape[1]
        self.indices_ = tuple(range(dim)) # tuple for itertools.combinations(lables, r)
        self.subsets_ = [self.indices_]
        score = self._calc_score( X_train, y_train, X_test, y_test, self.indices_ )
        self.scores_ = [score]

        while dim > self.k_features:
            scores  = []
            subsets = []

            for p in combinations( self.indices_, r=dim-1 ): 
                # itertools.combinations(lables, r): non-repeat combinations "C^{len(lables)}_{r}/r!"
                # Using it to check/scan all perfomances of training reaults without anyone of fearutres
                score = self._calc_score( X_train, y_train, X_test, y_test, p )
                scores.append(score)
                subsets.append(p)

            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)
            self.scores_.append(scores[best])
            dim -= 1
      
        self.k_score_ = self.scores_[-1]

        return self


    def transform( self, X ):
        return X[:, self.indices_]


    def _calc_score( self, X_train, y_train, X_test, y_test, indices ):

        self.estimator.fit(X_train[:, indices], y_train)
        y_pred = self.estimator.predict(X_test[:, indices])
        score = self.scoring(y_test, y_pred)
        return score
    

