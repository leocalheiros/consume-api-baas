from abc import ABC, abstractmethod


class BaasReqInterface(ABC):
    @abstractmethod
    def operate(self, data: dict) -> any:
        pass
