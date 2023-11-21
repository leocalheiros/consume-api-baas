from flask import request
from src.controllers.interface.request_interface import RequestInterface
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class TransferSaldoController(RequestInterface):
    def __init__(self, api_consumer: ApiConsumerInterface, api_method: str, api_url: str) -> None:
        self.__api_consumer = api_consumer
        self.api_method = api_method
        self.api_url = api_url
        self.api_headers = {
            "Content-type": "application/json",
            "email": f"{request.headers.get('email')}",
            "Authorization": f"Bearer {request.headers.get('Authorization').replace('Bearer ', '')}"
        }

    def send_request(self, request_data: dict) -> any:
        source_email = request_data.get("source_email")
        target_email = request_data.get("target_email")
        amount = request_data.get("amount")

        self.__validate(source_email)
        account_information = {
            "source_email": source_email,
            "target_email": target_email,
            "amount": amount
        }

        response = self.__api_consumer.request_response(self.api_method, self.api_url, self.api_headers,
                                                        account_information)
        return response

    def __validate(self, email: str):
        if email != request.headers.get("email"):
            raise HttpUnprocessableEntityError(
                "O email da solicitação e dos headers devem ser iguais ao utilizado para gerar o token jwt")
