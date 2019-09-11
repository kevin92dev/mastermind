#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from flask import Flask, request

from game.infrastructure.ui.flask.api_response import ApiResponse
from game.domain.model.game.cannot_save_game_exception import CannotSaveGameException
from game.domain.model.game.cannot_read_game_exception import CannotReadGameException
from game.application.service.codemaker.secret_code_creation import SecretCodeCreation

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


@app.route("/codemaker/generate_secret_code", methods=["POST"])
def create_secret_code():
    status = False
    result_data = None
    error_message = None

    try:
        data = get_data_from_request(request)

        game_id = str(request.headers.get('game_id'))

        SecretCodeCreation().create(
            game_id=game_id,
            secret_code=data['secret_code']
        )

        status = True
    except CannotReadGameException as e:
        error_message = e.MESSAGE
    except CannotSaveGameException as e:
        error_message = e.MESSAGE

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
