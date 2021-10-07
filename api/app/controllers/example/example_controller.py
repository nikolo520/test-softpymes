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
    def get_index(params = {}):
        response = {
            'status': False,
            'message': "No se encontraron registros",
            'data':[]
        }
        try:
            registros = db.session.query(ExampleModel).all()
            # name = params.get('name',False)
            # top = params.get('top',False)
            
            # if name:
            #     registros = db.session.query(ExampleModel).filter(ExampleModel.name.contains(name)).all()#paginate(page=1, per_page=10, error_out=False).scalar() #filter(ExampleModel.name.like(name + '%'))
            
            if len(registros)>0:
                response['status']=True
                response['message'] = 'Consulta exitosa'
                for registro in registros:
                    temp = {
                        "id" : registro.id,
                        "name" : registro.name,
                        "description" : registro.description,
                        "status" : registro.status
                    }
                    response['data'].append(temp)
            else:
                response['message'] = 'No se encontraron registros'
            
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response = {
                'status': False,
                'message': "Error al intentar consultar la información (ERROR_CODE => 1)",
            }
        return response
    
    @staticmethod
    def detail(id):
        response = {
            'status': False,
            'message': "No se encontraron modelos con este id",
            'data':{}
        }
        
        try:
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
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response['message'] ="Error al intentar consultar la información (ERROR_CODE => 2)"
        return response

    @staticmethod
    def create(data):
        response = {
                    'status': False,
                    'message': "Complete los campos requeridos"
                }
        try:
            name = data.get('name',False)
            identification = data.get('identification',False)
            description = data.get('description',False)
            if name and identification and description:
                objeto = ExampleModel(
                    name=data['name'],
                    identification=data['identification'],
                    description=data['description'],
                    status=True
                    )
                objeto.save()
                response = {
                    'status': True,
                    'message': 'Regitro creado exitosamente'
                }

        except Exception as e:
            print('Error: {er}'.format(er=e))
            response['message'] = "Error al intentar consultar la información (ERROR_CODE => 3)"
        return response
    
    @staticmethod
    def edit(id,data):
        response = {
            'status': False,
            'message': "No se encontraron registros con este id",
        }
        try:
            objeto = db.session.query(ExampleModel).filter_by(id=id).first()
            if objeto:
                name = data.get('name',False)
                identification = data.get('identification',False)
                description = data.get('description',False)
                status = data.get('status',False)
                if name:
                    objeto.name=name
                if identification:
                    objeto.identification=identification
                if description:
                    objeto.description=description
                if status:
                    objeto.status=status
                objeto.update()
                response = {
                    'status': True,
                    'message': 'Regitro actualizado exitosamente'
                }
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response['message'] = "Error al intentar consultar la información (ERROR_CODE => 4)"
        return response

    @staticmethod
    def delete(id):
        response = {
            'status': False,
            'message': 'No se encontraron registros con este id'
        }
        try:
            objeto = db.session.query(ExampleModel).filter_by(id=id).first()
            if objeto:
                objeto.delete()
                response['status'] = True
                response['message'] = "Se eliminó el registro exitosamente"
        except Exception as e:
            print('Error: {er}'.format(er=e))
            response['message'] = "Error al intentar consultar la información (ERROR_CODE => 5)"
        return response
