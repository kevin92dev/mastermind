#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import abc


class IBoardRepository(abc.ABC):

    @abc.abstractmethod
    def persist(self, board):
        pass

    @abc.abstractmethod
    def get_by_id(self, board_id):
        pass
