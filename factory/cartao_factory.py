from datetime import datetime
from model.cartao import Cartao
from model.usuario import Usuario


class CartaoFactory:
    @staticmethod
    def criar(usuario: Usuario) -> Cartao:
        ano_atual = datetime.now().year
        # Utiliza o ano do vencimento como sendo 5 anos no futuro
        ano_futuro = str(ano_atual + 5)[-2:]
        return Cartao(
            "4886123456789012",
            f"{usuario.primeiro_nome} {usuario.ultimo_nome}",
            "567",
            f"1220{ano_futuro}"
        )
