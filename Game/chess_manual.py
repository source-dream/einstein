#!python
# -*-coding:utf-8 -*-
'''
@File    :   chess_manual.py
@Time    :   2023/07/10 10:42:21
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''


import os
import numpy
import time
from Config import *



class Manual:
    def __init__(self):
        self.blue = [-1, -2, -3, -4, -5, -6]
        self.red = [1, 2, 3, 4, 5, 6]
        self.board = [[0] * 5 for _ in range(5)]  # 初始化真实棋盘
        self.PI = []
        self.CI = []
        self.RCSS = []  # 红色棋子初始设定
        self.BCSS = []

    def createBoard(self, red, blue):  # 新建棋盘，传入红蓝两个参数，就是新棋盘开始时候的布局
        self.RCSS = ['R:']
        self.BCSS = ['B:']
        self.board = [[0] * 5 for _ in range(5)]
        self.board[0][0] = red[0]
        self.RCSS.append('A5-')
        self.RCSS.append(str(int(red[0])))
        self.RCSS.append(';')
        self.board[0][1] = red[1]
        self.RCSS.append('B5-')
        self.RCSS.append(str(int(red[1])))
        self.RCSS.append(';')
        self.board[0][2] = red[2]
        self.RCSS.append('C5-')
        self.RCSS.append(str(int(red[2])))
        self.RCSS.append(';')
        self.board[1][0] = red[3]
        self.RCSS.append('A4-')
        self.RCSS.append(str(int(red[3])))
        self.RCSS.append(';')
        self.board[1][1] = red[4]
        self.RCSS.append('B4-')
        self.RCSS.append(str(int(red[4])))
        self.RCSS.append(';')
        self.board[2][0] = red[5]
        self.RCSS.append('A3-')
        self.RCSS.append(str(int(red[5])))
        self.RCSS.append(';')
        self.board[2][4] = -abs(blue[0])
        self.BCSS.append('E3-')
        self.BCSS.append(str(int(abs(blue[0]))))
        self.BCSS.append(';')
        self.board[3][3] = -abs(blue[1])
        self.BCSS.append('D2-')
        self.BCSS.append(str(int(abs(blue[1]))))
        self.BCSS.append(';')
        self.board[3][4] = -abs(blue[2])
        self.BCSS.append('E2-')
        self.BCSS.append(str(int(abs(blue[2]))))
        self.BCSS.append(';')
        self.board[4][2] = -abs(blue[3])
        self.BCSS.append('C1-')
        self.BCSS.append(str(int(abs(blue[3]))))
        self.BCSS.append(';')
        self.board[4][3] = -abs(blue[4])
        self.BCSS.append('D1-')
        self.BCSS.append(str(int(abs(blue[4]))))
        self.BCSS.append(';')
        self.board[4][4] = -abs(blue[5])
        self.BCSS.append('E1-')
        self.BCSS.append(str(int(abs(blue[5]))))
        self.BCSS.append(';')
        self.PI.append(list(numpy.array(self.board).reshape(25)))

    def appendCI(self, board, chess, rand):
        x = y = -1
        for i in range(5):
            for j in range(5):
                if board[i][j] == chess:
                    x = i
                    y = j
        chess = board[x][y]
        if chess > 0:
            chess = 'R' + str(chess)
        else:
            chess = 'B' + str(-chess)
        x = str(5 - x)
        if y == 0:
            y = 'A'
        elif y == 1:
            y = 'B'
        elif y == 2:
            y = 'C'
        elif y == 3:
            y = 'D'
        elif y == 4:
            y = 'E'
        self.CI.append(':' + str(abs(rand)) + ';(' + chess + ',' + str(y) + str(x) + ')')
        return self.CI

    def Save(self, winner, team_now, CI):
        if team_now == 'team1':
            team_now = get_config('info', 'TEAM1')
        else:
            team_now = get_config('info', 'TEAM2')
        Team1 = team_now
        Team = [get_config('info', 'TEAM1'), get_config('info', 'TEAM2')]
        Team.remove(team_now)
        Team2 = Team[0]
        Location = get_config('info', 'GAME_NAME')
        Name = get_config('info', 'GAME_LOCATION')
        if winner == team_now:
            Winner = '先手胜'
        elif winner != team_now:
            Winner = '后手胜'
        dir_name = './Data/ChessManual/'

        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        FileName = dir_name + 'WTN' + '-' + Team1 + ' ' + 'vs' + ' ' + Team2 + '-' + Winner + ' ' + time.strftime(
            "%Y%m%d%H%M",
            time.localtime()) + '.txt'
        Text1 = '#[' + Team1 + '][' + Team2 + '][' + time.strftime("%Y.%m.%d %H:%M",
                                                                   time.localtime()) + ' ' + Location + '][' + Name + '];'
        File = open(FileName, 'w')
        File.write(Text1)
        File.write('\r')
        for RC in self.RCSS:
            File.write(RC)
        File.write('\r')
        for BC in self.BCSS:
            File.write(BC)
        File.write('\r')
        for Step in range(len(CI)):
            File.write(str(Step + 1))
            File.write(CI[Step])
            File.write('\r')
        File.close()