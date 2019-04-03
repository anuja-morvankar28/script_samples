import logging
from flask import jsonify, request
from pygments.lexers import data
import requests
from api.item import Item


logger = logging.getLogger(__name__)


def get_demo_api():

    """
    get demo api
    as resopnse 200
    return the get demo api as response

     """
    logger.debug("in demo api")

   # task_1.delay()
    data = request.json
    if 'name' not in data:
        return jsonify(data['name']),400
    item = Item(name=data['name'])
    return jsonify({'message': "demo get api"}), 200


def post_demo_api():
    
    """
    post demo api
    as resopnse 200
    return the post demo api as response

     """
    logger.getLogger("in demo api")

    data = request.json
    if 'name' not in data:
        return jsonify(data['name']),400
    item = Item(name=data['name'])
    return jsonify({'message': "demo post api"}),200


def delete_api():
    
    
    """
    delete demo api
    as resopnse 200
    return the delete demo api as response

     """
    logger.debug("in demo api")
    data = request.json
    if 'name' not in data:
        return jsonify(data['name']), 400
    item = Item.objects(name=data['name']).delete()
    return jsonify({'message': "demo delete api"}), 200
