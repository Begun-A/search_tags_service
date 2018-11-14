from flask import Blueprint, jsonify

blueprint = Blueprint('public_tags_api', __name__, url_prefix='/v1')


def get_tags():
    return jsonify('Need implement algorigthm')


blueprint.add_url_rule('/tags', view_func=get_tags, methods=['GET'])
