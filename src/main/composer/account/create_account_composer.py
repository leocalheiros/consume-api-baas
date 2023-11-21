from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.account.create_person_controller import CreatePersonController
from src.views.send_request_view import SendRequestView


def create_account_composer():
    consumer = ApiConsumer()
    controller = CreatePersonController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-person')
    view = SendRequestView(controller)
    return view
