# Chapter 6 : Model validation and paramers optimation
Model validation and parameters optimation are strongly correlatied the results of the learning. The validation can check and avoid the **underfitting** or **overfitting** problem during fitting before applying model to test or comming new data. The optimazation of superparameters can fine tune the model to fit better with the helps of validation. The method introduces here includes example of ***Pipline***, **K-fold cross-validation** and **nested cross-validation** etc....     

1. [example_01_validations](example_01_validations.ipynb)
   - Using **pipline** to simplify the process of fitting
   - Achive the **Stratified k-fold cross-validation** by **scikit-learn**'s packages.
   - Visualization of learning curve for checking overfitting issue.
2. [example_02_optimations](example_02_optimations.ipynb)
   - Introduce **validation curve** to find the proper parameter value.
   - Perform simple case of parameter tuning in **regularization parameter**.
   - Fine tuning the parameter with **Grid search**
   - Introduce the combination way of optimation and validation for choosing the model, called **Nested cross-validation**.
3. [example_03_scoringMethods](example_03_scoringMethods.ipynb)
   - Start from **Confusion matrix** to introduce common scoring methods.
   - Introduce the basic scoring method: *Precision*, *Recall* and *F1 scores*.
   - Introduce the behavoir of **Receiver operating characteristic (ROC)** with logistic regression model case.
