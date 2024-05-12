#!python
# -*-coding:utf-8 -*-
'''
@File    :   ui.py
@Time    :   2023/07/10 10:42:13
@Author  :   sourcedream
@Contact :   admin@sourcedream.cn
@License :   (C)Copyright 2023, sourcedream
@Desc    :   None
'''

import pygame

class UI():
    def __init__(self):
        pygame.init()
        # clock = pygame.time.Clock()
        pygame.display.set_caption('XM Einstein Chess')
        self.main_window = pygame.display.set_mode((960, 540))
        self.main_window.fill((121, 128, 182))
        pygame.display.flip()
        # clock.tick(60)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # pygame.display.flip()
        pygame.quit()
# ui = UI()