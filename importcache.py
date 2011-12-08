#!/usr/bin/env python
# encoding: utf-8
"""
readin.py

Created by Christopher K. Lee on 2011-12-08.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

def readCache(INDEX):
    
    f = open('cache/nltk{}.txt'.format(INDEX), 'r')
    raw = f.readlines()
    f.close

    nltk_data=[]
    for i in xrange (0,6):
        nltk_data.append(eval(raw[i]))
    
    return nltk_data
    
