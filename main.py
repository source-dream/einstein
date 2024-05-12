#!python
# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/07/10 10:41:17
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   程序主文件
'''

from Game import *
from Config import *
from Game.chess_manual import Manual

if __name__ == "__main__":
    GAME_MODE = get_config('setting', 'GAME_MODE')
    if GAME_MODE == 'train':
        TRAIN_TIME = get_config('train', 'TRAIN_TIME')
        for _ in range(int(TRAIN_TIME)):
            game = Game()
            game.init()
            game.start()
        print('训练完成')
    if GAME_MODE == 'game':
        game = Game()
        manual = Manual()
        red, blue = game.init()
        manual.createBoard(red, blue)
        team_first, winner, CI = game.start()
        manual.Save(winner, team_first, CI)
    if GAME_MODE == 'debug':
        pass