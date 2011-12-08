#!/usr/bin/env python
# encoding: utf-8
"""
trivial_pursuit.py

Created by Christopher K. Lee on 2011-12-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

from trivialpursuitfunctions import *
from questions import *
from scoring import *
from weights import *
from determine import *
from output import *
from test import *
from importcache import *

def update():
    reload(trivialpursuitfunctions)
    reload(questions)
    reload(scoring)
    reload(weights)
    reload(determine)
    reload(output)
    reload(test)