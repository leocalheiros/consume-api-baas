from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.payments.create_payment_controller import CreatePaymentController
from src.views.send_request_view import SendRequestView


def create_payment_composer():
    consumer = ApiConsumer()
    controller = CreatePaymentController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-payment')
    view = SendRequestView(controller)
    return view
