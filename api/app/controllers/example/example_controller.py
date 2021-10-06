# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel
from app import db
import json

class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': False,
                'message': "No se encontraron modelos",
                'data':[]
            }
            modelos = db.session.query(ExampleModel).all()
            response['ok']=True
            if len(modelos)>0:
                response['message'] = 'Consulta exitosa'
                for modelo in modelos:
                    temp = {
                        "id" : modelo.id,
                        "name" : modelo.name,
                        "description" : modelo.description,
                        "status" : modelo.status
                    }
                    response['data'].append(temp)
            else:
                response['message'] = 'No se encontraron modelos'
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
    
    @staticmethod
    def detail(id):
        try:
            response = {
                'status': False,
                'message': "No se encontraron modelos con este id",
                'data':{}
            }
            objeto = db.session.query(ExampleModel).filter_by(id=id).first()
            if objeto:
                response['status'] = True
                response['message'] = "Consulta exitosa"
                response['data'] = {
                        "id" : objeto.id,
                        "name" : objeto.name,
                        "description" : objeto.description,
                        "status" : objeto.status
                    }
            else:
                response['status'] = True
                response['message'] = "No se encontraron registros con este id"
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    # @staticmethod
    # def create():
    #     try:
    #         response = {
    #             'ok': True,
    #             'message': 'Response OK, method get_index'
    #         }
    #         return response
    #     except Exception as e:
    #         print('Error: {er}'.format(er=e))
    #         raise InternalServerError(e)
    
    # @staticmethod
    # def edit():
    #     try:
    #         response = {
    #             'ok': True,
    #             'message': 'Response OK, method get_index'
    #         }
    #         return response
    #     except Exception as e:
    #         print('Error: {er}'.format(er=e))
    #         raise InternalServerError(e)

    @staticmethod
    def delete(id):
        try:
            try:
                response = {
                    'ok': True,
                    'message': 'Response OK, method get_index'
                }
                objeto = db.session.query(ExampleModel).filter_by(id=id).first()
                if objeto:
                    objeto.delete()
                    response['status'] = True
                    response['message'] = "Se eliminó el registro exitosamente"
                else:
                    response['status'] = True
                    response['message'] = "No se encontraron registros con este id"
            except:
                response = {
                    'ok': False,
                    'message': 'Error'
                }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)
