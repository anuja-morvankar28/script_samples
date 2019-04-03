from flask import Blueprint
from api.demo_api import get_demo_api

api = Blueprint('api', __name__)
"""
    here we defined class field names

    """
api_v1.add_url_rule('/demo-api/', view_func=get_demo_api, methods=['GET'])
api_v1.add_url_rule('/demo-api/', view_func=post_demo_api, methods=['POST'])
api_v1.add_url_rule('/demo-api/', view_func=delete_api, methods=['DELETE'])
