#!python
# -*-coding:utf-8 -*-
'''
@File    :   role.py
@Time    :   2023/07/10 10:42:03
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

from AI import *

def get_move(role, legal_move, board, color, dice):
    if role == 'people':
        return get_move_people()
    elif role == 'random':
        return get_move_random(legal_move)
    elif role == 'lucky':
        return get_move_lucky(legal_move)
    elif role == 'killer':
        return get_move_killer(legal_move, board, color)
    elif role == 'cmcts':
        return get_move_cmcts(board, color, dice)
    else:
        print('ai配置文件错误')