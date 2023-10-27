import requests
from flask import request
from src.controllers.baas.interface.baas_controller_interface import BaasControllerInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.types.http_unauthorized import HttpUnauthorizedError


class DepositSaldoController(BaasControllerInterface):
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def operate(self, person_data: dict) -> any:
        email = person_data.get("email")
        amount = person_data.get("amount")
        token = request.headers.get("Authorization").replace("Bearer ", "")
        self.__validate(email)
        account_information = {
            "email": email,
            "amount": amount
        }
        headers = {
            "Authorization": f"Bearer {token}",
            "email": email
        }

        response = requests.post(self.api_url, json=account_information, headers=headers)
        return self.__format_response(response)

    def __validate(self, email: str):
        if email != request.headers.get("email"):
            raise HttpUnprocessableEntityError(
                "O email da solicitação e dos headers devem ser iguais ao utilizado para gerar o token jwt")

    def __format_response(self, response):
        if response.status_code == 401:
            error_response = response.json()
            if "error" in error_response and error_response["error"] == "Token inválido!":
                raise HttpUnauthorizedError("Token inválido!")
        return self.__parse_api_response(response), response.status_code

    def __parse_api_response(self, response) -> dict:
        return response.json()

