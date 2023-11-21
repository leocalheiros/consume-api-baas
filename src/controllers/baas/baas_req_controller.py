from src.controllers.baas.interface.baas_req_interface_controller import BaasReqInterface
from src.infra.requests.api_consumer import ApiConsumer
from src.controllers.baas.account.create_person_controller import CreatePersonController
from src.controllers.baas.account.login_controller import LoginController
from src.controllers.baas.account.get_person_controller import GetPersonController
from src.controllers.baas.saldo.deposit_saldo_controller import DepositSaldoController
from src.controllers.baas.saldo.transfer_saldo_controller import TransferSaldoController
from src.controllers.baas.saldo.withdraw_saldo_controller import WithdrawSaldoController
from src.controllers.baas.payments.register_credit_card_controller import RegisterCreditCardController
from src.controllers.baas.payments.create_payment_controller import CreatePaymentController
from src.errors.types.http_invalid_action import HttpInvalidActionError


class BaasReqController(BaasReqInterface):
    def __init__(self):
        base_url = 'https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod'
        api_consumer = ApiConsumer()
        self.controllers = {
            "create-person": CreatePersonController(api_consumer, 'POST', f'{base_url}/create-person'),
            "login": LoginController(api_consumer, 'POST', f'{base_url}/login'),
            "get-person": GetPersonController(api_consumer, 'POST', f'{base_url}/get-person'),
            "deposit-saldo": DepositSaldoController(api_consumer, 'POST', f'{base_url}/deposit-saldo'),
            "transfer-saldo": TransferSaldoController(api_consumer, 'POST', f'{base_url}/transfer-saldo'),
            "withdraw-saldo": WithdrawSaldoController(api_consumer, 'POST', f'{base_url}/withdraw-saldo'),
            "register-credit-card": RegisterCreditCardController(api_consumer, 'POST', f'{base_url}/register-credit-card'),
            "create-payment": CreatePaymentController(api_consumer, 'POST', f'{base_url}/create-payment')
        }

    def operate(self, data: dict) -> any:
        action = data.get("action")
        controller = self.controllers.get(action)

        if controller:
            return controller.send_request(data)
        else:
            raise HttpInvalidActionError("Action inválida!")
