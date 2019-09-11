#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from board.domain.model.board_repository import IBoardRepository
from board.domain.model.cannot_save_board_exception import CannotSaveBoardException
from board.domain.model.cannot_read_board_exception import CannotReadBoardException


class BoardRepository(IBoardRepository):

    def persist(self, board):
        try:
            file = open('/tmp/' + board.board_id + '.txt', 'a')
            file.write(board.to_json)
            file.close()
        except Exception:
            raise CannotSaveBoardException()

    def get_by_id(self, board_id):
        try:
            file = open('/tmp/' + board_id + '.txt', 'r')
            data = file.readlines()
            file.close()

            return data
        except Exception:
            raise CannotReadBoardException()
