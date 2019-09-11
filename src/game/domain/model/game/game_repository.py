#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import abc


class IGameRepository(abc.ABC):

    @abc.abstractmethod
    def persist(self, game):
        pass

    @abc.abstractmethod
    def get_by_id(self, game_id):
        pass
