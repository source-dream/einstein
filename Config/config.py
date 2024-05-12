#!python
# -*-coding:utf-8 -*-
'''
@File    :   config.py
@Time    :   2023/07/10 10:43:21
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import configparser
import os

def get_config(section_name, option_name):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'ai.ini'), encoding='utf-8')
    config.read(os.path.join(os.path.dirname(__file__), 'game.ini'), encoding='utf-8')
    return config.get(section_name, option_name).split('#')[0].strip()