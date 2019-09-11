#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from board.infrastructure.domain.model.board_factory import BoardFactory
from board.infrastructure.repositories.filesystem.board_repository import BoardRepository


class BoardCreation(object):

    def __init__(self):
        self.board_factory = BoardFactory()
        self.board_repository = BoardRepository()

    def create(self):
        board = self.board_factory.create()
        self.board_repository.persist(board)

        return {
            'board_id': board.id
        }
