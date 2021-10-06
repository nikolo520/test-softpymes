# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from flask.globals import session
from app.exception import InternalServerError
from app.models import ExampleModel
from app import db
import json

class ExampleController:

    @staticmethod
    def get_index():
        response = {
            'status': False,
            'message': "No se encontraron registros",
            'data':[]
        }
        try:
            
            modelos = db.session.query(ExampleModel).all()
            response['status']=True
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
            
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 1)",
            }
        return response
    
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
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 2)",
            }
        return response

    @staticmethod
    def create(form):
        try:
            objeto = ExampleModel(
                name=form['name'],
                identification=form['identification'],
                description=form['description'],
                status=True
                )
            objeto.save()
            response = {
                'status': True,
                'message': 'Regitro creado exitosamente'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 3)",
            }
        return response
    
    @staticmethod
    def edit(id,form):
        response = {
            'status': False,
            'message': "No se encontraron modelos",
        }
        try:
            
            objeto = db.session.query(ExampleModel).filter_by(id=id).first()
            if objeto:
                objeto.update(
                    name=form['name'],
                    identification=form['identification'],
                    description=form['description'],
                    status=form['status']
                    )
                objeto.save()
                response = {
                    'status': True,
                    'message': 'Regitro creado exitosamente'
                }
            else:
                response['status'] = True
                response['message'] = "No se encontraron registros con este id"
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 4)",
            }
        return response

    @staticmethod
    def delete(id):
        try:
            try:
                response = {
                    'status': True,
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
                    'status': False,
                    'message': 'Error'
                }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 5)",
            }
        return response
