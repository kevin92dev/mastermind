#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2019
"""


class ApiResponse(object):

    def __init__(self, status=False, data=None, error_message=None):
        self.status = status
        self.data = data
        self.error_message = error_message

    def to_json(self):
        return {
            'status': self.status,
            'data': self.data,
            'error_message': self.error_message
        }
