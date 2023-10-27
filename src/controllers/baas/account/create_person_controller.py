import requests
from src.controllers.baas.interface.baas_controller_interface import BaasControllerInterface


class CreatePersonController(BaasControllerInterface):
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def operate(self, person_data: dict) -> any:
        self.__validate(person_data)
        email = person_data.get("email")
        senha = person_data.get("senha")
        saldo = person_data.get("saldo")
        account_information = {
            "email": email,
            "senha": senha,
            "saldo": saldo
        }
        response = requests.post(self.api_url, json=account_information)
        return self.__format_response(response)

    def __validate(self, person_data: dict) -> None:
        if 'saldo' not in person_data or person_data['saldo'] is None:
            person_data['saldo'] = 0

    def __format_response(self, response):
        return self.__parse_api_response(response), response.status_code

    def __parse_api_response(self, response) -> dict:
        return response.json()

