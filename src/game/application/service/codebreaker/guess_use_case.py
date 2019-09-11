#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""
from game.infrastructure.domain.model.attempt.attempt_factory import AttemptFactory
from game.infrastructure.repositories.filesystem.game.game_repository import GameRepository


class GuessUseCase(object):

    def __init__(self):
        self.game_repository = GameRepository()
        self.attempt_factory = AttemptFactory()

    def check(self, game_id, guess_code):
        game = self.game_repository.get_by_id(game_id)

        attempt = self.attempt_factory.create(board=game.board, guess_code=guess_code)

        game.attempts.append(attempt)

        self.game_repository.persist(game)

        return {
            'feedback': attempt.get_feedback(),
            'num_of_attempts': len(game.attempts)
        }
