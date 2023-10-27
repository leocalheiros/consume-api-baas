from src.controllers.interface.type_controller_interface import TypeControllerInterface
from src.controllers.baas.baas_req_controller import BaasReqController
from src.errors.types.http_invalid_type import HttpInvalidTypeError
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class TypeController(TypeControllerInterface):
    def __init__(self, baas_controller: BaasReqController):
        self.baas_controller = baas_controller

    def operate(self, type_data: dict) -> any:
        self.__validate(type_data)
        type_name = type_data.get("type")
        if type_name == "baas":
            return self.baas_controller.operate(type_data)
        else:
            raise HttpInvalidTypeError("Type especificado inválido!")

    def __validate(self, type_data: dict) -> None:
        if 'type' not in type_data or 'action' not in type_data:
            raise HttpUnprocessableEntityError('Campos type e action são obrigatórios!')

