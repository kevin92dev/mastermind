#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""

from flask import Flask, request
from common.infrastructure.ui.api_response import ApiResponse
from board.application.service.board_creation import BoardCreation
from board.domain.model.cannot_save_board_exception import CannotSaveBoardException
from board.domain.model.cannot_read_board_exception import CannotReadBoardException

JSON_CONTENT_TYPE = 'application/json'
app = Flask(__name__)


@app.route("/board", methods=["POST"])
def create_game():
    status = False
    result_data = None
    error_message = None

    try:
        result_data = BoardCreation().create()
        status = True
    except CannotSaveBoardException as e:
        error_message = e.MESSAGE
    except CannotReadBoardException as e:
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
