#!python
# -*-coding:utf-8 -*-
'''
@File    :   random.py
@Time    :   2023/07/10 10:43:13
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import random

def get_move_random(legal_move):
    return random.choice(legal_move)