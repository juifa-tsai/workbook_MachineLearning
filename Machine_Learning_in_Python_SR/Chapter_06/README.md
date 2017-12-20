# Chapter 6 : Model validation and paramers optimation
Model validation and parameters optimation are strongly correlatied the results of the learning. The validation can check and avoid the **underfitting** or **overfitting** problem during fitting before applying model to test or comming new data. The optimazation of superparameters can fine tune the model to fit better with the helps of validation. The method introduces here includes example of ***Pipline***, **K-fold cross-validation** and **nested cross-validation** etc.... In the end, the scoring methods are introduced for observing the perfomances of trained model.

- [**Example 1 - Validation methods**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_01_validations.ipynb)
   - Using **pipline** to simplify the process of fitting
   - Achive the **Stratified k-fold cross-validation** by **scikit-learn**'s packages.
   - Visualization of learning curve for checking overfitting issue.
- [**Example 2 - Model selections**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_02_optimations.ipynb)
   - Introduce **validation curve** to find the proper parameter value.
   - Perform simple case of parameter tuning in **regularization parameter**.
   - Fine tuning the parameter with **Grid search**
   - Introduce the combination way of optimation and validation for choosing the model, called **Nested cross-validation**.
- [**Example 3 - Scoring methods**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Machine_Learning_in_Python_SR/Chapter_06/example_03_scoringMethods.ipynb)
   - Start from **Confusion matrix** to introduce common scoring methods.
   - Introduce the basic scoring method: *Precision*, *Recall* and *F1 scores*.
   - Introduce the behavoir of **Receiver operating characteristic (ROC)** with logistic regression model case.

---
###### Correspoding example codes
* Chapter 6 @ [Chapter_06](.)
* Example 1 @ [example_01_validations.ipynb](example_01_validations.ipynb)
* Example 2 @ [example_02_optimations.ipynb](example_02_optimations.ipynb)
* Example 3 @ [example_03_scoringMethods.ipynb](example_03_scoringMethods.ipynb)

:warning: **If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:**
