from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.payments.register_credit_card_controller import RegisterCreditCardController
from src.views.send_request_view import SendRequestView


def register_card_composer():
    consumer = ApiConsumer()
    controller = RegisterCreditCardController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/register-credit-card')
    view = SendRequestView(controller)
    return view
