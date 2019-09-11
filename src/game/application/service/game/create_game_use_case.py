#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from game.infrastructure.domain.model.board.board_factory import BoardFactory
from game.infrastructure.domain.model.game.game_factory import GameFactory
from game.infrastructure.repositories.filesystem.game.game_repository import GameRepository


class CreateGameUseCase(object):

    def __init__(self):
        self.game_factory = GameFactory()
        self.game_repository = GameRepository()
        self.board_factory = BoardFactory()

    def create(self):
        board = self.board_factory.create()

        game = self.game_factory.create(board=board)

        self.game_repository.persist(game=game)

        return game
