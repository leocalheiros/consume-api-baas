from src.controllers.interface.request_interface import RequestInterface
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface
from typing import Dict


class LoginController(RequestInterface):
    def __init__(self, api_consumer: ApiConsumerInterface, api_method: str, api_url: str) -> None:
        self.__api_consumer = api_consumer
        self.api_method = api_method
        self.api_url = api_url
        self.api_headers = {"Content-type": "application/json"}

    def send_request(self, request_data: Dict[str, str]) -> any:

        email = request_data.get("email")
        senha = request_data.get("senha")
        account_information = {
            "email": email,
            "senha": senha,
        }
        response = self.__api_consumer.request_response(self.api_method, self.api_url, self.api_headers, account_information)

        return self.__format_response(response)

    def __format_response(self, response: Dict) -> Dict:
        if "response" in response and "data" in response["response"]:
            data = response["response"]["data"]
            email = data.get("email")
            status = data.get("status")
            token = data.get("token")
            formatted_response = {
                "email": email,
                "status": status,
                "token": token,
            }

            return formatted_response

        # Se a estrutura não for como esperado, retorne a resposta original
        return response
