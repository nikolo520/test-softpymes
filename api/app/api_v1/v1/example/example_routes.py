# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller


@api.route('/index', methods=['GET'])
def get_index():
    #http://127.0.0.1:5000/api/v1/get_index
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/detail/<id>', methods=['POST'])
def detail(id):
    #http://127.0.0.1:5000/api/v1/detail/id
    response = Controller.detail(id)
    return jsonify(data=response)

@api.route('/create', methods=['POST'])
def create():
    #http://127.0.0.1:5000/api/v1/create   ;;;;;; form-data
    if request.form:
        response = Controller.create(request.form)
        return jsonify(data=response)
    else:
        return jsonify(data={'ok':False, 'message':'Bad Request'})



@api.route('/edit/<id>', methods=['POST'])
def edit(id):
    #http://127.0.0.1:5000/api/v1/edit/id   ;;;;;; form-data
    if request.form:
        response = Controller.edit(id, request.form)
        return jsonify(data=response)
    else:
        return jsonify(data={'ok':False, 'message':'Bad Request'})

@api.route('/del/<id>', methods=['POST'])
def delete(id):
    #http://127.0.0.1:5000/api/v1/del/id
    response = Controller.delete(id)
    return jsonify(data=response)