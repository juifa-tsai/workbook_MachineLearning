# Chapter 7 : Model aggregations
Model aggregations (ensemble methods) are the methods to ensemble or average the models on hands. The ensembled models can be called a **meta-model** which can be used either in classification and regression case. The concept is for reducing the bias of model dependency, and it also can be view as an alternative way of regularization. The aggregation models introduced in this chapter are : **Majority voting**

- [**Example 1 - Majority Voting method**](example_01_majorityVote.ipynb)
   - Introduce the **ensemble error**
   - Introduce the **Majority voting** method with counting maximum vote and average probability.
   - Demonstrates the full procedure to train an ensembled model.
   - Visualize ROC, decision regions and hyperparameter optimization.

---
###### Correspoding example codes
* Example 1 @ [example_01_majorityVote.ipynb](example_01_majorityVote.ipynb)

###### Functions and classes  
* [MajorityVoteClassifier.py](MajorityVoteClassifier.py) : class `MajorityVoteClassifier` for Majority Vote Classification method. \
