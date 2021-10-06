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

@api.route('/detail/<id>', methods=['GET'])
def detail(id):
    response = Controller.detail(id)
    return jsonify(data=response)

# @api.route('/create', methods=['POST'])
# def create():
#     response = Controller.create()
#     return jsonify(data=response)

# @api.route('/edit', methods=['POST'])
# def edit(id):
#     response = Controller.edit()
#     return jsonify(data=response)

# @api.route('/del', methods=['POST'])
# def delete(id):
#     response = Controller.delete()
#     return jsonify(data=response)