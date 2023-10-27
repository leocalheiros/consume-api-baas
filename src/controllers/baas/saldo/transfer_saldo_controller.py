import requests
from flask import request
from src.controllers.baas.interface.baas_controller_interface import BaasControllerInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.types.http_unauthorized import HttpUnauthorizedError


class TransferSaldoController(BaasControllerInterface):
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def operate(self, person_data: dict) -> any:
        source_email = person_data.get("source_email")
        target_email = person_data.get("target_email")
        amount = person_data.get("amount")
        token = request.headers.get("Authorization").replace("Bearer ", "")
        self.__validate(source_email)
        account_information = {
            "source_email": source_email,
            "target_email": target_email,
            "amount": amount
        }
        headers = {
            "Authorization": f"Bearer {token}",
            "email": source_email
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

