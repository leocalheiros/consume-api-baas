from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.saldo.transfer_saldo_controller import TransferSaldoController
from src.views.send_request_view import SendRequestView


def transfer_saldo_composer():
    consumer = ApiConsumer()
    controller = TransferSaldoController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/transfer-saldo')
    view = SendRequestView(controller)
    return view
