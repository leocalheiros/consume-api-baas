from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request, PreparedRequest
from src.errors.types.http_request_error import HttpRequestError
from src.controllers.interface.api_consumer_interface import ApiConsumerInterface


class ApiConsumer(ApiConsumerInterface):
    def request_response(self, method: str, url: str, headers: Dict = None, data: Dict = None) -> Dict:
        response = self.__send_http_request(method, url, headers=headers, json=data)
        status_code = response.status_code

        if 200 <= status_code <= 299:
            return {
                "status_code": status_code,
                "request": {
                    "method": method,
                    "url": url,
                    "headers": headers,
                    "json": data
                },
                "result": response.json()
            }
        raise HttpRequestError(
            message=response.json()["errors"], status_code=status_code
        )

    @classmethod
    def __send_http_request(cls, method: str, url: str, **kwargs) -> any:
        response = requests.request(method=method, url=url, **kwargs)
        return response
