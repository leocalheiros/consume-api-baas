from abc import ABC, abstractmethod


class BaasControllerInterface(ABC):
    @abstractmethod
    def operate(self, request_data: dict) -> dict:
        pass
