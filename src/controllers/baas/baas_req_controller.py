from src.controllers.baas.interface.baas_req_interface_controller import BaasReqInterface
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
        self.controllers = {
            "create-person": CreatePersonController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-person'),
            "login": LoginController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/login'),
            "get-person": GetPersonController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/get-person'),
            "deposit-saldo": DepositSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/deposit-saldo'),
            "transfer-saldo": TransferSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/transfer-saldo'),
            "withdraw-saldo": WithdrawSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/withdraw-saldo'),
            "register-credit-card": RegisterCreditCardController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/register-credit-card'),
            "create-payment": CreatePaymentController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-payment')
        }

    def operate(self, data: dict) -> any:
        action = data.get("action")
        controller = self.controllers.get(action)

        if controller:
            return controller.operate(data)
        else:
            raise HttpInvalidActionError("Action inválida!")
