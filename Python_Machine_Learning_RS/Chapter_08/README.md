# Chapter 8 : Application for Sentiment Analysis

- [**Example 1 - Basic Techniques of Nature Language Processing**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_08/example_01_basicNLP.ipynb?flush_cache=true)
   - Introduce Techniques of the Nature Language Processing (NLP).
   - The preprocessing of sentiment analysis.
- [**Example 2 - Sentiment training with IMBd data, grid searching**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_08/example_02_gridSearch.ipynb?flush_cache=true)
   - The IMBd data are downloaded from [http://ai.stanford.edu/~amaas/data/sentiment](http://ai.stanford.edu/~amaas/data/sentiment).
   - Use the machine learning and NLP techniques to train IMBd movie review data.
   - Using grid-search to optimize to parameters.

- [**Example 3 - Sentiment training with IMBd data, out-of-core learning**](https://nbviewer.jupyter.org/github/juifa-tsai/workbook_MachineLearning/blob/master/Python_Machine_Learning_RS/Chapter_08/example_03_outofcore.ipynb?flush_cache=true)
   - Similar procedure to Example 2 but using **out-of-core learning** to have better parameters for training.

---
###### Correspoding example codes
* Chapter 8 @ [Chapter_08](.)
* Example 1 @ [example_01_basicNLP.ipynb](example_01_basicNLP.ipynb)
* Example 2 @ [example_02_IMBd.ipynb](example_02_gridSearch.ipynb)  
* Example 3 @ [example_03_outofcore.ipynb](example_02_gridSearch.ipynb)

:warning: **If the example code (`*.ipynb`) can't be loaded, please *"copy"* its Github URL and *"paste"* to [nbviewer](https://nbviewer.jupyter.org) :warning:**

###### Functions and classes  
* [imbdToCSV.py](imbdToCSV.py) : function `imbdToCSV()` to transfer IMBd data to CSV file. Please install **pyprind** first by `pip install pyprind`.
