from src.controllers.interface.request_interface import RequestInterface
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface


class CreatePersonController(RequestInterface):
    def __init__(self, api_consumer: ApiConsumerInterface, api_method: str, api_url: str) -> None:
        self.__api_consumer = api_consumer
        self.api_method = api_method
        self.api_url = api_url
        self.api_headers = {
            "Content-type": "application/json",
        }

    def send_request(self, person_data: dict) -> any:
        self.__validate(person_data)
        email = person_data.get("email")
        senha = person_data.get("senha")
        saldo = person_data.get("saldo")
        account_information = {
            "email": email,
            "senha": senha,
            "saldo": saldo
        }
        response = self.__api_consumer.request_response(self.api_method, self.api_url, self.api_headers,
                                                        account_information)
        return response

    def __validate(self, person_data: dict) -> None:
        if 'saldo' not in person_data or person_data['saldo'] is None:
            person_data['saldo'] = 0
