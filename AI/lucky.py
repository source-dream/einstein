#!python
# -*-coding:utf-8 -*-
'''
@File    :   lucky.py
@Time    :   2023/07/10 13:18:56
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import random

def get_move_lucky(legal_move):
    for move in legal_move:
        if '左上' in move:
            return move
        if '右下' in move:
            return move
    return random.choice(legal_move)