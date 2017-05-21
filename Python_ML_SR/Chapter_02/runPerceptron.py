#!/usr/bin/env python
import pandas as pd

df = pd.read_csv('iris.data', header=None)
print df.tail()

