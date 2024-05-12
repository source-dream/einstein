#!python
# -*-coding:utf-8 -*-
'''
@File    :   killer.py
@Time    :   2023/07/10 13:46:59
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import random

def get_move_killer(legal_move, board, color):
    
    for move in legal_move:
        if color == 'blue':
            chess = -int(move[0])
        else:
            chess = int(move[0])
        for i in range(5):
            for j in range(5):
                if chess == board[i][j]:
                    if move[1:] == '上':
                        if i > 0:
                            if board[i-1][j] > 0:
                                return move
                    if move[1:] == '下':
                        if i < 4:
                            if board[i+1][j] < 0:
                                return move
                    if move[1:] == '左':
                        if j > 0:
                            if board[i][j-1] > 0:
                                return move
                    if move[1:] == '右':
                        if j < 4:
                            if board[i][j+1] < 0:
                                return move
                    if move[1:] == '左上':
                        if i > 0 and j > 0:
                            if board[i-1][j-1] > 0:
                                return move
                    if move[1:] == '右下':
                        if i < 4 and j < 4:
                            if board[i+1][j+1] < 0:
                                return move
    return random.choice(legal_move)