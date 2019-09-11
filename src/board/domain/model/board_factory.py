#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import abc


class IBoardFactory(abc.ABC):

    @abc.abstractmethod
    def create(self):
        pass
