from abc import ABC, abstractmethod


class TypeControllerInterface(ABC):
    @abstractmethod
    def operate(self, type_data: dict) -> any:
        pass
