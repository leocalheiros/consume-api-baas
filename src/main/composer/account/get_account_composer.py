from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.account.get_person_controller import GetPersonController
from src.views.send_request_view import SendRequestView


def get_account_composer():
    consumer = ApiConsumer()
    controller = GetPersonController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/get-person')
    view = SendRequestView(controller)
    return view
