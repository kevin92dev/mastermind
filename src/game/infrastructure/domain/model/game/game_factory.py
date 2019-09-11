#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from game.domain.model.game.game import Game
from game.domain.model.game.game_factory import IGameFactory


class GameFactory(IGameFactory):

    def create(self, board):
        return Game(board=board)
