# Chapter 2
## Perceptron algorithm
### Description  
* It is online method, i.e. update weighting in each data point. <br />
  ```
  X : array of variables
  w : array of weighting
  y : binary results
  ```
  ```
  z = wX<br />
  y = sign(z), i.e. 1 or -1
  ```
* Update weighting in each data point when ``y != y_true``.<br />
  ```
  w' = w + dw
  dw = eta( y_true - y )X
  ```
  ``eta`` is training rate.

* Stop iteration<br />
When statistics of dataset is big enough, the algorithm can stop when ``dw = 0``, while the small statistics is using whole dataset with many iterations.  
  1. When ``dw = 0``.
  2. Linear separable.

### Class ``Perceptron.py``
* Global values
   * Parameters<br />
  ``eta`` : (**float**) Learning rate.<br />
  ``n_iter`` : (**int**) Passes over the training datasets (iteration).
   * Attributes<br />
  ``w_`` : (**1d-array**) Weights after fitting.<br />
  ``errors_`` : (**list**) # of misclassifications in every epoch.
* Functions
  * ``fit (X, y)`` : <br />
  * ``net_input (X)`` : <br />
  * ``predict (X)`` : <br />
