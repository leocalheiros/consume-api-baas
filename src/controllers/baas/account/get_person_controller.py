from src.controllers.interface.request_interface import RequestInterface
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict
from flask import request


class GetPersonController(RequestInterface):
    def __init__(self, api_consumer: ApiConsumerInterface, api_method: str, api_url: str) -> None:
        self.__api_consumer = api_consumer
        self.api_method = api_method
        self.api_url = api_url
        self.api_headers = {
            "Content-type": "application/json",
            "email": f"{request.headers.get('email')}",
            "Authorization": f"Bearer {request.headers.get('Authorization').replace('Bearer ', '')}"
        }

    def send_request(self, person_data: Dict[str, str]) -> any:
        email = person_data.get("email")
        self.__validate(email)
        account_information = {
            "email": email,
        }

        response = self.__api_consumer.request_response(self.api_method, self.api_url, self.api_headers, account_information)
        return response

    def __validate(self, email: str):
        if email != request.headers.get("email"):
            raise HttpUnprocessableEntityError(
                "O email da solicitação e dos headers devem ser iguais ao utilizado para gerar o token jwt")


