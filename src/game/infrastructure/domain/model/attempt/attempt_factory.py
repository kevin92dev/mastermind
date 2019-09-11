#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from game.domain.model.attempt.attempt import Attempt
from game.domain.model.attempt.attempt_factory import IAttemptFactory


class AttemptFactory(IAttemptFactory):

    def create(self, board, guess_code):
        return Attempt(board=board, code=guess_code)
