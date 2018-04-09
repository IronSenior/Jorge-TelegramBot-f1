# -*-coding:utf-8 -*-
# !/usr/bin/env python

import json
from constantes import db_path


def ranking(cid):
    path = db_path+str(cid)
    lst = []
    with open('%s/rank.json' % path, 'r') as rank:
        dct = json.load(rank)
        for key in dct:
            lst.append((key, dct[key]))
    ranklst = []
    while len(lst) > 0:
        bigger = 0
        for elem in lst:
            if elem[1] > bigger:
                bigger = elem[1]
        for elem in lst:
            if elem[1] == bigger:
                ranklst.append(elem)
                lst.remove(elem)
    return ranklst
