# Machine Learning in Python (Sebastian Raschka)
The book, **Machine Learning in Python**  written by *Sebastian Raschka*, demonstrates and well explaines the motheds and perfomances of ML and data analysis. It does not just provide the application the codes, but the theories behine the ML models are also clear. However, beyond following this book, I also provide a lot of extra tutorials (exersices) for optimation, debugging and test for each cases, whcih based on the inspiration of my expreinces of physics analysis. Some theories in this book may not easy to understand, I also provide clearly derivations and examples if it needs. Thus, this workbook is not just simply demostrating the codes from books, but giving the advance exersices and clear insight of models, since I beilive *"Technology comes, technology goes, but insight is forever"*.

Several models of machine learning intruduced in this workbooks include  **classification** and **regession** cases, and **supervisied** and **unsupervised** learners. Simple examples about data structure for anaylsis with some common tools, which can be done in **Pyhton**, are also provided. In the end, **Nature Language** and **Nueal network** are simply introduced and demonstrated.

The programing language focus on **Python**, and the packages of machine learning models are using **scikit-learn**, **pandas** and **numpy**. The performance and visualization for analysis are using **matplotlib** and **jupyter notebook** in **ipython**. They demonstrates the processes of analysis from data. Sometimes **Scipy** are used.

All the main contants and knowledges are refered to the book [**Machine Learning in Python**, *Sebastian Raschka*](https://sebastianraschka.com/books.html). Several detial theories and mathematical methods are inspired by the book [**Pattern Recognition and Machine Learning**, *Christopher M. Bishop* ](https://books.google.com.tw/books/about/Pattern_Recognition_and_Machine_Learning.html?id=kTNoQgAACAAJ&source=kp_cover&redir_esc=y), and online course [**Machine Learning Foundations/Techniques**, *Hsuan-Tien Lin*](https://www.csie.ntu.edu.tw/~htlin/).

<img src="../doc/Python_Machine_Learning_RS.jpeg" height="300"> <img src="../doc/Pattern_Recognition_and_Machine_Learning_Bishop.jpeg"  height="300">
<img src="../doc/Lin.jpg"  height="200">

（Pictures credited by link-[1](https://books.google.com.tw/books/about/Python_Machine_Learning.html?id=GOVOCwAAQBAJ&source=kp_cover&redir_esc=y), [2](https://books.google.com.tw/books/about/Pattern_Recognition_and_Machine_Learning.html?id=kTNoQgAACAAJ&source=kp_cover&redir_esc=y) and [3](https://www.youtube.com/watch?v=tDq_CSzFRYA&t=7s)）


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
Provide important topic about feature extraction and reduction. Several common method will be shown here, e.g. **Principal Component Analysis (PCA)**, **Fisher's Linear Discriminant Analysis (LDA)** and **Kernel PCA**. I also introduce the fundamental theories about **Kernel algorithm**.

* [example_01_PCA](Chapter_05/example_01_PCA.ipynb)
* [example_02_FisherLDA](Chapter_05/example_02_FisherLDA.ipynb)
* [example_03_KernelPCA](Chapter_05/example_03_KernelPCA.ipynb)


## [Chapter 6 - Model validation and paramers optimation](Chapter_06)
Model validation and parameters optimation are strongly correlatied the results of the learning. The validation can check and avoid the **underfitting** or **overfitting** problem during fitting before applying model to test or comming new data. The optimazation of superparameters can fine tune the model to fit better with the helps of validation. The method introduces here includes example of ***Pipline***, **K-fold cross-validation** and **nested cross-validation** etc....   

* [example_01_validations](Chapter_06/example_01_validations.ipynb)
* [example_02_optimations](Chapter_06/example_02_optimations.ipynb)
* [example_03_scoringMethods](Chapter_06/example_03_scoringMethods.ipynb)

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
