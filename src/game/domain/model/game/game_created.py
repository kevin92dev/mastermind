#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import datetime


class GameCreated(object):

    def __init__(self, game_id):
        self.game_id = game_id
        self.occurred_on = datetime.datetime.now()
