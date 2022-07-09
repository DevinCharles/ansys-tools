#!/usr/bin/python

import re
import numpy as np

def parse(data,item):
    '''
    data:    text read from ascii fluent .msh file
    item:    type to parse: nodes, cells, faces
    '''
    rgx = '(?:\(\('+num+'.*\)\(\n((?:.*\n)+?)\)\))+'

    if item=='nodes':
        n = '10'
        f = float
    elif item=='faces':
        n = '13'
        f = lambda x:int(x,16)
    elif item=='cells':
        n = '12'
        f = lambda x:int(x,16)

    m = re.findall(rgx,data,re.MULTILINE)
    p = [[[f(v) for v in row.strip().split(' ')] for row in group.strip().split('\n')] for group in m]

    return p
