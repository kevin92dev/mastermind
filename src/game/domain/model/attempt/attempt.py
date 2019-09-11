#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import datetime
import numpy as np


class Attempt(object):

    def __init__(self, board, code):
        self.board = board
        self.code = code
        self.occurred_on = datetime.datetime.now()

    def get_feedback(self):
        pass

    def get_secret_code(self):
        return self.board.secret_code

    def to_json(self):
        return {
            'guessed': np.array_equal(self.get_secret_code(), self.code),
            'secret_code': self.get_secret_code(),
            'code': self.code,
            'feedback': self.get_feedback(),
            'occurred_on': self.occurred_on.strftime("%d/%m/%Y %H:%M:%S")
        }
