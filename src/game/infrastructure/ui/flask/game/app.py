#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from flask import Flask

from game.infrastructure.ui.flask.api_response import ApiResponse
from game.application.service.game.create_game_use_case import CreateGameUseCase
from game.domain.model.game.cannot_read_game_exception import CannotReadGameException
from game.domain.model.game.cannot_save_game_exception import CannotSaveGameException

JSON_CONTENT_TYPE = 'application/json'
app = Flask(__name__)


@app.route("/game/new", methods=["POST"])
def create_game():
    status = False
    result_data = None
    error_message = None

    try:
        game = CreateGameUseCase().create()

        result_data = {
            'game_id': game.id
        }

        status = True
    except CannotSaveGameException as e:
        error_message = e.MESSAGE
    except CannotReadGameException as e:
        error_message = e.MESSAGE
    except Exception as e:
        error_message = str(e)

    api_response = ApiResponse(
        status,
        result_data,
        error_message
    )

    return api_response.to_json()
