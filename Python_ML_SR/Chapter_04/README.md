# Chapter 4 : Preprocessing data, regularization methods
This chapter gives the basic examples for pre-processing data. Several tools can help us to make the dataframe processable and easier to be trained, e.g. **scikit-learn**, **Pandas** and **Numpy**. On the other hand, we also introduce the ***Regularization*** in machine learning to deal with the overfitting problem. Two Regularization methods, **L1** and **L2**, have clear comparison in this chapter. In the end, the alternative algorithms for overfitting are introduced, **Sequential backward selection (SBS)** and **Random forest**. They can help to select most important feature for training, to avoid the dimension disaster.

1. [example_01_Preprocessing](example_01_Preprocessing.ipynb)
   - Deal with lost data.
   - Numerate words for training.
   - **One-hot encoder**.
2. [example_02_Regularization](example_02_Regularization.ipynb)
   - Gives the basic sense of regularization.
   - Performs the sparse behavior between **L1** and **L2** regularization.

3. [example_03_FeatureSelection](example_03_FeatureSelection.ipynb)
   - Introduce **Sequential backward selection** (SBS) algorithm.
   - Extrcat the importance of features with **Random forest**.


---
> **Functions and class**\
> [sbs.py](sbs.py) : class `SBS`
