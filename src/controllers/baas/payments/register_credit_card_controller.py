from flask import request
from src.controllers.interface.request_interface import RequestInterface
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class RegisterCreditCardController(RequestInterface):
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
        email = request_data.get("email")
        card_number = request_data.get('card_number')
        expiration_month = request_data.get('expiration_month')
        expiration_year = request_data.get('expiration_year')
        security_code = request_data.get('security_code')
        holder_name = request_data.get('holder_name')

        self.__validate(email)
        account_information = {
            "email": email,
            "card_number": card_number,
            "expiration_month": expiration_month,
            "expiration_year": expiration_year,
            "security_code": security_code,
            "holder_name": holder_name
        }

        response = self.__api_consumer.request_response(self.api_method, self.api_url, self.api_headers,
                                                        account_information)
        return response

    def __validate(self, email: str):
        if email != request.headers.get("email"):
            raise HttpUnprocessableEntityError(
                "O email da solicitação e dos headers devem ser iguais ao utilizado para gerar o token jwt")
