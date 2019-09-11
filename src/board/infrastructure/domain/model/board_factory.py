#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from board.domain.model.board import Board
from board.domain.model.board_factory import IBoardFactory


class BoardFactory(IBoardFactory):

    def create(self):
        return Board()
