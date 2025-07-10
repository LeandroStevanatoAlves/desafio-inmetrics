from datetime import datetime
from model.cartao import Cartao
from model.usuario import Usuario


class CardFactory:
    @staticmethod
    def create(user: Usuario) -> Cartao:
        year_current = datetime.now().year
        # Due date will be in 5 years in the future
        year_future = str(year_current + 5)[-2:]
        return Cartao(
            "4886123456789012",
            f"{user.primeiro_nome} {user.ultimo_nome}",
            "567",
            f"1220{year_future}"
        )
