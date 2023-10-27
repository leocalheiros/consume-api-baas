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
    def operate(self, data: dict) -> any:
        action = data.get("action")

        if action == "create-person":
            create_person_controller = CreatePersonController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-person')
            return create_person_controller.operate(data)
        elif action == 'login':
            login_controller = LoginController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/login')
            return login_controller.operate(data)
        elif action == 'get-person':
            get_person_controller = GetPersonController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/get-person')
            return get_person_controller.operate(data)
        elif action == 'deposit-saldo':
            deposit_saldo_controller = DepositSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/deposit-saldo')
            return deposit_saldo_controller.operate(data)
        elif action == 'transfer-saldo':
            transfer_saldo_controller = TransferSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/transfer-saldo')
            return transfer_saldo_controller.operate(data)
        elif action == 'withdraw-saldo':
            withdraw_saldo_controller = WithdrawSaldoController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/withdraw-saldo')
            return withdraw_saldo_controller.operate(data)
        elif action == 'register-credit-card':
            register_credit_card_controller = RegisterCreditCardController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/register-credit-card')
            return register_credit_card_controller.operate(data)
        elif action == 'create-payment':
            create_payment_controller = CreatePaymentController('https://x0wiy4jqdf.execute-api.us-east-1.amazonaws.com/Prod/create-payment')
            return create_payment_controller.operate(data)
        else:
            raise HttpInvalidActionError("Action inválida!")
