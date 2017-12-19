# Chapter 7 : Model aggregation
Model aggregations (ensemble methods) are the methods to ensemble or average the models on hands. The ensembled models can be called a **meta-model** which can be used either in classification and regression case. The concept is for reducing the bias of model dependency, and it also can be view as an alternative way of regularization. The aggregation models introduced in this chapter are : **Majority voting aggregation**

- [**Example 1 - Majority Voting Aggregation**](example_01_majorityVote.ipynb)
   - Introduce the **ensemble error**
   - Intorduce two methods with **counting maximum votes** and **averaging probability**.
   - Demonstrates the full procedure to train an ensembled model.
   - Visualize ROC, decision regions and hyperparameter optimization.

- [**Example 2 - Boostrap Aggregation**](example_02_boostrap.ipynb)

---
###### Correspoding example codes
* Example 1 @ [example_01_majorityVote.ipynb](example_01_majorityVote.ipynb)

###### Functions and classes  
* [MajorityVoteClassifier.py](MajorityVoteClassifier.py) : class `MajorityVoteClassifier` for Majority Vote Classification method. \
