# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            raise InternalServerError(e)
