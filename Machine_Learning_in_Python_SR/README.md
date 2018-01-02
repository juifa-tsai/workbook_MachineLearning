# Machine Learning in Python
The book, **Machine Learning in Python**  written by *Sebastian Raschka*, demonstrates and well explaines the motheds and perfomances of ML and data analysis. It does not just provide the application the codes, but the theories behine the ML models are also clear. However, beyond following this book, I also provide a lot of extra tutorials (exersices) for optimation, debugging and test for each cases, whcih based on the inspiration of my expreinces of physics analysis. Some theories in this book may not easy to understand, I also provide clearly derivations and examples if it needs. Thus, this workbook is not just simply demostrating the codes from books, but giving the advance exersices and clear insight of models, since I beilive *"Technology comes, technology goes, but insight is forever"*.

Several models of machine learning intruduced in this workbooks include  **classification** and **regession** cases, and **supervisied** and **unsupervised** learners. Simple examples about data structure for anaylsis with some common tools, which can be done in **Pyhton**, are also provided. In the end, **Nature Language** and **Nueal network** are simply introduced and demonstrated.

The programing language focus on **Python**, and the packages of machine learning models are using **scikit-learn** (v 0.20), **pandas** and **numpy**. The performance and visualization for analysis are using **matplotlib** and **jupyter notebook** in **ipython**. They demonstrates the processes of analysis from data. Sometimes **Scipy** are used.

