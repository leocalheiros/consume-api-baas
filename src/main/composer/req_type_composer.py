from src.views.req_type_view import ReqTypeView
from src.controllers.type_controller import TypeController
from src.controllers.baas.baas_req_controller import BaasReqController


def req_type_composer():
    baas_controller = BaasReqController()
    controller = TypeController(baas_controller)
    view = ReqTypeView(controller)
    return view
