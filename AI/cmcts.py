#!python
# -*-coding:utf-8 -*-
'''
@File    :   cmcts.py
@Time    :   2023/07/10 10:42:42
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import copy
from Config import *
import math
import time
import random

COF = get_config('cmcts', 'COF')

class Node():
    def __init__(self, board, color, dice, move=None, parent=None):
        self.board = board
        self.color = color
        self.dice = dice
        self.parent = parent
        self.pre_move = move
        self.children = []
        self.visit_times = 10
        self.win_times = 0.0
    def get_ucb(self):
        return self.win_times/(self.visit_times + 1e-6) + float(COF) * math.sqrt((2 * math.log(self.parent.visit_times)) / (self.visit_times + 1e-6))
    def is_terminal(self):
        if self.board[0][0] < 0 or self.board[4][4] > 0:
            return True
        red = []
        blue = []
        for i in range(5):
            for j in range(5):
                if self.board[i][j] > 0:
                    red.append(self.board[i][j])
                if self.board[i][j] < 0:
                    blue.append(self.board[i][j])
        if not blue or not red:
            return True
        return False
    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False
    def is_expend(self):
        if self.is_terminal():
            return False
        return True
    def select(self):
        ucb_max = -1.0
        node_select = None
        for n in self.children:
            if not n.visit_times:
                return n
            else:
                ucb = n.get_ucb()
                if  ucb > ucb_max:
                    ucb_max = ucb
                    node_select = n
        return node_select
    def round(self):
        if self.color == 'red':
            self.color = 'blue'
        else:
            self.color = 'red'
    def get_legal_chess(self):
        if self.color == 'blue':
            self.dice = -self.dice
        legal_chess = [] 
        if any(self.dice in b for b in self.board):
            legal_chess.append(abs(self.dice))
        else:
            count = 0
            while ( self.dice - count ) >= 1 and ( self.dice - count ) <= 6:
                if any((self.dice - count) in b for b in self.board):
                    legal_chess.append(abs(self.dice - count))
                    break
                count += 1
            count = 0
            while ( self.dice + count ) >= 1 and ( self.dice + count ) <= 6:
                if any((self.dice + count) in b for b in self.board):
                    legal_chess.append(abs(self.dice + count))
                    break
                count += 1
            count = 0
            while ( self.dice - count ) >= -6 and ( self.dice - count ) <= -1:
                if any((self.dice - count) in b for b in self.board):
                    legal_chess.append(abs(self.dice - count))
                    break
                count += 1
            count = 0
            while ( self.dice + count ) >= -6 and ( self.dice + count ) <= -1:
                if any((self.dice + count) in b for b in self.board):
                    legal_chess.append(abs(self.dice + count))
                    break
                count += 1
        self.dice = abs(self.dice)
        return legal_chess
    def get_legal_move(self, legal_chess):
        legal_move = []
        for chess in legal_chess.copy():
            if self.color == 'blue':
                chess = -chess
            for i in range(5):
                for j in range(5):
                    if self.board[i][j] == chess:
                        if self.color == 'red':
                            if i < 4:
                                legal_move.append(str(abs(chess))+'下')
                            if j < 4:
                                legal_move.append(str(abs(chess))+'右')
                            if i < 4 and j < 4:
                                legal_move.append(str(abs(chess))+'右下')
                        if self.color == 'blue':
                            if i > 0:
                                legal_move.append(str(abs(chess))+'上')
                            if j > 0:
                                legal_move.append(str(abs(chess))+'左')
                            if i > 0 and j < 0:
                                legal_move.append(str(abs(chess))+'左上')
        return legal_move
    def move(self):
        if self.color == 'red':
            chess = int(self.pre_move[0])
        else:
            chess = -int(self.pre_move[0])
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == chess:
                    if self.pre_move[1:] == '上':
                        self.board[i][j] = 0
                        self.board[i-1][j] = chess
                    elif self.pre_move[1:] == '下':
                        self.board[i][j] = 0
                        self.board[i+1][j] = chess
                    elif self.pre_move[1:] == '左':
                                self.board[i][j] = 0
                                self.board[i][j-1] = chess
                    elif self.pre_move[1:] == '右':
                                self.board[i][j] = 0
                                self.board[i][j+1] = chess
                    elif self.pre_move[1:] == '右下':
                                self.board[i][j] = 0
                                self.board[i+1][j+1] = chess
                    elif self.pre_move[1:] == '左上':
                                self.board[i][j] = 0
                                self.board[i-1][j-1] = chess
                    return
    def expend(self, color):
        legal_chess = self.get_legal_chess()
        legal_move = self.get_legal_move(legal_chess)
        for move in legal_move:
            for _ in range(1,7):
                n = Node(copy.deepcopy(self.board), self.color, _, move, parent=self)
                n.move()
                n.round()
                self.children.append(n)
        for node in self.children:
            color_win = node.simulate()
            node.backup(color, color_win)
    def rollDice(self):
        self.dice = random.randint(1,6)
    def simulate(self):
        node = copy.deepcopy(self)
        while not node.is_terminal():
            legal_move = node.get_legal_move(node.get_legal_chess())
            node.pre_move = random.choice(legal_move)
            node.move()
            if node.is_terminal():
                break
            else:
                node.rollDice()
                node.round()
        return node.color
    def backup(self, color, color_win):
        node = self
        while node.parent != None:
            if color_win == color:
                node.win_times += 1
            node.visit_times += 1
            node = node.parent
    def print_board(self):
        board = '' 
        for i in range(5):
            for j in range(5):
                if int(self.board[i][j]) < 0:
                    board += f'\033[44m {abs(self.board[i][j])} \033[0m'
                elif (self.board[i][j]) > 0:
                    board += f'\033[41m {self.board[i][j]} \033[0m'
                else:
                    board += "\033[47m   \033[0m"
            board += "\n"
        print(board)
def get_move_cmcts(board, color, dice):
    search_size = int(get_config('cmcts', 'SEARCH_SIZE'))
    SEARCH_SIZE = search_size
    root = Node(board, color, dice)
    start = time.perf_counter()
    while search_size:
        print("\r", end="")
        print("search progress: {}%: [{}{}]{:.2f}s".format(int(((SEARCH_SIZE-search_size)/SEARCH_SIZE)*100), "▋" * (int(((SEARCH_SIZE-search_size)/SEARCH_SIZE)*100) // 2), " " * (50-(int(((SEARCH_SIZE-search_size)/SEARCH_SIZE)*100) // 2)), time.perf_counter() - start), end="")
        node = root
        while not node.is_leaf():
            node = node.select()
        if node.is_expend():
            node.expend(color)
        search_size -= 1
    max_ucb = -0.1
    for n in root.children:
        ucb = n.get_ucb()
        if ucb > max_ucb:
            max_ucb = ucb
            node = n
    return node.pre_move