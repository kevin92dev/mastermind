#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from game.infrastructure.repositories.filesystem.game.game_repository import GameRepository


class GetGameHistoryUseCase(object):

    def __init__(self):
        self.game_repository = GameRepository()

    def get_history(self, game_id):
        game = self.game_repository.get_by_id(game_id=game_id)

        return {
            'num_of_attempts': len(game.attempts),
            'attempts': game.attempts
        }
