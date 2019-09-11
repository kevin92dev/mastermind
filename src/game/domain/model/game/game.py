#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import uuid


class Game(object):

    PEGS = {
        0: 'BLANK',
        1: 'RED',
        2: 'BLUE',
        3: 'GREEN',
        4: 'YELLOW',
        5: 'PURPLE',
        6: 'ORANGE'
    }

    def __init__(self, board):
        self.id = uuid.uuid1()
        self.board = board
        self.attempts = None

    def to_json(self):
        return {
            'id': self.id,
            'game': self.board.to_json(),
            'attempts': self.attempts.to_json()
        }
