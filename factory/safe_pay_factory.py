from model.safe_pay import SafePay
from model.usuario import Usuario
from unidecode import unidecode


class SafePayFactory:
    @staticmethod
    def create(user: Usuario) -> SafePay:
        username_first_name = unidecode(user.primeiro_nome).replace(" ", "").lower()
        username_last_name = unidecode(user.ultimo_nome).replace(" ", "").lower()
        username = f"{username_first_name}{username_last_name}"
        return SafePay(
            username[: 10],
            "Aa123456"
        )
