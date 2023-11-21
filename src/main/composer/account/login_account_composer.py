from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.account.login_controller import LoginController
from src.views.send_request_view import SendRequestView


def login_account_composer():
    consumer = ApiConsumer()
    controller = LoginController(consumer, api_method='POST', api_url='https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/login')
    view = SendRequestView(controller)
    return view
