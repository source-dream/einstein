#!python
# -*-coding:utf-8 -*-
'''
@File    :   game.py
@Time    :   2023/07/10 10:41:57
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import random
from Config import *
from .role import get_move
import os
import time
from .sava_data import save_rate
from .chess_manual import Manual

class Board():
    def __init__(self):
        self.board = [[0] * 5 for _ in range(5)]
    def init(self, blue, red):
        pass
    def is_terminal(self, color, dice):
        if color == 'red':
            color = 'blue'
        else:
            color = 'red'
        if self.board[0][0] < 0 or self.board[4][4] > 0:
            return True
        if len(self.get_legalChess(color, dice)) == 0:
            return True
        return False

    def is_legalChess(self, move, legal_chess):
        if int(move[0]) in legal_chess:
            return True
        else:
            return False

    def get_legalChess(self, color, dice):
        if color == 'blue':
            dice = -dice
        legal_chess = []
        if any(dice in b for b in self.board):
            legal_chess.append(abs(dice))
        else:
            d = dice
            while abs(d) > 1:
                if color == 'red':
                    d -= 1
                else:
                    d += 1
                if any(d in b for b in self.board):
                    legal_chess.append(abs(d))
                    break
            while abs(dice) < 6:
                if color == 'red':
                    dice += 1
                else:
                    dice -= 1
                if any(dice in b for b in self.board):
                    legal_chess.append(abs(dice))
                    break
        return legal_chess

    def get_legal_move(self, legalChess, color):
        legal_move = []
        for chess in legalChess.copy():
            if color == 'blue':
                chess = -chess
            for i in range(5):
                for j in range(5):
                    if self.board[i][j] == chess:
                        if i > 0 and color == 'blue':
                            legal_move.append(str(abs(chess)) + '上')
                            if j > 0:
                                legal_move.append(str(abs(chess)) + '左上')
                        if i < 4 and color == 'red':
                            legal_move.append(str(abs(chess)) + '下')
                            if j < 4:
                                legal_move.append(str(abs(chess)) + '右下')
                        if j > 0 and color == 'blue':
                            legal_move.append(str(abs(chess)) + '左')
                        if j < 4 and color == 'red':
                            legal_move.append(str(abs(chess)) + '右')
        return legal_move

    def move(self, move, color):
        if color == 'red':
            chess = int(move[0])
        else:
            chess = -int(move[0])
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == chess:
                    if move[1:] == '上':
                        self.board[i][j] = 0
                        self.board[i - 1][j] = chess
                    elif move[1:] == '下':
                        self.board[i][j] = 0
                        self.board[i + 1][j] = chess
                    elif move[1:] == '左':
                        self.board[i][j] = 0
                        self.board[i][j - 1] = chess
                    elif move[1:] == '右':
                        self.board[i][j] = 0
                        self.board[i][j + 1] = chess
                    elif move[1:] == '右下':
                        self.board[i][j] = 0
                        self.board[i + 1][j + 1] = chess
                    elif move[1:] == '左上':
                        self.board[i][j] = 0
                        self.board[i - 1][j - 1] = chess
                    return chess


    def is_legalMove(self, move, color):
        if color == 'red':
            chess = int(move[0])
        else:
            chess = -int(move[0])
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == chess:
                    if move[1:] == '上' and color == 'blue':
                        if i < 1:
                            return False
                    elif move[1:] == '下' and color == 'red':
                        if i > 3:
                            return False
                    elif move[1:] == '左' and color == 'blue':
                        if j < 1:
                            return False
                    elif move[1:] == '右' and color == 'red':
                        if j > 3:
                            return False
                    elif move[1:] == '右下' and color == 'red':
                        if j > 3 and i > 3:
                            return False
                    elif move[1:] == '左上' and color == 'blue':
                        if i < 1 and j < 1:
                            return False
                    else:
                        return False
                    return True
        return False

    def print_board(self):
        print('\033c')
        print('当前棋盘状态如下\n')
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


class Game(Board):

    def __init__(self):
        super().__init__()
        self.CI = []
        self.red = []
        self.blue = []
        self.team_now = None
        self.color = 'red'
        self.dice_now = None
        self.legalChess = None
        self.chess = None
        self.legal_move = None
        self.team = {'team1': get_config('game', 'TEAM1'), 'team2': get_config('game', 'TEAM2')}
        self.team_name = {'team1': get_config('info', 'TEAM1'), 'team2': get_config('info', 'TEAM2')}

    def init(self):
        INIT_MODE = get_config('setting', 'INIT_MODE')
        if INIT_MODE == 'random':
            self.red = [1, 2, 3, 4, 5, 6]
            self.blue = [-1, -2, -3, -4, -5, -6]
            random.shuffle(self.red)
            random.shuffle(self.blue)
        elif INIT_MODE == 'input':
            red1 = 0
            blue1 = 0
            while True:
                print("请输入红方顺序[1,2,3,4,5,6]")
                for i in range(6):
                    self.red.append(int(input()))
                    red1 += 1
                if red1 != 6:
                    print('输入错误')
                elif red1 == 6:
                    break
            while True:
                print("请输入蓝方顺序[1,2,3,4,5,6]")
                for i in range(6):
                    self.blue.append(-int(input()))
                    blue1 += 1
                if blue1 != 6:
                    print('输入错误')
                elif red1 == 6:
                    break
        index = 0
        for i in range(3):
            for j in range(3 - i):
                self.board[i][j] = self.red[index]
                index += 1
        index = 0
        temp = 0
        for i in range(2, 5):
            for j in range(4 - temp, 5):
                self.board[i][j] = self.blue[index]
                index += 1
            temp += 1
        self.print_board()
        return [self.red, self.blue]

    def rollDice(self):
        DICE_MODE = get_config('setting', 'DICE_MODE')
        if DICE_MODE == 'random':
            self.dice_now = random.randint(1, 6)
        elif DICE_MODE == 'input':
            self.dice_now = int(input('请输入骰子数: '))
        else:
            print('队伍初始化配置错误,请检查文件后重新运行')
            exit(0)

    def init_team(self):
        TEAM_MODE = get_config('setting', 'TEAM_MODE')
        if TEAM_MODE == 'random':
            self.team_now = random.choice(['team1', 'team2'])
        elif TEAM_MODE == 'input':
            self.team_now = input('请输入先手队伍[team1]或[team2]')
        else:
            print('队伍初始化配置错误,请检查文件后重新运行')
            exit(0)
        print(f'本轮比赛 {self.team_now}({self.color})[{self.team[self.team_now]}] 先手\n')
        return self.team_now

    def round(self):
        if self.color == 'red':
            self.color = 'blue'
        else:
            self.color = 'red'
        if self.team_now == 'team1':
            self.team_now = 'team2'
        else:
            self.team_now = 'team1'

    def start(self):
        team_first = self.init_team()
        manual = Manual()
        while True:
            self.rollDice()
            self.legalChess = self.get_legalChess(self.color, self.dice_now)
            self.legal_move = self.get_legal_move(self.legalChess, self.color)
            print(f'当前骰子数: {self.dice_now} 你可移动的棋子: {self.legalChess}\n当前可移动的方法: {self.legal_move}\n')
            while True:
                move = get_move(self.team[self.team_now], self.legal_move, self.board, self.color, self.dice_now)
                while not move[0].isdigit():
                    print('棋子不合法, 请重试')
                    move = get_move(self.team[self.team_now])
                if self.is_legalChess(move, self.legalChess):
                    if self.is_legalMove(move, self.color):
                        break
                    else:
                        print('移动不合法, 请重试')
                else:
                    print('棋子不合法, 请重试')

            self.chess = self.move(move, self.color)
            self.CI = manual.appendCI(self.board, self.chess, self.dice_now)
            if self.is_terminal(self.color, self.dice_now):
                self.print_board()
                print(f'本局比赛 {self.team_now}<{self.team_name[self.team_now]}>({self.color})[{self.team[self.team_now]}] 获胜\n')
                # time.sleep(2)
                if self.team_now == 'team1':
                    result = True
                else:
                    result = False
                save_rate(self.team['team1'], self.team['team2'], result)
                return team_first, self.team_name[self.team_now], self.CI
            else:
                self.round()
                self.print_board()
                print(
                    f'本回合是 {self.team_now}<{self.team_name[self.team_now]}>({self.color})[{self.team[self.team_now]}] 回合\n')


