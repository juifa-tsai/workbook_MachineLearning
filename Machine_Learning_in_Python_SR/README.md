# Machine Learning in Python (Sebastian Raschka)
The artificial intellegent (AI) has been a popular key word in any field, e.g. marketing, robotics, art, biologics, physics anaylsis etc.. However, **machine learning (ML)** is actually the fundametal elements behine the AI. To get into know the work of AI, we can not skip the basis. Thanks to many great experts in the world, we are lucky to have many good tools to know and step into this field. Thus, we are going to step by step to follow the book written by *Sebastian Raschka* to demonstrate and show perfomances of ML models. It does not just provide the application the codes, but the theories behine the ML models are also clear. Beyond following this book, I also provide a lot of extra tutorials for optimation and test for each cases based on my expreinces of physics analysis. Some theories in this book may not easy to understand, I also provide clearly derivations and examples if it needs. Thus, this workbook is not just simply demostrating the codes from books, but giving the advance exersices and clear insight of models, since I beilive *"Technology comes, technology goes, but insight is forever"*.

The models of machine learning intruduced in this workbooks are included  **classification ** and **regession** cases, and **supervisied** and **unsupervised** learns. On the other hand, following the books includes simple examples about data structure for anaylsis with some common tool which can be done in **Pyhton**. In the end, **Nature Language** and **Nueal network** are also provided.

The programing language focus on **Python**, and the packages of machine learning models are using **scikit-learn**, **pandas** and **numpy**. The performance and visualization for analysis are using **matplotlib** and **jupyter notebook** in **ipython**. They demonstrates the processes of analysis from data. Sometimes **Scipy** are used.

## [Chapter 2 - Basic models of machine learning ](Chapter_02)
Give the major concept and history of machine learning algorithm. Start from the **supervised learning**: **Perceptron learning algorithm (PLA)**, **Gradient decent algorithm** and **Stochastic gradient decent algorithm** by building own class.
* [example_01_PLA](Chapter_02/example_01_PLA.ipynb)
* [example_02_PLA](Chapter_02/example_02_PLA.ipynb)
* [example_03_PLA](Chapter_02/example_03_PLA.ipynb)
* [example_04_AdalineGD](Chapter_02/example_04_AdalineGD.ipynb)
* [example_05_StochasticGD](Chapter_02/example_05_StochasticGD.ipynb)

## [Chapter 3 - Classification models](Chapter_03)
Give several futher popular learning algorithms in current and foucs on **classification** case with **supervised learning** by using **Scikit-learn** tools, e.g. **PLA**, **Logist regession**, **Support Vector Machine (SVM)**, **decision tree**, **random forest** and **K-nearest neigbors (KNN)**.
* [example_01_PLA](Chapter_03/example_01_PLA.ipynb)
* [example_02_LogisticRegresion](Chapter_03/example_02_LogisticRegresion.ipynb)
* [example_03_SVM](Chapter_03/example_03_SVM.ipynb)
* [example_04_TreeAlgorithms](Chapter_03/example_04_TreeAlgorithms.ipynb)
* [example_05_KNN](Chapter_03/example_05_KNN.ipynb)

## [Chapter 4 - Preprocessing data, regularization methods](Chapter_04)
Gives the basic examples for preprocessing data and introduceing the ***Regularization*** in machine learning, which is for dealing with the overfitting problem. Two Regularization methods, **L1** and **L2**, have clear comparison in this chapter. Except regularization, two feature selection algorithms are introduced: **Sequential backward selection (SBS)** and **Random forest**.

* [example_01_Preprocessing](Chapter_04/example_01_Preprocessing.ipynb)
* [example_02_Regularization](Chapter_04/example_02_Regularization.ipynb)
* [example_03_FeatureSelection](Chapter_04/example_03_FeatureSelection.ipynb)

## [Chapter 5 - Feature extraction and reduction](Chapter_05)
Provide important topic about feature extraction and reduction. Several common method will be shown here, e.g. **Principal Component Analysis (PCA)**, **Linear Discriminant Analysis (LDA)** and **Kernel PCA**. I also introduce the fundamental theories about **Kernel algorithm**.

* [example_01_PCA](Chapter_05/example_01_PCA.ipynb)
* [example_02_LDA](Chapter_05/example_02_LDA.ipynb)
* [example_03_KernelPCA](Chapter_05/example_03_KernelPCA.ipynb)


## [Chapter 10 - Regression models](Chapter_10)
Foucus on **regression** case in **supervised** machine learning and give a example about **Exploratory Data Analysis** (EDA) for analyzing features. **Linear regression** with/without regularization cases,  
* [example_01_EDA.ipynb](Chapter_10/example_01_EDA.ipynb)
* [example_02_LinearRegressionGD](Chapter_10/example_02_LinearRegressionGD.ipynb)
* [example_03_LinearRegressionSkLearn](Chapter_10/example_03_LinearRegressionSkLearn.ipynb)
* [example_04_regularization_regression](Chapter_10/example_04_regularization_regression.ipynb)

---
> **Scripts** \
> [command.md](command.md) : shows the common and useful command lines. \
> [py2ipy.py](py2ipy.py) : convert .py to .ipynb.\
  ```
  python py2ipy.py --inpy file.py
  ```
