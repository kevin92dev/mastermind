#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

import json
from game.domain.model.game.game_repository import IGameRepository
from game.domain.model.game.cannot_read_game_exception import CannotReadGameException
from game.domain.model.game.cannot_save_game_exception import CannotSaveGameException


class GameRepository(IGameRepository):

    def __init__(self):
        self.root_folder = '/tmp'

    def persist(self, game):
        try:
            file = open(self.root_folder + '/' + game.id + '.txt', 'w')

            content = self.serialize_to_json(game.to_json())

            file.write(content)

            file.close()
        except Exception:
            raise CannotSaveGameException()

    def get_by_id(self, game_id):
        try:
            file = open(self.root_folder + '/' + game_id + '.txt', 'r')

            json_content = file.readlines()

            file.close()

            deserialized_object = self.deserialize(json_content)

            return deserialized_object
        except Exception:
            raise CannotReadGameException()

    def serialize_to_json(self, data):
        return json.dumps(data)

    def deserialize(self, data):
        return json.loads(data)
