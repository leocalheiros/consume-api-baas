from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.saldo.withdraw_saldo_controller import WithdrawSaldoController
from src.views.send_request_view import SendRequestView


def withdraw_saldo_composer():
    consumer = ApiConsumer()
    controller = WithdrawSaldoController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/withdraw-saldo')
    view = SendRequestView(controller)
    return view
