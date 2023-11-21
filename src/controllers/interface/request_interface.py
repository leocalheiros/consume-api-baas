from typing import Dict
from abc import ABC, abstractmethod


class RequestInterface(ABC):

    @abstractmethod
    def send_request(self, request_data) -> Dict: pass
