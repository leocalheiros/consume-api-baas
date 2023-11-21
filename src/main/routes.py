from flask import Blueprint, request, jsonify
from src.main.composer.account.login_account_composer import login_account_composer
from src.main.composer.account.get_account_composer import get_account_composer
from src.main.composer.account.create_account_composer import create_account_composer
from src.main.composer.payments.create_payment_composer import create_payment_composer
from src.main.composer.payments.register_credit_card_composer import register_card_composer
from src.main.composer.saldo.deposit_saldo_composer import deposit_saldo_composer
from src.main.composer.saldo.transfer_saldo_composer import transfer_saldo_composer
from src.main.composer.saldo.withdraw_saldo_composer import withdraw_saldo_composer
from src.main.composer.req_type_composer import req_type_composer
from src.errors.error_handler import handle_errors
from src.main.adapter.request_adapter import request_adapter

account_blueprint = Blueprint('account', __name__)
payments_blueprint = Blueprint('payments', __name__)
balance_blueprint = Blueprint('balance', __name__)
type_blueprint = Blueprint('type', __name__)


@type_blueprint.route('/operate', methods=['POST'])
def operate_route():
    http_response = None

    try:
        http_response = request_adapter(request, req_type_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@account_blueprint.route('/account/login', methods=['POST'])
def login_route():
    http_response = None

    try:
        http_response = request_adapter(request, login_account_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@account_blueprint.route('/account/get-self-person', methods=['POST'])
def get_self_person_route():
    http_response = None

    try:
        http_response = request_adapter(request, get_account_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@account_blueprint.route('/account/create-person', methods=['POST'])
def create_person_route():
    http_response = None

    try:
        http_response = request_adapter(request, create_account_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@payments_blueprint.route('/payments/create-payment', methods=['POST'])
def create_person_route():
    http_response = None

    try:
        http_response = request_adapter(request, create_payment_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@payments_blueprint.route('/payments/register-card', methods=['POST'])
def create_card_route():
    http_response = None

    try:
        http_response = request_adapter(request, register_card_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@balance_blueprint.route('/balance/deposit', methods=['POST'])
def deposit_balance_route():
    http_response = None

    try:
        http_response = request_adapter(request, deposit_saldo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@balance_blueprint.route('/balance/transfer', methods=['POST'])
def transfer_balance_route():
    http_response = None

    try:
        http_response = request_adapter(request, transfer_saldo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@balance_blueprint.route('/balance/withdraw', methods=['POST'])
def withdraw_balance_route():
    http_response = None

    try:
        http_response = request_adapter(request, withdraw_saldo_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
