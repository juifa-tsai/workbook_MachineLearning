# Chapter 5 : Feature extraction and reduction
This chapter gives the examples for feature extrcation and reduction which are very important topic in data analysis, especially in model training. Here we will introduce some common method, e.g. **Principal Component Algorithm** **(PCA)**, **Fisher's Linear Discriminant Analysis (LDA)** and **Kernel PCA**. I also introduce the fundamental theories about **Kernel algorithm**. The exersice data is using wine data and demonstrating with pure **Numpy** packages, and than comparing with using **Scikit-learn**.

- [**Example 1 - Principal Component Analysis, PCA**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_05/example_01_PCA.ipynb?flush_cache=true)
   - The theories of unsupervisied learner, PCA.
   - Exersice with pure **Numpy** and **Scikit-learn**.
- [**Example 2 - Fisher's Linear Discriminant Analysis, LDA**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_05/example_02_FisherLDA.ipynb?flush_cache=true)
   - The theories of supervisied learner, Fisher's LDA
   - Exersice with pure **Numpy** and **Scikit-learn**.
   - Comparison with PCA
- [**Example 3 - Kernel PCA**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_05/example_03_KernelPCA.ipynb?flush_cache=true)
   - The theories of Kernel and application in PCA
   - Exersice with pure **Numpy** and **Scikit-learn**

---
###### Correspoding example codes
* Chapter 5 @ [Chapter_05](.)
* Example 1 @ [example_01_PCA.ipynb](example_01_PCA.ipynb)
* Example 2 @ [example_02_FisherLDA.ipynb](example_02_FisherLDA.ipynb)
* Example 3 @ [example_03_KernelPCA.ipynb](example_03_KernelPCA.ipynb)

:warning: **If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:**

###### Functions and classes
* [plot_decision_regions.py](plot_decision_regions.py) : function `plot_decision_regions`
* [rbf_kernel_pca.py](rbf_kernel_pca.py) : function `rbf_kernel_pca` for RBF kernel PCA.
