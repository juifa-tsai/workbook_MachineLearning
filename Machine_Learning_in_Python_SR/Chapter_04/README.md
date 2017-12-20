# Chapter 4 : Preprocessing data, regularization methods
This chapter gives the basic examples for pre-processing data. Several tools can help us to make the dataframe processable and easier to be trained, e.g. **scikit-learn**, **Pandas** and **Numpy**. On the other hand, we also introduce the ***Regularization*** in machine learning to deal with the overfitting problem. Two Regularization methods, **L1** and **L2**, have clear comparison in this chapter. In the end, the alternative algorithms for overfitting are introduced, **Sequential backward selection (SBS)** and **Random forest**. They can help to select most important feature for training, to avoid the dimension disaster.

- [**Example 1 - Pre-processing with Data**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_01_Preprocessing.ipynb)
   - Deal with lost data.
   - Numerate words for training.
   - **One-hot encoder**.
- [**Example 2 - Regularization methods**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_02_Regularization.ipynb)
   - Gives the basic sense of regularization.
   - Performs the sparse behavior between **L1** and **L2** regularization.

- [**Example 3 - Feature selections**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_03_FeatureSelection.ipynb)
   - Introduce **Sequential backward selection** (SBS) algorithm.
   - Extrcat the importance of features with **Random forest**.

---
###### Correspoding example codes
* Chapter 4 @ [Chapter_04](.)
* Example 1 @ [example_01_Preprocessing.ipynb](example_01_Preprocessing.ipynb)
* Example 2 @ [example_02_Regularization.ipynb](example_02_Regularization.ipynb)
* Example 3 @ [example_03_FeatureSelection.ipynb](example_03_FeatureSelection.ipynb)

:warning: **If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:**

###### Functions and classes
* [sbs.py](sbs.py) : class `SBS` for Sequential backward selection (SBS) method.
