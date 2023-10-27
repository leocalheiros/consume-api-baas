from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.views_interface import ViewInterface
from src.controllers.interface.type_controller_interface import TypeControllerInterface
from src.errors.error_handler import handle_errors


class ReqTypeView(ViewInterface):
    def __init__(self, type_controller: TypeControllerInterface) -> None:
        self.__type_controller = type_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            type_data = http_request.body
            response, _ = self.__type_controller.operate(type_data)  # Ignorar o status code da nossa aplicação
            status_code = response[1]  # Pegar o status code da API externa
            response = response[0]  # Pegar a resposta da API externa
            return HttpResponse(status_code, body=response)
        except Exception as exception:
            return handle_errors(exception)
