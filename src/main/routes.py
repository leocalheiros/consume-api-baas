from flask import Blueprint, request, jsonify
from src.main.composer.req_type_composer import req_type_composer
from src.main.adapter.request_adapter import request_adapter

account_blueprint = Blueprint('account', __name__)


@account_blueprint.route('/execute', methods=['POST'])
def type_route():
    http_response = request_adapter(request, req_type_composer())
    return jsonify(http_response.body, http_response.status_code)

