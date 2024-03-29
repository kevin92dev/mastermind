#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from flask import Flask, request
from game.infrastructure.ui.flask.api_response import ApiResponse
from game.application.service.codebreaker.guess_use_case import GuessUseCase
from game.domain.model.game.cannot_save_game_exception import CannotSaveGameException
from game.domain.model.game.cannot_read_game_exception import CannotReadGameException

JSON_CONTENT_TYPE = 'application/json'
app = Flask(__name__)


@app.before_request
def check_game_identifier():
    game_id = str(request.headers.get('game_id'))

    if game_id is not None:
        return None

    return ApiResponse(
        False,
        None,
        "Error: Header game_id not found."
    )


@app.route("/codebreaker/guess", methods=["POST"])
def create_secret_code():
    status = False
    result_data = None
    error_message = None

    try:
        data = get_data_from_request(request)

        game_id = str(request.headers.get('game_id'))

        GuessUseCase().check(
            game_id=game_id,
            guess_code=data['code']
        )

        status = True
    except CannotReadGameException as e:
        error_message = e.MESSAGE
    except CannotSaveGameException as e:
        error_message = e.MESSAGE
    except Exception as e:
        error_message = str(e)

    api_response = ApiResponse(
        status,
        result_data,
        error_message
    )

    return api_response.to_json()


def get_data_from_request(request):
    content_type = str(request.headers.get('Content-Type'))

    if JSON_CONTENT_TYPE == content_type:
        return request.get_json(force=True)

    return request.data
