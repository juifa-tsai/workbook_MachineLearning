# Chapter 7 : Model aggregation
Model aggregations (ensemble methods) are the methods to ensemble or average the models on hands. The ensembled models can be called a **meta-model** which can be used either in classification and regression case. The concept is for reducing the bias of model dependency, and it also can be view as an alternative way of regularization. The aggregation models introduced in this chapter are : **Majority voting aggregation**

- [**Example 1 - Majority Voting Aggregation**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_01_majorityVote.ipynb)
   - Introduce the **ensemble error**
   - Intorduce two methods with **counting maximum votes** and **averaging probability**.
   - Demonstrates the full procedure to train an ensembled model.
   - Visualize ROC, decision regions and hyperparameter optimization.

- [**Example 2 - Bootstrap Aggregation**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_02_bootstrap.ipynb)
   - Intoduce the **Bootstrao Aggregation**, so call **bagging method**.
   - Comparing the performace between single decision tree and *bagged* trees.

- [**Example 3 - Adaptive boosting**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_03_adaBoost.ipynb)
   - Indroduce the **Adaptive boosting (AdaBoost)** method to obtain strong learners from weak learners.
   - Demonstrate and compare the performace between weak learners and **AdaBoost** with *1-depth decision tree* and *perceptron*.

---
###### Correspoding example codes
* Chapter 7 @ [Chapter_07](.)
* Example 1 @ [example_01_majorityVote.ipynb](example_01_majorityVote.ipynb)
* Example 2 @ [example_02_bootstrap.ipynb](example_02_bootstrap.ipynb)
* Example 3 @ [example_03_adaBoost.ipynb](example_03_adaBoost.ipynb)     

:warning: **If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:**

###### Functions and classes  
* [MajorityVoteClassifier.py](MajorityVoteClassifier.py) : class `MajorityVoteClassifier` for Majority Vote Classification method.
