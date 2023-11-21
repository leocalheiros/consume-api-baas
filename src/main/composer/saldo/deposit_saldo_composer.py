from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.saldo.deposit_saldo_controller import DepositSaldoController
from src.views.send_request_view import SendRequestView


def deposit_saldo_composer():
    consumer = ApiConsumer()
    controller = DepositSaldoController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/deposit-saldo')
    view = SendRequestView(controller)
    return view
