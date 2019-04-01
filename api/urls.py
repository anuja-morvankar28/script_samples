from flask import Blueprint
from api.demo_api import get_demo_api

api = Blueprint('api', __name__)
"""
    here we defined class field names

    """
api.add_url_rule('/demo-api/https://angus.readthedocs.io/en/2016/LC-github.html', view_func=get_demo_api, methods=['GET'])