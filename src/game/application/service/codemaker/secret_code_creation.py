#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""
from game.infrastructure.repositories.filesystem.game.game_repository import GameRepository


class SecretCodeCreation(object):

    def __init__(self):
        self.game_repository = GameRepository()

    def create(self, game_id, secret_code):
        game = self.game_repository.get_by_id(game_id)

        board = game.board

        board.secret_code = secret_code

        game.board = board

        self.game_repository.persist(game)
