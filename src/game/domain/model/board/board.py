#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""


class Board(object):

    def __init__(self):
        self.secret_code = None

    def to_json(self):
        return {
            'secret_code': self.secret_code
        }
