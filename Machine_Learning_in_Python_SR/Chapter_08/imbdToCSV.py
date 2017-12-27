#!/usr/bin/env python
import pyprind
import pandas as pd
import numpy as np
import os

# IMBd data : http://ai.stanford.edu/~amaas/data/sentiment
# Train data: 25,000
# Test data:  25,000

def imbdToCSV( path_in='../data/aclImdb', path_out='../data/imbd.csv' ):

    pbar = pyprind.ProgBar(50000)
    labels = {'pos':1, 'neg':0}
    df = pd.DataFrame()

    # Extract data to dataframe
    print '[INFO] Extracting data from %s....'% path_in
    for s in ('test', 'train'):
        for l in ('pos', 'neg'):
            path = path_in+'/%s/%s'%(s, l)
            for file in os.listdir(path):
                with open(os.path.join(path, file), 'r') as infile:
                    txt = infile.read()
                df = df.append([[txt, labels[l]]], ignore_index=True)
                pbar.update()
    df.columns = ['review', 'sentiment']

    # Shuffle and save
    print '[INFO] Saving data to %s ....'% path_out
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    df.to_csv(path_out)

    return df
