#!/usr/bin/env python
import os, re, sys, shutil

#import nbformat as nbf
from nbformat import v3, v4
from optparse import OptionParser

usage = """
  Usage: """+sys.argv[0]+""" --inpy test.py  
  For more help: """+sys.argv[0]+""" --help 
 """

parser = OptionParser(usage=usage)
parser.add_option("-i", "--inpy", dest="inpy", default='', 
                          help="Input .py file")
parser.add_option("-o", "--outPath", dest="outpath", default='.',  
                          help="Output .ipynb path")
(options, args) = parser.parse_args()

if options.inpy == '':
    print usage
    sys.exit()

outipy = options.outpath + '/'+options.inpy.replace(".py",".ipynb").rsplit("/", 1)[1]   

with open(options.inpy) as fpin:
        text = fpin.read()

nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)

jsonform = v4.writes(nbook) + "\n"
with open(outipy, "w") as fpout:
        fpout.write(jsonform)

print 'Generated '+outipy 

#nb = nbf.read(open(options.inpy, 'r'), 'py')
#nbf.write(nb, open(options.outipy, 'w'), 'ipynb')
