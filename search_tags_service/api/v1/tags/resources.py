from flask import Blueprint, jsonify, request

from search_tags_service.services.v1.tags import get_tags

blueprint = Blueprint('public_tags_api', __name__, url_prefix='/v1')


def get_tags_by_text():
    result = get_tags(request.json['text'])
    return jsonify(result)


blueprint.add_url_rule('/tags', view_func=get_tags_by_text, methods=['POST'])
