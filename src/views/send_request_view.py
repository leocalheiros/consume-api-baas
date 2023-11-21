from src.views.interface.views_interface import ViewInterface
from src.views.http_types.http_response import HttpResponse
from src.views.http_types.http_request import HttpRequest
from src.controllers.interface.request_interface import RequestInterface


class SendRequestView(ViewInterface):
    def __init__(self, request_handler: RequestInterface) -> None:
        self.__request_handler = request_handler

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        request_data = http_request.body
        response = self.__request_handler.send_request(request_data)

        return HttpResponse(
            status_code=200,
            body=response
        )
