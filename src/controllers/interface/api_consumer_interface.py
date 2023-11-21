from typing import Tuple, Type, Dict
from requests import Request
from abc import ABC, abstractmethod


class ApiConsumerInterface(ABC):

    @abstractmethod
    def request_response(
        self,
        method: str,
        url: str,
        headers: Dict[str, str] = None,
        json: Dict = None
    ) -> Dict:
        pass
