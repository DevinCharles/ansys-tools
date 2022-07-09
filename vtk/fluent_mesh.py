#!/usr/bin/python

import re

def parse(data,item):
    '''
    data:    text read from ascii fluent .msh file
    item:    type to parse: nodes, cells, faces
    '''

    if item=='nodes':
        n = '10'
        f = float
    elif item=='faces':
        n = '13'
        f = lambda x:int(x,16)-1
    elif item=='cells':
        n = '12'
        f = lambda x:int(x,16)

    rgx = '(?:\('+n+'.*\)\(\n((?:.*\n)+?)\)\))+'
    m = re.findall(rgx,data,re.MULTILINE)
    p = [[[f(v) for v in row.strip().split(' ')] for row in group.strip().split('\n')] for group in m]

    if item == 'nodes':
        return p[0]
    elif item == 'faces':
        return [[len(f[0])-2]+f[0][0:-2] for f in p]
    elif item == 'cells':
        return p
