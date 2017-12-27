#!/usr/bin/env python
import pyprind
import pandas as pd
import numpy as np
import os

# IMBd data : http://ai.stanford.edu/~amaas/data/sentiment
# Train data: 25,000
# Test data:  25,000

def imbdToCSV( path_in='../data/aclImdb', path_out='../data/imbd.csv', split_test_train=True ):

    pbar = pyprind.ProgBar(50000)
    labels = {'pos':1, 'neg':0}
    dfs    = {'train':pd.DataFrame(), 'test':pd.DataFrame()} 

    # Extract data to dataframe
    print '[INFO] Extracting data from %s....'% path_in
    for s in ('test', 'train'):
        for l in ('pos', 'neg'):
            path = path_in+'/%s/%s'%(s, l)
            for file in os.listdir(path):
                with open(os.path.join(path, file), 'r') as infile:
                    txt = infile.read()
                dfs[s] = dfs[s].append([[txt, labels[l]]], ignore_index=True)
                pbar.update()

    # Shuffle and save
    np.random.seed(0)
    if split_test_train:
        for s in ('test','train'):
            print '[INFO] Saving data to %s ....'% (path_out+'.'+s)
            dfs[s].columns = ['review', 'sentiment']
            dfs[s] = dfs[s].reindex(np.random.permutation(dfs[s].index))
            dfs[s].to_csv(path_out+'.'+s, index=False)
        return dfs['test'], dfs['train']
    else:
        print '[INFO] Saving data to %s ....'% path_out
        df = dfs['test'].append( dfs['train'], ignore_index=True )
        df = df.reindex(np.random.permutation(df.index))
        df.to_csv(path_out, index=False)
        return df