All the main contants and knowledges are refered to the book [**Machine Learning in Python**, *Sebastian Raschka*](https://sebastianraschka.com/books.html). Several detial theories and mathematical methods are inspired by the book [**Pattern Recognition and Machine Learning**, *Christopher M. Bishop* ](https://books.google.com.tw/books/about/Pattern_Recognition_and_Machine_Learning.html?id=kTNoQgAACAAJ&source=kp_cover&redir_esc=y), , and online courses, detail listed in [resources.md](resources.md).

<img src="../doc/Python_Machine_Learning_RS.jpeg" height="300"> <img src="../doc/Pattern_Recognition_and_Machine_Learning_Bishop.jpeg"  height="300">

（Pictures credited by link-[1](https://books.google.com.tw/books/about/Python_Machine_Learning.html?id=GOVOCwAAQBAJ&source=kp_cover&redir_esc=y) and [2](https://books.google.com.tw/books/about/Pattern_Recognition_and_Machine_Learning.html?id=kTNoQgAACAAJ&source=kp_cover&redir_esc=y)）

##### :warning: If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:

## [Chapter 2 - Basic models of machine learning ](Chapter_02/README.md)
Give the major concept and history of machine learning algorithm. Start from the **supervised learning**: **Perceptron learning algorithm (PLA)**, **Gradient decent algorithm** and **Stochastic gradient decent algorithm** by building own class.
* [Example 1 - Perceptron Linear Algorith, PLA](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_02/example_01_PLA.ipynb?flush_cache=true)
* [Example 2 - PLA with shuffled data](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_02/example_02_PLA.ipynb?flush_cache=true)
* [Example 3 - Ensembling PLA hypotheses](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_02/example_03_PLA.ipynb?flush_cache=true)
* [Example 4 - Adaptive Linear Neuron Gradian Decent](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_02/example_04_AdalineGD.ipynb?flush_cache=true)
* [Example 5 - Stochastic Gradian Decent](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_02/example_05_StochasticGD.ipynb?flush_cache=true)

## [Chapter 3 - Classification models](Chapter_03/README.md)
Give several futher popular learning algorithms in current and foucs on **classification** case with **supervised learning** by using **Scikit-learn** tools, e.g. **PLA**, **Logist regession**, **Support Vector Machine (SVM)**, **decision tree**, **random forest** and **K-nearest neigbors (KNN)**.
* [Example 1 - PLA by *scikit-learn* ](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_03/example_01_PLA.ipynb?flush_cache=true)
* [Example 2 - Logistic Regression](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_03/example_02_LogisticRegression.ipynb?flush_cache=true)
* [Example 3 - Support Vector Machine, SVM](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_03/example_03_SVM.ipynb?flush_cache=true)
* [Example 4 - Tree algorithms](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_03/example_04_TreeAlgorithms.ipynb?flush_cache=true)
* [Example 5 - k-Nearest Neighbor, KNN](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_03/example_05_KNN.ipynb?flush_cache=true)

## [Chapter 4 - Preprocessing data, regularization methods](Chapter_04/README.md)
Gives the basic examples for preprocessing data and introduceing the ***Regularization*** in machine learning, which is for dealing with the overfitting problem. Two Regularization methods, **L1** and **L2**, have clear comparison in this chapter. Except regularization, two feature selection algorithms are introduced: **Sequential backward selection (SBS)** and **Random forest**.

* [Example 1 - Pre-processing with Data](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_01_Preprocessing.ipynb?flush_cache=true)
* [Example 2 - Regularization methods](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_02_Regularization.ipynb?flush_cache=true)
* [Example 3 - Feature selections](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_04/example_03_FeatureSelection.ipynb?flush_cache=true)

## [Chapter 5 - Feature extraction and reduction](Chapter_05/README.md)
Provide important topic about feature extraction and reduction. Several common method will be shown here, e.g. **Principal Component Analysis (PCA)**, **Fisher's Linear Discriminant Analysis (LDA)** and **Kernel PCA**. I also introduce the fundamental theories about **Kernel algorithm**.

* [Example 1 - Principal Component Analysis, PCA](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_05/example_01_PCA.ipynb?flush_cache=true)
* [Example 2 - Fisher's Linear Discriminant Analysis, LDA](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_05/example_02_FisherLDA.ipynb?flush_cache=true)
* [Example 3 - Kernel PCA](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_05/example_03_KernelPCA.ipynb?flush_cache=true)


## [Chapter 6 - Model validation and paramers optimation](Chapter_06/README.md)
Model validation and parameters optimation are strongly correlatied the results of the learning. The validation can check and avoid the **underfitting** or **overfitting** problem during fitting before applying model to test or comming new data. The optimazation of superparameters can fine tune the model to fit better with the helps of validation. The method introduces here includes example of ***Pipline***, **K-fold cross-validation** and **nested cross-validation** etc....   

* [Example 1 - Validation methods](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_01_validations.ipynb?flush_cache=true)
* [Example 2 - Model selections](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_02_optimations.ipynb?flush_cache=true)
* [Example 3 - Scoring methods](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_03_scoringMethods.ipynb?flush_cache=true)

## [Chapter 7 - Model aggregation](Chapter_07/README.md)
The methods can ensemble the models a meta-model which can be used either in classification and regression case. The concept is for reducing the bias of model dependency, and it also can be view as an alternative way of regularization. The aggregation models introduced in this chapter are : **Majority voting Aggregation**

* [Example 1 - Majority Voting Aggregation](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_01_majorityVote.ipynb?flush_cache=true)
* [Example 2 - Bootstrap Aggregation](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_02_bootstrap.ipynb?flush_cache=true)
* [Example 3 - Adaptive boosting](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_07/example_03_adaBoost.ipynb?flush_cache=true)

## [Chapter 8 - Application for Sentiment Analysis](Chapter_08/README.md)

* [Example 1 - Basic Techniques of Nature Language Processing](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_08/example_01_basicNLP.ipynb?flush_cache=true)
* [Example 2 - Sentiment training with IMBd data, grid searching](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_08/example_02_gridSearch.ipynb?flush_cache=true)
* [Example 3 - Sentiment training with IMBd data, out-of-core learning](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_08/example_03_outofcore.ipynb?flush_cache=true)

## [Chapter 9 - Model application on website](Chapter_09/README.md) :construction:

## [Chapter 10 - Regression models ](Chapter_10/README.md)
Foucus on **regression** case in **supervised** machine learning and give a example about **Exploratory Data Analysis** (EDA) for analyzing features. **Linear regression** with/without regularization cases,  
* [Example 1 - Exploratory Data Analysis, EDA](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_10/example_01_EDA.ipynb?flush_cache=true)
* [Example 2 - Linear Gredian Decent Regression ](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_10/example_02_LinearRegressionGD.ipynb?flush_cache=true)
* [Example 3 - Linear Regression with *scikit-learn*](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_10/example_03_LinearRegressionSkLearn.ipynb?flush_cache=true)
* [Example 4 - Regularization in Regression models](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_10/example_04_regularization_regression.ipynb?flush_cache=true)

## [Chapter 11 - Unsupervised models](Chapter_11) :construction:

## [Chapter 12 - Neural network](Chapter_12) :construction:

## [Chapter 13 - Neural network application by Theano](Chapter_13) :construction:

---
> **Scripts** \
> [py2ipy.py](py2ipy.py) : convert .py to .ipynb.  
  ```
  python py2ipy.py --inpy file.py
  ```
> [reWord.csh](reWord.csh) : change file's word of content
  ```
  ./reWord.csh [path] [text1] [text2]
  ```
