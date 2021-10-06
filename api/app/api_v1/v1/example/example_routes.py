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
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/detail/<id>', methods=['POST'])
def detail(id):
    response = Controller.detail(id)
    return jsonify(data=response)

@api.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        if request.form:
            response = Controller.create(request.form)
            return jsonify(data=response)
    else:
        return jsonify(data={'ok':False, 'message':'Bad Request'})


@api.route('/edit/<id>', methods=['POST'])
def edit(id):
    response = Controller.edit()
    return jsonify(data=response)

@api.route('/del/<id>', methods=['POST'])
def delete(id):
    response = Controller.delete(id)
    return jsonify(data=response)