# Chapter 2 : Basic models of machine learning
This chapter give the introduction about the basic machine learning (ML) and start from classification case: ***linear perceptron***, ***adoptive linear perceptron*** and ***gradient decent algorithm*** etc. Before going to next chapter to using online open-source ML package, **scikit-learn**, we build the own ML class by **pandas** and **numpy** package. We also perform and visisulize the results with **matplotlib** and **ipython** packges. This is not only focusing on implement part but demonstrate the detail caculation and theories behinde the models. Some exmaples also give the optimaztion test which extends from the book. The exercises are all using iris data.  

1. [Example 1 - Perceptron Linear Algorith, PLA :point_right: example_01_PLA.ipynb](example_01_PLA.ipynb)
   - Apply `Perceptron` to data, [iris.data](Chapter_02/iris.data) , to demonstrate the learing process.
2. [example_02_PLA](example_02_PLA.ipynb)
3. [example_03_PLA](example_03_PLA.ipynb)
4. [example_04_AdalineGD](example_04_AdalineGD.ipynb)
5. [example_05_StochasticGD](example_05_StochasticGD.ipynb)

---
> **Functions and class**\
> [Perceptron.py](Perceptron.py) : class `Perceptron` for perceptron algorithm. \
> [Perceptron_online.py](Perceptron_online.py) : class `Perceptron_online` \
> [AdalineGD.py](AdalineGD.py) : class `AdalineGD` \
> [AdalineGD_online.py](AdalineGD_online.py) : class `AdalineGD_online` \
> [plot_decision_regions.py](plot_decision_regions.py) : function `plot_decision_regions`

### Perceptron algorithm
* It is online method, i.e. update weighting in each data point.
  ```
  X : array of variables
  w : array of weighting
  y : binary results
  ```
  ```
  z = w.X
  y = sign(z), i.e. 1 or -1
  ```

* Update weighting in each data point when ``y != y_true``.<br />
  ```
  w' = w + dw
     = w + eta.dy.X
  dw = eta.dy.X
     = eta.( y_true - y ).X
  ```
  1. ``dy.X`` : Fixing the wrong angle (too big/small) by extending/subtracting the normal vector of hyperplane ``w``. When whole dataset having zero of this, the hyperplane can classify the data in correct side.<br />
  2. ``eta``  : The training rate.

* Stop iteration<br />
When statistics of dataset is big enough, the algorithm can stop when ``dw = 0``, while the small statistics is using whole dataset with many iterations.  
  1. When ``dw = 0``.
  2. Linear separable.

### Class ``Perceptron``
@ Perceptron.py
* Global values
   * Parameters<br />
  ``eta`` : (**float**) Learning rate.<br />
  ``n_iter`` : (**int**) Passes over the training datasets (iteration).
   * Attributes<br />
  ``w_`` : (**1d-array**) Weights after fitting.<br />
  ``errors_`` : (**list**) # of misclassifications in every epoch.
* Functions
  * ``fit (X, y)`` : The functions for doing perceptron learning iteratively. <br />
  * ``net_input (X)`` : Calculate ``z = w.X = w'.X' + w_0.X_0, (X_0 = 1)``<br />
  * ``predict (X)`` : Get predict sign of y as`` y = sign(w.X)`` <br />
